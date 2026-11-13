"""One Claude request, run in its own environment (.venv-claude, which holds only the anthropic SDK) so the main
environment's packages are never touched. bench/claude_fix.py starts it as a subprocess.

    stdin : {"system": str, "text": str, "images": [png or jpg paths], "schema": json schema, "effort": "high",
             "model": optional, default claude-opus-5-5, "max_tokens": optional}
    stdout: {"text": str, "model": str, "stop_reason": str, "usage": {...}, "request_id": str}

"model" in the reply is the model that served the request: with server-side fallbacks it can differ from the one asked
for. Claude Haiku 5.5 has no server-side fallback, so none is requested for it.

The API key comes from the environment of this process only (the caller reads it from a .env file); it is never
printed or logged.
"""

from __future__ import annotations

import base64
import json
import sys

import anthropic

MODEL = "claude-opus-5-5"


def main():
    req = json.load(sys.stdin)
    content = []
    for path in req.get("images") or []:
        with open(path, "rb") as f:
            data = base64.standard_b64encode(f.read()).decode()
        media = "image/jpeg" if path.lower().endswith((".jpg", ".jpeg")) else "image/png"
        content.append({"type": "image", "source": {"type": "base64", "media_type": media, "data": data}})
    content.append({"type": "text", "text": req["text"]})
    client = anthropic.Anthropic(max_retries=4)
    model = req.get("model", MODEL)
    extra = {}
    if not model.startswith("claude-haiku"):
        # a declined request is re-run on a fallback model; response.model says which served
        extra = {"betas": ["server-side-fallback-2026-07-01"], "fallbacks": "default"}
    output_config = {"effort": req.get("effort", "high")}
    if req.get("schema"):
        output_config["format"] = {"type": "json_schema", "schema": req["schema"]}
    response = client.beta.messages.create(
        model=model,
        max_tokens=req.get("max_tokens", 16000),
        system=req["system"],
        output_config=output_config,
        messages=[{"role": "user", "content": content}],
        **extra,
    )
    text = next((b.text for b in response.content if b.type == "text"), "")
    out = {
        "text": text,
        "model": response.model,
        "stop_reason": response.stop_reason,
        "usage": {"input_tokens": response.usage.input_tokens, "output_tokens": response.usage.output_tokens},
        "request_id": response._request_id,
    }
    json.dump(out, sys.stdout)


if __name__ == "__main__":
    main()
