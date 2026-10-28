
import pandas as pd
from pathlib import Path

path = Path("data/processed/pilot_evaluation_labeled.csv")
df = pd.read_csv(path, keep_default_na=False)

print("Pilot label verification")
print("------------------------")
print("Total rows:", len(df))
print("Meaning scores:")
print(df["meaning_score"].value_counts().to_string())

print("\nGender issue labels:")
print(df["gender_issue"].value_counts().to_string())

print("\nMissing review notes:", (df["review_notes"].str.strip() == "").sum())
print("Missing issue descriptions:",
      (df["additions_or_omissions"].str.strip() == "").sum())

print("\nAll labels:")
print(
    df[
        ["row_id", "meaning_score", "gender_issue",
         "additions_or_omissions", "review_notes"]
    ].to_string(index=False)
)
