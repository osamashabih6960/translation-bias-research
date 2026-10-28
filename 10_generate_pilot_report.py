
import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/processed/pilot_evaluation_labeled.csv")
OUTPUT_PATH = Path("data/processed/day4_pilot_report.txt")

df = pd.read_csv(INPUT_PATH, keep_default_na=False)

meaning = df["meaning_score"].astype(str).str.strip()
gender = df["gender_issue"].astype(str).str.strip()

lines = [
    "DAY 4 — PILOT EVALUATION REPORT",
    "=" * 32,
    "",
    "Dataset: BanglaNMT",
    "Language pair: Bengali -> English",
    "Pilot sample size: 10",
    "Annotation status: PROVISIONAL; not independently validated",
    "",
    "Meaning score counts:",
]

for label, count in meaning.value_counts().items():
    lines.append(f"  {label}: {count}")

lines.extend(["", "Gender issue label counts:"])

for label, count in gender.value_counts().items():
    lines.append(f"  {label}: {count}")

lines.extend([
    "",
    "Limitations:",
    "- This is a 10-pair pilot sample.",
    "- Labels are provisional and require human validation.",
    "- U means insufficient context to make a reliable decision.",
    "- These counts are not a confirmed translation-bias rate.",
    "- No generalization to the full dataset is justified.",
])

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")

print("\n".join(lines))
print(f"\nReport saved to: {OUTPUT_PATH}")
