# Synthetic Cross-Sheet Duplicate Example Walkthrough

This synthetic example mirrors [`https://datacheck.cc/en/cross-sheet-duplicates`](https://datacheck.cc/en/cross-sheet-duplicates):

- **Reference tab (`Reference data`, `A2:A9`):** `12.3751, 18.6427, 27.9143, 35.2086, 44.7319, 53.0864, 61.4592, 78.3205`
- **Same order reuse (`Same order reuse`, `A2:A9`):** Exact sequence repeated in the same order across tabs.
- **Reordered reuse (`Reordered reuse`, `A2:A9`):** Same 8-value pool reordered (`78.3205` moved to row 2), which standard row-by-row `COUNTIF` or `df.duplicated()` misses.

Run `python3 scripts/quick_exact_check.py samples/synthetic-reference.csv samples/synthetic-reordered.csv` or inspect the interactive evidence report at [DataCheck Cross-Sheet Duplicates](https://datacheck.cc/en/cross-sheet-duplicates).
