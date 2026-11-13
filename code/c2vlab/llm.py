"""One way to ask a model. Every reply is JSON unless as_json=False.

A model name is either an Ollama model on this box (free), e.g. "gemma4:26b", or "or:<openrouter id>", e.g.
"or:google/gemini-3-flash-preview" (paid, written to runs/ledger.jsonl, refused past C2V_CAP_USD).

OpenRouter key: C2V_OPENROUTER_KEY (a key of its own for this study is best), else OPENROUTER_API_KEY, else the
OPENROUTER_API_KEY in the .env file named by C2V_ENV. The key is never printed or written anywhere.
"""

from __future__ import annotations

import base64
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

OLLAMA = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
OPENROUTER = "https://openrouter.ai/api/v1/chat/completions"
LEDGER = Path(os.getenv("C2V_LEDGER", Path(__file__).resolve().parents[1] / "runs" / "ledger.jsonl"))
CAP_USD = float(os.getenv("C2V_CAP_USD", "1.00"))

# Defaults are all local and free. Override any of them with an "or:..." id to use OpenRouter.
PLANNER = os.getenv("C2V_PLANNER", "qwen3.6:latest")  # outlines, quizzes (text only: it crashes with images here)
CODER = os.getenv("C2V_CODER", "qwen3-coder:30b")  # Manim code and its repairs
STUDENT = os.getenv("C2V_STUDENT", "gemma4:26b")  # the unlearned student (forgets properly; qwen2.5vl does not)
JUDGE = os.getenv("C2V_JUDGE", "qwen2.5vl:7b")  # evidence judge, another family than the student


def spent():
    if not LEDGER.exists():
        return 0.0
    return sum(json.loads(line).get("usd", 0.0) for line in LEDGER.read_text().splitlines() if line.strip())


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


def _ollama(model, messages, images, temperature, seed, ctx, as_json):
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
    req = urllib.request.Request(OLLAMA, json.dumps(body).encode(), {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=900))["message"]["content"]


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
            req = urllib.request.Request(OLLAMA, json.dumps(body).encode(), {"Content-Type": "application/json"})
            r = json.load(urllib.request.urlopen(req, timeout=1800))
            used = r.get("prompt_eval_count") or 0
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
            elif video:
                raise RuntimeError(f"{model}: a local model cannot take a video file; use an or: Gemini model")
            else:
                text = _ollama(model, messages, images, temperature, seed, ctx, as_json)
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
