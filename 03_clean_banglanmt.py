
from datasets import load_from_disk, Dataset
from pathlib import Path

RAW_PATH = Path("data/raw/banglanmt")
OUTPUT_PATH = Path("data/processed/banglanmt_sample_1000")

print("Loading BanglaNMT training data...")
dataset = load_from_disk(str(RAW_PATH))["train"]

# Take a sample of 1,000 rows
sample = dataset.select(range(min(1000, len(dataset))))

clean_rows = []
seen_pairs = set()

for row in sample:
    bn = row.get("bn")
    en = row.get("en")

    # Remove missing or empty translations
    if not isinstance(bn, str) or not bn.strip():
        continue
    if not isinstance(en, str) or not en.strip():
        continue

    bn = bn.strip()
    en = en.strip()
    pair = (bn, en)

    # Remove duplicate translation pairs
    if pair in seen_pairs:
        continue

    seen_pairs.add(pair)
    clean_rows.append({"bn": bn, "en": en})

clean_dataset = Dataset.from_list(clean_rows)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
clean_dataset.save_to_disk(str(OUTPUT_PATH))

print("\nCleaning completed!")
print(f"Original sample rows: {len(sample)}")
print(f"Cleaned rows: {len(clean_dataset)}")
print(f"Rows removed: {len(sample) - len(clean_dataset)}")
print(f"Saved to: {OUTPUT_PATH}")
print("\nExample:")
print(clean_dataset[0] if len(clean_dataset) else "No valid rows found.")
