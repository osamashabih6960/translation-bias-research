
from datasets import load_from_disk
from pathlib import Path
import csv

INPUT_PATH = "data/processed/banglanmt_sample_1000"
OUTPUT_PATH = Path("data/processed/translation_quality_flags.csv")

print("Loading cleaned BanglaNMT sample...")
dataset = load_from_disk(INPUT_PATH)

flagged_rows = []

for index, row in enumerate(dataset):
    bn = row["bn"].strip()
    en = row["en"].strip()

    bn_words = len(bn.split())
    en_words = len(en.split())

    reasons = []

    # Flag unusually short or long translations
    if bn_words >= 8 and en_words <= 2:
        reasons.append("Long Bengali source, very short English translation")

    if len(bn) > 500 or len(en) > 500:
        reasons.append("Very long text")

    # Flag possible truncation
    if bn.endswith("...") or en.endswith("..."):
        reasons.append("Text may be truncated")

    # Flag extreme word-count differences
    if bn_words >= 10 and en_words > 0:
        ratio = en_words / bn_words
        if ratio < 0.2 or ratio > 5:
            reasons.append("Extreme word-count ratio")

    if reasons:
        flagged_rows.append({
            "row_id": index,
            "bengali_words": bn_words,
            "english_words": en_words,
            "reasons": "; ".join(reasons),
            "bengali": bn,
            "english": en,
        })

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT_PATH.open("w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "row_id",
            "bengali_words",
            "english_words",
            "reasons",
            "bengali",
            "english",
        ],
    )
    writer.writeheader()
    writer.writerows(flagged_rows)

print("\nQuality screening completed!")
print("Total rows checked:", len(dataset))
print("Potentially suspicious rows:", len(flagged_rows))
print("Saved report:", OUTPUT_PATH)

print("\nFirst 5 flagged examples:")
for row in flagged_rows[:5]:
    print(f"\nRow ID: {row['row_id']}")
    print("Reason:", row["reasons"])
    print("Bengali:", row["bengali"][:200])
    print("English:", row["english"][:200])
