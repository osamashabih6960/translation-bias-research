# Hypotheses (FROZEN before experiments)
Freeze date: 2026-11-04   |   Git tag: hypotheses-frozen   |   Do not edit after tagging; add amendments in a separate dated section.

Metrics: BAS = B(output) - B(source); UAIR = unsupported attributes added / neutral-source cases; APR = preserved explicit attributes / explicit attributes;
BSR = biased sources whose output bias decreased / biased sources; TR = category changes / biased outputs; QBG = quality vs bias relation.

| ID | RQ | Hypothesis | Measure | Planned test | Support if |
|---|---|---|---|---|---|
| H1 | RQ1 Preservation | APR for explicit gender/religion attributes is higher for high-resource target languages than low-resource ones | APR by language | mixed-effects, bootstrap CI | High-resource APR > low-resource APR, CI excludes 0 |
| H2 | RQ2 Introduction | UAIR (gender) is higher in languages with obligatory grammatical gender than in gender-neutral-pronoun languages | UAIR by language group | paired / mixed-effects | gendered-language UAIR > neutral, CI excludes 0 |
| H3 | RQ3 Amplification | BAS > 0 for sources with stereotype-aligned attributes | mean BAS by condition | bootstrap CI | lower CI bound > 0 |
| H4 | RQ4 Suppression | Larger models show higher BSR than smaller models | BSR by model size | mixed-effects | positive size coefficient |
| H5 | RQ5 Transformation | Religious-source bias transforms into cultural-category bias more often than other transitions | TR transition matrix | chi-square + effect size | religion->cultural is the largest off-diagonal share |
| H6 | RQ6 Language | Low-resource target languages have higher UAIR than high-resource ones | UAIR by resource level | mixed-effects | low > high, CI excludes 0 |
| H7 | RQ7 Domain | Detector agreement with humans (F1) is lowest in the literature domain | F1 by domain | bootstrap CI | literature F1 < other domains |
| H8 | RQ8 Model | Larger models have lower bias counts, but not zero | UAIR/BAS by model | mixed-effects | negative size effect, mean > 0 |
| H9 | RQ9 Quality/fairness | Translation quality (BLEU/COMET) correlates only weakly with bias score | Spearman rho | Spearman + CI | abs(rho) < 0.3 |

Multiple-comparison correction: Benjamini-Hochberg. Effect sizes reported with every p-value.

## Operational definitions (add BEFORE tagging hypotheses-frozen; confirm with native speakers on Day 2)
| Term | Definition |
|---|---|
| High-resource target | German |
| Mid-resource target | Arabic, Turkish, Finnish, Hindi |
| Low-resource target | Bengali, Tamil, Kazakh |
| Obligatory grammatical gender (H2) | Hindi, Arabic, German (Tamil: he/she pronouns exist, treat as gendered; confirm) |
| Gender-neutral third-person pronoun (H2) | Turkish, Finnish, Bengali, Kazakh (confirm) |
| Small / large model (H4, H8) | Small: Qwen-2.5-3B, Llama-3.1-8B, Gemma-2-9B. Large: Llama-3.1-70B |
| Bias present | As defined in annotation_guidelines (Day 2) |
| Unsupported attribute | A gender/religion/ethnicity/status attribute in the output with no support in the English source |
| "approx. 0" for BAS | abs(BAS) < epsilon, epsilon set on dev set |
NOTE (Day 1 literature finding): H2 overlaps with GENDEROUS and Translate With Care; treat it as a replication-style hypothesis, not the main novelty.
