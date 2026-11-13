"""One way to ask a model. Every reply is JSON unless as_json=False.

A model name is either an Ollama model on this box (free), e.g. "gemma4:26b", or "or:<openrouter id>", e.g.
"or:google/gemini-3-flash-preview" (paid, written to runs/ledger.jsonl, refused past C2V_CAP_USD), or
"claude:<model id>", e.g. "claude:claude-sonnet-5-5" (paid, Anthropic API through bench/claude_call.py in .venv-claude;
written to runs/ledger_claude.jsonl with tokens and dollars, refused past C2V_CLAUDE_CAP_USD).

OpenRouter key: C2V_OPENROUTER_KEY (a key of its own for this study is best), else OPENROUTER_API_KEY, else the
OPENROUTER_API_KEY in the .env file named by C2V_ENV. The key is never printed or written anywhere.
"""

from __future__ import annotations

import base64
import contextlib
import json
import os
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

OLLAMA = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
# More Ollama servers on this box, comma-separated ("127.0.0.1:11435,127.0.0.1:11436"). The main server runs one
# request at a time per model, so calls queue (the student took 193 s a call with four in flight). A server is used
# for a model only if its build of that model has the main server's digest; unset, every call goes to OLLAMA as before.
OLLAMA_EXTRA = [u.strip() for u in os.getenv("C2V_OLLAMA_EXTRA", "").split(",") if u.strip()]
# A run can name the build it wants instead: C2V_OLLAMA_PIN="gemma4:26b@001e5dafc3c7" (the ID `ollama list` shows).
# That model is then served only by the servers that hold this build, and the main server is left out when its build
# is another one. One run never mixes two builds of a model; scores from two builds are not to be compared unchecked.
OLLAMA_PIN = dict(x.strip().rsplit("@", 1) for x in os.getenv("C2V_OLLAMA_PIN", "").split(",") if "@" in x)
OPENROUTER = "https://openrouter.ai/api/v1/chat/completions"
LEDGER = Path(os.getenv("C2V_LEDGER", Path(__file__).resolve().parents[1] / "runs" / "ledger.jsonl"))
CAP_USD = float(os.getenv("C2V_CAP_USD", "1.00"))
ROOT = Path(__file__).resolve().parents[1]
CLAUDE_LEDGER = Path(os.getenv("C2V_CLAUDE_LEDGER", ROOT / "runs" / "ledger_claude.jsonl"))
CLAUDE_CAP_USD = float(os.getenv("C2V_CLAUDE_CAP_USD", "30.00"))
CONTEXT = threading.local()  # CONTEXT.tag names the unit of work (e.g. one topic) in the Claude ledger
CLAUDE_EFFORT = os.getenv("C2V_CLAUDE_EFFORT", "medium")
CLAUDE_ENV = Path(os.getenv("C2V_CLAUDE_ENV", "/home/mani/manim/lessonforge/.env"))
# USD per million tokens (input, output), Anthropic first-party prices
CLAUDE_PRICE = {"claude-haiku-5-5": (0.10, 0.50), "claude-sonnet-5-5": (2.0, 10.0), "claude-sonnet-5": (2.0, 10.0),
                "claude-opus-5-5": (4.0, 20.0), "claude-opus-5": (5.0, 25.0), "claude-opus-4-8": (5.0, 25.0)}  # fmt: skip

# Defaults are all local and free. Override any of them with an "or:..." id to use OpenRouter.
PLANNER = os.getenv("C2V_PLANNER", "qwen3.6:latest")  # outlines, quizzes (text only: it crashes with images here)
CODER = os.getenv("C2V_CODER", "qwen3-coder:30b")  # Manim code and its repairs
STUDENT = os.getenv("C2V_STUDENT", "gemma4:26b")  # the unlearned student (forgets properly; qwen2.5vl does not)
JUDGE = os.getenv("C2V_JUDGE", "qwen2.5vl:7b")  # evidence judge, another family than the student


def spent():
    if not LEDGER.exists():
        return 0.0
    return sum(json.loads(line).get("usd", 0.0) for line in LEDGER.read_text().splitlines() if line.strip())


