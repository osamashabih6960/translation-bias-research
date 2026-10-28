
from datasets import load_from_disk
import pandas as pd

INPUT_PATH = "data/processed/banglanmt_sample_1000"
OUTPUT_PATH = "data/processed/pilot_evaluation_10.csv"

dataset = load_from_disk(INPUT_PATH)

rows = []

for i in range(min(10, len(dataset))):
    rows.append({
        "row_id": i,
        "bengali_source": dataset[i]["bn"],
        "english_translation": dataset[i]["en"],
        "meaning_score": "",
        "gender_issue": "",
        "additions_or_omissions": "",
        "review_notes": "",
    })

df = pd.DataFrame(rows)
df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

print("Pilot evaluation file created!")
print("Rows:", len(df))
print("Saved to:", OUTPUT_PATH)
print("\nFirst 3 examples:")
print(df[["row_id", "bengali_source", "english_translation"]].head(3).to_string(index=False))
