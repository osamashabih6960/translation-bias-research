from datasets import load_dataset
import os

print("=" * 60)
print("LOADING LIT-CORPUS / KAZLIT-PARALLEL")
print("=" * 60)

# Load dataset
dataset = load_dataset(
    "SagiAbd/KazLit-Parallel"
)

print("\n✅ Dataset loaded successfully!")
print(dataset)

for split in dataset:
    print(f"{split}: {len(dataset[split]):,} rows")

print("\nColumns:")
print(dataset["train"].column_names)

print("\nFirst example:")
print(dataset["train"][0])


# ============================================================
# SAVE DATASET TO PROJECT
# ============================================================

save_path = "data/raw/lit_corpus"

os.makedirs(save_path, exist_ok=True)

print("\nSaving Lit-Corpus to project...")

dataset.save_to_disk(save_path)

print("\n" + "=" * 60)
print("✅ LIT-CORPUS SAVED SUCCESSFULLY")
print("=" * 60)
print("Location:", save_path)