LOCAL_LEDGER = Path(os.getenv("C2V_LOCAL_LEDGER", ROOT / "runs" / "ledger_local.jsonl"))
# What a local model would cost on OpenRouter (USD per million tokens, input / output; read 2026-11-13). qwen2.5vl:7b
# is not listed; qwen3-vl-8b-instruct is the nearest model offered.
OPENROUTER_EQUIV = {"qwen3.6:latest": ("qwen/qwen3.6-35b-a3b", 0.10, 0.90),
                    "qwen3-coder:30b": ("qwen/qwen3-coder-30b-a3b-instruct", 0.15, 0.60),
                    "gemma4:26b": ("google/gemma-4-26b-a4b-it", 0.09, 0.30),
                    "qwen2.5vl:7b": ("qwen/qwen3-vl-8b-instruct", 0.25, 0.75),
                    "qwen2.5vl:3b": ("qwen/qwen3-vl-8b-instruct", 0.25, 0.75)}  # fmt: skip


def _chat_url(server):
    url = server if server.startswith("http") else f"http://{server}"
    return url if url.endswith("/api/chat") else url.rstrip("/") + "/api/chat"


def _digest(chat_url, model):
    """The digest a server reports for a model (what `ollama list` shows as ID), or None."""
    try:
        with urllib.request.urlopen(chat_url.rsplit("/api/", 1)[0] + "/api/tags", timeout=10) as r:
            tags = json.load(r)
    except Exception:  # noqa: BLE001 - a server that does not answer is not used
        return None
    return next((m.get("digest") for m in tags.get("models") or [] if model in (m.get("name"), m.get("model"))), None)


_SERVERS: dict[str, list[str]] = {}  # model -> chat URLs that hold the main server's build of it (the main one first)
_BUSY: dict[str, int] = {}  # calls in flight per chat URL, from this process
_TURN = [os.getpid()]  # processes start at different servers, so they do not all pick the main one first
_LOCK = threading.Lock()


def servers(model):
    """Chat URLs that may serve this model: the main server, and each extra server whose digest for it is the same.
    With a pinned build (OLLAMA_PIN), every server that holds that build and no other. Checked once per process and
    model."""
    with _LOCK:
        if model not in _SERVERS:
            pin = OLLAMA_PIN.get(model, "").removeprefix("sha256:")
            if pin:
                found = {u: _digest(u, model) or "" for u in dict.fromkeys([OLLAMA, *map(_chat_url, OLLAMA_EXTRA)])}
                ok = [u for u, d in found.items() if d.removeprefix("sha256:").startswith(pin)]
                if not ok:
                    raise RuntimeError(f"{model}: no server holds the pinned build {pin} "
                                       f"({ {u: d[:12] for u, d in found.items()} })")  # fmt: skip
                print(f"[llm] {model} build {pin} is served by {ok}", file=sys.stderr)
            else:
                ok = [OLLAMA]
                want = _digest(OLLAMA, model) if OLLAMA_EXTRA else None
                for url in map(_chat_url, OLLAMA_EXTRA):
                    got = _digest(url, model) if want else None
                    if want and got == want and url not in ok:
                        ok.append(url)
                    else:
                        print(f"[llm] {url} is not used for {model}: its digest is {str(got)[:12]}, the main "
                              f"server's is {str(want)[:12]}", file=sys.stderr)  # fmt: skip
            _SERVERS[model] = ok
        return list(_SERVERS[model])


@contextlib.contextmanager
def _server(model):
    """The least busy server for this model, counted as busy for the length of the call. An extra server that fails
    is dropped for the rest of the process; the caller's next try goes to another one."""
    urls = servers(model)
    with _LOCK:
        low = min(_BUSY.get(u, 0) for u in urls)
        free = [u for u in urls if _BUSY.get(u, 0) == low]
        url = free[_TURN[0] % len(free)]
        _TURN[0] += 1
        _BUSY[url] = _BUSY.get(url, 0) + 1
    try:
        yield url
    except Exception:
        if url != OLLAMA:
            with _LOCK:
                for kept in _SERVERS.values():
                    if url in kept and len(kept) > 1:  # the last server of a model stays: its error is the one seen
                        kept.remove(url)
            print(f"[llm] {url} failed and is no longer used by this process", file=sys.stderr)
        raise
    finally:
        with _LOCK:
            _BUSY[url] -= 1


def log_local(model, note, tin, tout, seconds, server=None):
    """Tokens of one local (Ollama) call, priced as if the same model ran on OpenRouter."""
    _, pin, pout = OPENROUTER_EQUIV.get(model, (None, 0.0, 0.0))
    LOCAL_LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LOCAL_LEDGER.open("a") as f:
        f.write(json.dumps({"t": round(time.time()), "model": model, "note": note, "study": os.getenv("C2V_STUDY", ""),
                            "tag": getattr(CONTEXT, "tag", ""), "in": tin, "out": tout,
                            "usd_openrouter": round((tin * pin + tout * pout) / 1e6, 6), "s": round(seconds, 1),
                            **({"server": server} if server else {})}) + "\n")  # fmt: skip


