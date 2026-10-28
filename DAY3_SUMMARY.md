
# Day 3 — Dataset Quality and Cleaning

## Dataset
- Name: BanglaNMT
- Language pair: Bengali (bn) → English (en)
- Split: Training
- Pilot sample size: 1,000 rows

## Completed Tasks
1. Inspected dataset structure and columns.
2. Checked missing and duplicate translation pairs.
3. Cleaned the 1,000-row pilot sample.
4. Verified the cleaned dataset.
5. Screened translation pairs for potential quality issues.

## Cleaning Results
- Original rows: 1,000
- Cleaned rows: 1,000
- Rows removed: 0
- Empty Bengali values after cleaning: 0
- Empty English values after cleaning: 0

## Quality Screening Results
- Rows checked: 1,000
- Potentially suspicious rows: 15
- Flagged percentage: 1.5%
- Report: data/processed/translation_quality_flags.csv

## Important Limitation
The flagged examples have not yet been manually verified.
A flag does not establish that a translation is incorrect.
Only the first 1,000 training rows were processed.

## Output Files
- data/processed/banglanmt_sample_1000
- data/processed/translation_quality_flags.csv
- DATASET_NOTES.md
