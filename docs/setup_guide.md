# Setup guide (Hinglish)
## Kahan kya chalega
| Kaam | Kahan chalao |
|---|---|
| Code, data, stats, figures, writing | Apna laptop (Python 3.10+) |
| Chhote models (Qwen-3B, Llama-8B, Gemma-9B) | Google Colab (T4/L4) ya Kaggle GPU, 4-bit/8-bit; ya HF Inference |
| Llama-3.1-70B | API (Groq / Together / OpenRouter). Local GPU me 70B ke liye 80GB chahiye |
| LLM judge + embeddings | Gemini API (gemini-2.5-flash, gemini-embedding-001) |
## Steps
1. unzip -> cd project -> bash setup.sh   (Windows: WSL ya Git-Bash)
2. .env bharo: HF_TOKEN, GEMINI_API_KEY, LLM_API_KEY, LLM_BASE_URL, LLM_MODEL_70B
3. HuggingFace pe Gemma aur Llama ka license accept karo (gated models), token banao
4. python tests/test_access.py   (local model bhi test karna ho: --local)
5. git init && git add -A && git commit -m "Day 1 scaffold"
6. Colab ke liye: notebook me  !git clone <tumhari repo>  ->  !pip install -r requirements.txt  -> .env ki jagah userdata secrets use karo
## Rules
- .env kabhi commit mat karo (.gitignore me hai)
- Model checkpoints aur API model names configs/config.yaml me exact likho (Day 2)
- Har translation ka raw output logs me save ho (Day 9 logger)
