#!/usr/bin/env bash
# Usage: bash setup.sh      (Linux / macOS / WSL / Git-Bash)
set -e
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m spacy download xx_ent_wiki_sm     # multilingual NER
python -m spacy download de_core_news_sm
python -m spacy download fi_core_news_sm
[ -f .env ] || cp .env.example .env
echo "Done. Edit .env, then run: python tests/test_access.py"
