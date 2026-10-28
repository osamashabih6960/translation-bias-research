
# Day 4 — Translation Bias Research Plan

## 1. Research Question

To what extent do Bengali-to-English machine translations introduce unsupported gender information or alter the meaning of the source text?

## 2. Research Objectives

1. Identify possible meaning changes in Bengali-to-English translations.
2. Investigate whether translations introduce gender information that is not supported by the source.
3. Record suspicious examples for manual review.
4. Develop a reproducible evaluation procedure.

## 3. Research Hypotheses

### H1 — Meaning Preservation
Some Bengali-to-English translation pairs may contain meaning changes or omissions.

### H2 — Unsupported Gender Information
Some translations may introduce gender information that is not explicitly supported by the source text or its context.

### H3 — Quality Flags
Automatic screening rules can identify candidate examples that require further review, but a flag alone does not prove bias.

## 4. Dataset

- Dataset: BanglaNMT
- Language pair: Bengali (bn) → English (en)
- Split: Training
- Initial cleaned sample: 1,000 pairs
- Cleaned dataset path: data/processed/banglanmt_sample_1000

## 5. Planned Evaluation

For each selected pair, examine:

- Meaning preservation
- Possible omissions or additions
- Unsupported gender information
- Context needed to interpret the translation
- Manual review decision

## 6. Evidence and Reporting

Report the number of pairs reviewed, the number of candidate issues, and the number of issues confirmed through manual review.

Do not label a translation as biased based only on sentence length, word-count differences, or automatic flags.

## 7. Limitations

- The initial sample contains only 1,000 training pairs.
- The dataset may not represent all Bengali text or translation systems.
- Source sentences may lack enough context to determine intended meaning or gender.
- Human review is needed to verify candidate issues.
- Findings from this sample cannot automatically be generalized to all translation systems.
