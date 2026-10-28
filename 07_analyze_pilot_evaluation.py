
import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/processed/pilot_evaluation_10.csv")
OUTPUT_PATH = Path("data/processed/pilot_evaluation_summary.csv")

df = pd.read_csv(INPUT_PATH, keep_default_na=False)

# Calculate word counts for each language
df["bengali_word_count"] = df["bengali_source"].apply(
    lambda text: len(str(text).split())
)
df["english_word_count"] = df["english_translation"].apply(
    lambda text: len(str(text).split())
)

# Check whether manual review has been filled in
df["review_completed"] = df.apply(
    lambda row: bool(
        row["meaning_score"]
        and row["gender_issue"]
        and row["review_notes"]
    ),
    axis=1,
)

df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

print("Pilot analysis completed!")
print("Total pairs:", len(df))
print("Manual reviews completed:", int(df["review_completed"].sum()))
print("Manual reviews pending:", int((~df["review_completed"]).sum()))
print("Summary saved to:", OUTPUT_PATH)

print("\nWord-count overview:")
print(
    df[
        ["row_id", "bengali_word_count", "english_word_count"]
    ].to_string(index=False)
)
