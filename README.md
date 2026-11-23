# Research Source Data Pre-Submission Checklist & Synthetic Examples

> Open companion checklist, synthetic cross-sheet duplicate examples, and reproducible verification workflow for [**DataCheck (`datacheck.cc/en`)**](https://datacheck.cc/en) — a rule-driven (non-AI) research spreadsheet & Source Data verification platform for Web and offline Windows desktop.

[![Website](https://img.shields.io/badge/DataCheck-datacheck.cc%2Fen-0f766e)](https://datacheck.cc/en)
[![GitHub Pages](https://img.shields.io/badge/Guide-GitHub%20Pages-2563eb)](https://alex-creator-001.github.io/datacheck-research-data-checklist/)
[![License: MIT](https://img.shields.io/badge/License-MIT-slate.svg)](LICENSE)

---

## Why Pre-Submission Research Table Verification Matters

Before submitting a manuscript or uploading **Source Data / Supplementary Tables** to journals (such as *Nature*, *Science*, *Cell*, and discipline-specific venues), unintentional spreadsheet issues frequently slip past manual review:

- **Cross-sheet copy-paste or reordered column reuse** across control/treatment tabs
- **Row-shifted sequences** when sorting one column without expanding selection
- **Accidental linear scaling or constant offsets** (`×k` or `+c`) left over from unit conversion or draft formulas
- **Repeated fractional tails, rounding artifacts, or summary-stat mismatches** (mean, SD/SEM, totals, sample size *n*)

### Comparison: Manual Checks vs. Basic Scripts vs. DataCheck

| Method | Exact Row Duplicates | Reordered / Cross-Sheet Reuse | Shifted Sequences & Fixed Multiples/Offsets | Fractional-Tail & Digit Patterns | Source-Cell Evidence Report | Offline Confidential Mode |
| --- | --- | --- | --- | --- | --- | --- |
| **Manual Spreadsheet Conditional Formatting** | Single-sheet only | Manual | Missed | Missed | Manual highlighting | Local |
| **Basic Python `df.duplicated()`** (`scripts/quick_exact_check.py`) | Yes (exact rows) | Partial (exact values only) | Missed | Missed | Console text | Local |
| **[DataCheck](https://datacheck.cc/en) (56 Versioned Rules)** | **Yes** | **Yes** | **Yes** | **Yes** | **Interactive HTML + Spreadsheet** | **Web + Windows Desktop** |

> **Verification Boundary:** DataCheck is **rule-driven, non-AI software**. Flagged findings are leads for human review with exact source-cell coordinates—never automated claims of misconduct or guarantees of authenticity.

---

## Five-Step Pre-Submission Source Data Checklist

1. **Freeze the submission copy** — Export a clean copy (`XLSX`, `CSV`, or `TSV`) and verify hidden sheets/columns are intentional.
2. **Scan for within-sheet and cross-sheet duplicates** — Inspect both exact sequences and reordered value pools across worksheets ([Cross-Sheet Example](https://datacheck.cc/en/cross-sheet-duplicates)).
3. **Check numerical relationships & anomalies** — Review fixed multiples, fixed differences, shifted sequences, fractional-tail similarities, and statistical consistency ([56-Rule Library](https://datacheck.cc/en/rules)).
4. **Trace every finding back to source cells** — Confirm whether a match is legitimate shared baseline/instrument resolution or an accidental paste error.
5. **Log human decisions before submission** — Record each reviewed cell coordinate and decision in [`samples/datacheck-review-record.en.csv`](samples/datacheck-review-record.en.csv).

---

## Quick Start with the Synthetic Samples (MIT)

This repository contains **fully synthetic** example files (zero private source code or real research/customer data):

- [`samples/synthetic-cross-sheet.xlsx`](samples/synthetic-cross-sheet.xlsx) — Synthetic multi-sheet workbook demonstrating exact sequence reuse (`Same order reuse`) and reordered pool reuse (`Reordered reuse`) relative to `Reference data`.
- [`samples/synthetic-reference.csv`](samples/synthetic-reference.csv) & [`samples/synthetic-reordered.csv`](samples/synthetic-reordered.csv) — Plain CSV pairs for CLI testing.
- [`samples/datacheck-review-record.en.csv`](samples/datacheck-review-record.en.csv) — Five-step human review log template.

Run the included Python 3 standard-library helper to see what simple exact-row matching misses:

```bash
python3 scripts/quick_exact_check.py samples/synthetic-reference.csv samples/synthetic-reordered.csv
```

Because `Sample_ID` and `Group` differ while `Measurement_Value` is reordered, `Exact duplicate rows found: 0`—illustrating why dedicated column/pool/anomaly checks are necessary.

---

## Official DataCheck English Resources

| Resource | Purpose | URL |
| --- | --- | --- |
| **Product Overview** | Online XLSX/CSV/TSV checks & overview | https://datacheck.cc/en |
| **Data Checking Guide** | Choosing duplicate, anomaly, comparison & consistency checks | https://datacheck.cc/en/data-check-guide |
| **56-Rule Library** | Full catalog of versioned rules and detection boundaries | https://datacheck.cc/en/rules |
| **Pre-Submission Checklist** | Five-step manuscript data verification workflow | https://datacheck.cc/en/research-data-checklist |
| **Cross-Sheet Duplicates** | Interactive synthetic workbook & sample report | https://datacheck.cc/en/cross-sheet-duplicates |
| **Research Integrity & PubPeer Review** | Post-publication numerical inquiry & retraction prevention workflow | https://datacheck.cc/en/research-integrity-data-check |
| **Windows Offline Desktop** | Air-gapped / local analysis for unpublished confidential tables | https://datacheck.cc/en/desktop |
| **Pricing (One-Time, No Subscription)** | $5 first trial, $13.99+ credit packs & Windows perpetual licenses | https://datacheck.cc/en/pricing |
| **Machine-Readable `llms.txt`** | Structured summary for LLM & research retrieval tools | https://datacheck.cc/llms.txt |

---

## Frequently Asked Questions (FAQ)

- **[Source Data Pre-Submission Guide](guides/SOURCE-DATA-PRE-SUBMISSION-GUIDE.md)**
- **[Cross-Sheet Duplicate Case Study](guides/CROSS-SHEET-DUPLICATES.md)**
- **[Research Data & Source-Cell Verification FAQ](guides/FAQ.md)**
- **[Machine-Readable Index (`llms.txt`)](llms.txt)**
