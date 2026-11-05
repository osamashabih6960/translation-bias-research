# "Hamara gap" paragraph (draft, edit after literature matrix)
Recent work evaluates multilingual LLM translation for quality and bias, but largely inspects the translated output alone. Translation Tangles (ACL 2026 Findings)
benchmarks 24 X<->English pairs and flags bias in X->EN outputs, yet it treats the English reference as unbiased, applies its detector only in the X->EN direction,
relies on an English-keyword/NER heuristic whose precision against human labels is about 27%, and uses an LLM judge as pseudo-gold (heuristic-judge agreement 48.79%).
It therefore cannot say whether a biased output reflects the source or was introduced, amplified, suppressed or transformed by the model. We study English->X
translation with controlled, matched English sources and measure the change in bias between source and output (BAS, UAIR, APR, BSR, TR), using a
target-language-aware detector validated against blinded human annotation, and test whether translation quality tracks fairness.
