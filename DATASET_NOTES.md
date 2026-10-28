
# Dataset Inspection and Cleaning Notes

## 1. Dataset
- Name: BanglaNMT
- Language pair: Bengali (bn) to English (en)
- Dataset source: csebuetnlp/BanglaNMT
- Raw dataset path: data/raw/banglanmt

## 2. Pilot Sample
- Split: train
- Rows inspected: 1,000
- Bengali column: bn
- English column: en

## 3. Cleaning Procedure
- Removed missing or empty Bengali translations.
- Removed missing or empty English translations.
- Removed exact duplicate Bengali-English pairs.
- Trimmed leading and trailing whitespace.

## 4. Cleaning Results
- Original sample rows: 1,000
- Cleaned rows: 1,000
- Rows removed: 0
- Empty Bengali values after cleaning: 0
- Empty English values after cleaning: 0

## 5. Output
- Processed dataset: data/processed/banglanmt_sample_1000

## 6. Limitations
- Only the first 1,000 training rows were cleaned.
- Results cannot be generalized to the entire dataset.
- Translation accuracy, semantic equivalence, and bias have not yet been evaluated.
