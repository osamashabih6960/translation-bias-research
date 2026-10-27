from datasets import load_from_disk
import pandas as pd
import os

print("=" * 70)
print("DAY 1 — DATASET INSPECTION")
print("=" * 70)


# ============================================================
# 1. WMT18 DE-EN
# ============================================================

print("\n" + "=" * 70)
print("1. WMT18 DE-EN")
print("=" * 70)

wmt18 = load_from_disk("data/raw/wmt18_de_en")

print(wmt18)

print("\nColumns:")
print(wmt18["train"].column_names)

print("\nTrain size:", f"{len(wmt18['train']):,}")
print("Validation size:", f"{len(wmt18['validation']):,}")
print("Test size:", f"{len(wmt18['test']):,}")

print("\nExample:")
print(wmt18["train"][0])


# ============================================================
# 2. WMT19 DE-EN
# ============================================================

print("\n" + "=" * 70)
print("2. WMT19 DE-EN")
print("=" * 70)

wmt19 = load_from_disk("data/raw/wmt19_de_en")

print(wmt19)

print("\nColumns:")
print(wmt19["train"].column_names)

print("\nTrain size:", f"{len(wmt19['train']):,}")
print("Validation size:", f"{len(wmt19['validation']):,}")

print("\nExample:")
print(wmt19["train"][0])


# ============================================================
# 3. BANGLANMT
# ============================================================

print("\n" + "=" * 70)
print("3. BANGLANMT")
print("=" * 70)

banglanmt = load_from_disk("data/raw/banglanmt")

print(banglanmt)

print("\nColumns:")
print(banglanmt["train"].column_names)

print("\nTrain size:", f"{len(banglanmt['train']):,}")
print("Validation size:", f"{len(banglanmt['validation']):,}")
print("Test size:", f"{len(banglanmt['test']):,}")

print("\nExample:")
print(banglanmt["train"][0])


# ============================================================
# 4. ELRC-MEDICAL-V2
# ============================================================

print("\n" + "=" * 70)
print("4. ELRC-MEDICAL-V2 EN-ES")
print("=" * 70)

elrc_path = "data/raw/elrc_medical_v2_en_es/en-es.csv"

elrc = pd.read_csv(elrc_path)

print("\nShape:", elrc.shape)

print("\nColumns:")
print(elrc.columns.tolist())

print("\nMissing values:")
print(elrc.isnull().sum())

print("\nExample:")
print(elrc.head(1).to_dict("records")[0])


# ============================================================
# 5. LIT-CORPUS / KAZLIT-PARALLEL
# ============================================================

print("\n" + "=" * 70)
print("5. LIT-CORPUS / KAZLIT-PARALLEL")
print("=" * 70)

lit = load_from_disk("data/raw/lit_corpus")

print(lit)

print("\nColumns:")
print(lit["train"].column_names)

print("\nTrain size:", f"{len(lit['train']):,}")

print("\nLanguage pairs:")
print(
    pd.Series(lit["train"]["Language_pair"])
    .value_counts()
)

print("\nExample:")
print(lit["train"][0])


# ============================================================
# 6. MULTIEURLEX
# ============================================================

print("\n" + "=" * 70)
print("6. MULTIEURLEX")
print("=" * 70)

multi = load_from_disk("data/raw/multieurlex")

print(multi)

print("\nColumns:")
print(multi["train"].column_names)

print("\nTrain size:", f"{len(multi['train']):,}")
print("Validation size:", f"{len(multi['validation']):,}")
print("Test size:", f"{len(multi['test']):,}")

print("\nExample:")
print(multi["train"][0])


print("\n" + "=" * 70)
print("✅ DAY 1 DATASET INSPECTION COMPLETED")
print("=" * 70)