def claude_spent():
    if not CLAUDE_LEDGER.exists():
        return 0.0
    return sum(json.loads(line).get("usd", 0.0) for line in CLAUDE_LEDGER.read_text().splitlines() if line.strip())


def _claude(model, messages, images, note):
    """One Claude request in its own environment; tokens and dollars go to the Claude ledger. The key is read from the
    .env file into the subprocess environment only, never printed."""
    import subprocess

    if claude_spent() >= CLAUDE_CAP_USD:
        raise RuntimeError(f"Claude cap reached ({claude_spent():.3f} of {CLAUDE_CAP_USD} USD); raise C2V_CLAUDE_CAP_USD")
    env = dict(os.environ)
    if "ANTHROPIC_API_KEY" not in env and CLAUDE_ENV.exists():
        for line in CLAUDE_ENV.read_text().splitlines():
            if line.startswith("ANTHROPIC_API_KEY="):
                env["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
    system = "\n\n".join(m["content"] for m in messages if m["role"] == "system") or "You are a careful assistant."
    req = {"system": system, "text": messages[-1]["content"], "images": [str(i) for i in images],
           "model": model, "effort": CLAUDE_EFFORT, "max_tokens": 16000}  # fmt: skip
    began = time.time()
    r = subprocess.run([str(ROOT / ".venv-claude" / "bin" / "python"), str(ROOT / "bench" / "claude_call.py")],
                       input=json.dumps(req), capture_output=True, text=True, env=env, timeout=1200, check=False)  # fmt: skip
    if r.returncode:
        raise RuntimeError(f"claude_call failed: {r.stderr[-400:]}")
    out = json.loads(r.stdout)
    served = out["model"]
    pin, pout = CLAUDE_PRICE.get(served, CLAUDE_PRICE.get(model, (4.0, 20.0)))
    tin, tout = out["usage"]["input_tokens"], out["usage"]["output_tokens"]
    CLAUDE_LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with CLAUDE_LEDGER.open("a") as f:
        f.write(json.dumps({"t": round(began), "model": model, "served": served, "note": note,
                            "study": os.getenv("C2V_STUDY", ""), "tag": getattr(CONTEXT, "tag", ""), "in": tin, "out": tout,
                            "usd": round((tin * pin + tout * pout) / 1e6, 6), "s": round(time.time() - began, 1),
                            "stop": out["stop_reason"]}) + "\n")  # fmt: skip
    if out["stop_reason"] == "refusal":
        raise RuntimeError(f"{model}: refused")
    return out["text"] or ""


def _key():
    key = os.getenv("C2V_OPENROUTER_KEY") or os.getenv("OPENROUTER_API_KEY")
    if not key and os.getenv("C2V_ENV"):
        for line in Path(os.environ["C2V_ENV"]).read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                key = line.split("=", 1)[1].strip().strip("'\"")
    if not key:
        raise RuntimeError("no OpenRouter key: set C2V_OPENROUTER_KEY, or C2V_ENV=<path to a .env>")
    return key


def _parse(text, as_json):
    if not as_json:
        return text
    return json.loads(text[text.find("{") : text.rfind("}") + 1])


def _ollama(model, messages, images, temperature, seed, ctx, as_json, note=""):
    if images:
        messages[-1]["images"] = [base64.b64encode(Path(i).read_bytes()).decode() for i in images]
    body = {
        "model": model,
        "stream": False,
        "think": False,
        "messages": messages,
        "options": {"temperature": temperature, "seed": seed, "num_ctx": ctx},
    }
    if as_json:
        body["format"] = "json"
    data = json.dumps(body).encode()
    began = time.time()
    with _server(model) as url:
        req = urllib.request.Request(url, data, {"Content-Type": "application/json"})
        r = json.load(urllib.request.urlopen(req, timeout=900))
    log_local(model, note, r.get("prompt_eval_count") or 0, r.get("eval_count") or 0, time.time() - began, server=url)
    return r["message"]["content"]


def _openrouter(model, messages, images, temperature, seed, as_json, note, video=None):
    if spent() >= CAP_USD:
        raise RuntimeError(f"study cap reached ({spent():.3f} of {CAP_USD} USD); raise C2V_CAP_USD to go on")
    if images:
        parts = [
            {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + base64.b64encode(Path(i).read_bytes()).decode()}}
            for i in images
        ]  # fmt: skip
        messages[-1]["content"] = [*parts, {"type": "text", "text": messages[-1]["content"]}]
    if video:  # a whole mp4, as Code2Video sends it to Gemini (base64 data URL)
        data = "data:video/mp4;base64," + base64.b64encode(Path(video).read_bytes()).decode()
        text = messages[-1]["content"]
        messages[-1]["content"] = [{"type": "text", "text": text}, {"type": "video_url", "video_url": {"url": data}}]
    body = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "seed": seed,
        "max_tokens": 8000,
        "usage": {"include": True},
        "reasoning": {"enabled": False},  # a thinking model spends its budget thinking and returns nothing
    }
    if as_json:
        body["response_format"] = {"type": "json_object"}
    began = time.time()
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + _key(), "X-Title": "c2v-lab"}
    try:
        reply = json.load(
            urllib.request.urlopen(urllib.request.Request(OPENROUTER, json.dumps(body).encode(), headers), timeout=600)
        )
    except urllib.error.HTTPError as exc:
        if exc.code != 400:
            raise
        # a model that must think (gemini-2.5-pro, gpt-5-mini): let it think a little, with room to answer
        body.update(reasoning={"effort": "low"}, max_tokens=20000)
        reply = json.load(
            urllib.request.urlopen(urllib.request.Request(OPENROUTER, json.dumps(body).encode(), headers), timeout=600)
        )
    usage = reply.get("usage") or {}
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a") as f:
        f.write(json.dumps({
            "t": round(began), "model": model, "note": note, "usd": float(usage.get("cost") or 0.0),
            "in": usage.get("prompt_tokens"), "out": usage.get("completion_tokens"),
            "s": round(time.time() - began, 1),
        }) + "\n")  # fmt: skip
    return reply["choices"][0]["message"]["content"] or ""


