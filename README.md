# A placebo test for narrative and time-only features in credit-risk models

Code that accompanies the paper *"Explainable Machine Learning for Basel and IFRS 9 Credit Risk: A Placebo-Controlled Test of Narrative Features"* (Muhammad Nawaz, Insytosys, 2026; link to be added once the paper is online).

## The idea in plain words
A feature that only changes over time, such as the tone of central bank statements, tells a model *when* a loan was made. A model can use that as a clock for the lending period. So a gain in accuracy (AUC) or a high rank in a feature-importance report does not prove the feature carries real information about borrowers. The notebook shows this and runs a simple placebo test: compare the real feature with random fake series, control for the period of lending, and test at the level of each statement.

## What the notebook does
| Part | Content |
|---|---|
| 1–2 | Baseline default model on Give Me Some Credit (logistic regression, gradient boosting, WOE/IV, calibration, SHAP) |
| 3 | Does tone help? Real tone versus shuffled-tone placebos, on Lending Club (with FOMC) and Bondora (with ECB) |
| 4 | The proper test: origination-period controls (year, half-year, quarter) and statement-level permutation tests |
| 5 | Can a feature-importance report tell a real driver from a clock? |
| 6 | How often does the standard check pass a series that carries no information? |
| Appendix | How the raw statements and loan file were downloaded (not needed to reproduce results) |

## How to run
1. Install Python 3.10+ and the packages: `pip install -r requirements.txt`
2. Put the loan files in the `data/` folder (see `data/README.md`). The tone scores are already there.
3. Open `PD_Narrative_Features_Notebook.ipynb` in Jupyter and run the cells **one at a time, in order**. Do not run the Appendix cells.
4. The *Settings* cell near the top sets the run size. The values in brackets are the ones used in the paper. The default for Part 6 (`PASS_K = 3`) is a quick version; set `PASS_K = 60` for the paper version (this takes many hours).

The Bondora file is large. The notebook reads it in pieces to save memory. Reading the 306,034 usable loans and running the Bondora tests in Parts 3 and 4 took about 15 minutes in my test; a laptop may be slower.

## Notes and limits
- The tone index uses a hand-built word list in the style of Loughran and McDonald (`lm_lexicon.py`), not the official published list. The notebook can use the official list instead (`SCORING = "official"`).
- This is a pilot on public peer-to-peer loan data, not on bank supervisory data. The paper explains what it can and cannot show.
- Part 5 and 6 outputs are not saved in this copy; run them to reproduce the paper's tables.
- Part of this code was written with the help of an AI assistant (Claude, Anthropic); the author reviewed it. See the paper's AI disclosure.

## Licence
MIT (see `LICENSE`). Data files from third parties keep their own licences.
