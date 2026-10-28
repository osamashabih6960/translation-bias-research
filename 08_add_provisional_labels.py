
import pandas as pd
from pathlib import Path

input_path = Path("data/processed/pilot_evaluation_10.csv")
output_path = Path("data/processed/pilot_evaluation_labeled.csv")

df = pd.read_csv(input_path, keep_default_na=False)

# Provisional labels: review these before using in research results.
labels = {
    0: ("2", "0", "No major change identified", "Meaning broadly preserved; provisional label."),
    1: ("U", "U", "Possible omission; source is truncated", "Insufficient context; needs manual review."),
    2: ("U", "U", "Single word requires context", "Translation cannot be verified from this word alone."),
    3: ("2", "0", "No obvious change", "Flag of Pakistan broadly preserves the source meaning."),
    4: ("U", "U", "Meaning requires context", "Translation may be plausible, but needs verification."),
    5: ("1", "U", "English translation appears incomplete", "Possible omission; inspect the full source and target."),
    6: ("U", "U", "Proper noun or culturally specific term", "Context is needed to verify the translation."),
    7: ("U", "U", "Insufficient context", "Single word or interjection requires context."),
    8: ("2", "U", "Check the referent of 'he'", "Meaning broadly preserved; gender/reference needs context."),
    9: ("2", "0", "Company name broadly preserved", "HTML entity &amp; represents an ampersand."),
}

for i, row in df.iterrows():
    row_id = int(row["row_id"])
    score, gender, issue, notes = labels[row_id]

    df.at[i, "meaning_score"] = score
    df.at[i, "gender_issue"] = gender
    df.at[i, "additions_or_omissions"] = issue
    df.at[i, "review_notes"] = notes

output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print("Provisional labels saved.")
print("Rows:", len(df))
print("Output:", output_path)
print("\nReview these labels before treating them as final annotations.")
