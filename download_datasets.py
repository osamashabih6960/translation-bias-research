from huggingface_hub import hf_hub_download
import pandas as pd
import os

print("=" * 60)
print("DOWNLOADING ELRC-MEDICAL-V2 — EN-ES")
print("=" * 60)

repo_id = "qanastek/ELRC-Medical-V2"
filename = "csv/en-es.csv"

# Download exact CSV from Hugging Face
file_path = hf_hub_download(
    repo_id=repo_id,
    filename=filename,
    repo_type="dataset"
)

print("\n✅ CSV downloaded")
print("Cache location:", file_path)

# Read CSV
df = pd.read_csv(file_path)

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

# Save inside our project
save_dir = "data/raw/elrc_medical_v2_en_es"
os.makedirs(save_dir, exist_ok=True)

save_path = os.path.join(save_dir, "en-es.csv")

df.to_csv(save_path, index=False)

print("\n" + "=" * 60)
print("✅ ELRC-MEDICAL-V2 EN-ES SAVED SUCCESSFULLY")
print("=" * 60)
print("Location:", save_path)
print("Rows:", len(df))
print("Columns:", df.columns.tolist())