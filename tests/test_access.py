"""Day 1 access test. Run: python tests/test_access.py
Checks (1) Gemini judge call, (2) Gemini embedding, (3) 70B translation via OpenAI-compatible API,
(4) optional local HF small model. Each check is independent; failures are printed, not fatal."""
import os, sys
from dotenv import load_dotenv
load_dotenv()
SENT = "The doctor spoke to the patient."

def check(name, fn):
    try:
        out = fn(); print(f"[OK]   {name}: {str(out)[:120]!r}")
    except Exception as e:
        print(f"[FAIL] {name}: {type(e).__name__}: {e}")

def gemini_judge():
    from google import genai
    c = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    r = c.models.generate_content(model="gemini-2.5-flash",
        contents='Return JSON {"bias_detected": bool} for: reference "The doctor spoke." translation "The male doctor spoke."')
    return r.text

def gemini_embed():
    from google import genai
    c = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    r = c.models.embed_content(model="gemini-embedding-001", contents=SENT)
    return f"embedding dim = {len(r.embeddings[0].values)}"

def api_translate():
    from openai import OpenAI
    c = OpenAI(api_key=os.environ["LLM_API_KEY"], base_url=os.environ["LLM_BASE_URL"])
    r = c.chat.completions.create(model=os.environ["LLM_MODEL_70B"], temperature=0,
        messages=[{"role": "user", "content": f"Translate the following text into Hindi. Do not add information.\n\n{SENT}"}])
    return r.choices[0].message.content

def local_small():
    from transformers import pipeline
    p = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct", device_map="auto")
    return p(f"Translate to German: {SENT}", max_new_tokens=40)[0]["generated_text"]

check("Gemini judge", gemini_judge)
check("Gemini embedding", gemini_embed)
check("70B API translation", api_translate)
if "--local" in sys.argv: check("Local HF small model", local_small)