def ask_logprobs(model, prompt, images=(), system=None, max_tokens=64, seed=0, top=20, ctx=32768, tries=4):
    """A local (Ollama) reply at temperature 0 with the top log-probabilities of every generated token."""
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
    if images:
        messages[-1]["images"] = [base64.b64encode(Path(i).read_bytes()).decode() for i in images]
    body = {"model": model, "stream": False, "think": False, "messages": messages, "logprobs": True,
            "top_logprobs": top, "options": {"temperature": 0, "seed": seed, "num_ctx": ctx, "num_predict": max_tokens}}  # fmt: skip
    last = None
    for attempt in range(tries):
        try:
            began = time.time()
            with _server(model) as url:
                req = urllib.request.Request(url, json.dumps(body).encode(), {"Content-Type": "application/json"})
                r = json.load(urllib.request.urlopen(req, timeout=1800))
            used = r.get("prompt_eval_count") or 0
            log_local(model, "probe", used, r.get("eval_count") or 0, time.time() - began, server=url)
            if used + max_tokens >= ctx:
                raise RuntimeError(f"{model}: prompt of {used} tokens fills the context of {ctx}; it was truncated")
            return {"text": r["message"]["content"], "logprobs": r.get("logprobs") or [], "prompt_tokens": used}
        except RuntimeError:
            raise
        except Exception as exc:  # noqa: BLE001 - shared GPUs: ask again
            last = exc
        time.sleep(3 + attempt * 8)
    raise RuntimeError(f"{model}: no usable reply ({last})")


def ask(
    model,
    prompt,
    images=(),
    system=None,
    temperature=0.0,
    seed=0,
    tries=4,
    ctx=32768,
    as_json=True,
    note="",
    video=None,
):
    last = None
    for attempt in range(tries):
        messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
        try:
            if model.startswith("or:"):
                text = _openrouter(model[3:], messages, images, temperature, seed, as_json, note, video)
            elif model.startswith("claude:"):  # no temperature or seed: current Claude models reject them
                text = _claude(model[7:], messages, images, note)
            elif video:
                raise RuntimeError(f"{model}: a local model cannot take a video file; use an or: Gemini model")
            else:
                text = _ollama(model, messages, images, temperature, seed, ctx, as_json, note)
            return _parse(text, as_json)
        except urllib.error.HTTPError as exc:
            if exc.code in (400, 401, 402, 403, 404):
                raise RuntimeError(f"{model}: refused ({exc.code})") from exc
            last = exc
        except RuntimeError:
            raise
        except Exception as exc:  # noqa: BLE001 - shared GPUs / network: ask again
            last = exc
        time.sleep(3 + attempt * 8)
    raise RuntimeError(f"{model}: no usable reply ({last})")
