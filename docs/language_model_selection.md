# Language and model selection (Step 3, Day 2) - DRAFT, confirm with native speakers/annotators

## Languages (8)
| Lang | Family | Script | Grammatical gender | 3rd-person pronoun | Resource level (study) | Why included |
|---|---|---|---|---|---|---|
| German (de) | Indo-European, Germanic | Latin | 3 genders | gendered (er/sie/es) | High | High-resource control; paper pair; strong gendered-noun test (Arzt/Ärztin) |
| Hindi (hi) | Indo-European, Indo-Aryan | Devanagari | masculine/feminine (verbs, adjectives, nouns) | vah is gender-neutral | Mid | Indian-language focus; gender shows up in verb agreement, so pronoun alone cannot reveal it |
| Bengali (bn) | Indo-European, Indo-Aryan | Bengali | none | gender-neutral (se) | Low (paper: low-resource) | Paper pair; gender-neutral target: tests introduction through lexical choice |
| Tamil (ta) | Dravidian | Tamil | gender marking on rational beings | gendered (avan/aval) | Low-mid | Different family from Indo-Aryan; gender in verb endings (CONFIRM with annotator) |
| Arabic (ar) | Afro-Asiatic, Semitic | Arabic (RTL) | masculine/feminine on verbs, pronouns, adjectives | gendered | Mid | Gender plus religion-sensitive vocabulary; RTL script |
| Turkish (tr) | Turkic | Latin | none | gender-neutral (o) | Mid (paper pair) | Genderless target; strong test of unsupported gender introduction |
| Finnish (fi) | Uralic | Latin | none | gender-neutral (han) | Mid (paper: medium-resource) | Different family; genderless; paper pair |
| Kazakh (kk) | Turkic | Cyrillic (check current script use) | none | gender-neutral | Low (paper: low-resource) | Low-resource Central Asian pair from the paper |

Selection criteria (to state in the paper): resource level, language family, grammatical gender system, script, geography/cultural context, model availability, annotator availability.
Annotator rule: at least 4-5 of these 8 must be covered by your annotators. Drop or swap languages that no annotator can read (candidates to drop first: Kazakh, Tamil).

## Models (4)
| Role | Model | Where | Exact ID to record |
|---|---|---|---|
| Small | Qwen2.5-3B-Instruct | Colab/Kaggle or local GPU | Qwen/Qwen2.5-3B-Instruct |
| Small-mid | Llama-3.1-8B-Instruct | Colab/Kaggle | meta-llama/Llama-3.1-8B-Instruct |
| Mid | Gemma-2-9B-it | Colab/Kaggle (4-bit) | google/gemma-2-9b-it |
| Large | Llama-3.3-70B (Groq) | API | llama-3.3-70b-versatile (record date + provider) |
Notes: the paper evaluated Llama-3.1-70B and others; using Llama-3.3-70B via API is a documented deviation (mention in Limitations). API-served models can change: log the date and provider for every run.
Judge: gemini-2.5-flash (as in the paper). Embeddings: gemini-embedding-001 (paper) and LaBSE (open alternative).
