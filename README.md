# Data folder

Two small files are included here (the tone scores of the central bank statements):

- `ecb_sentiment_scores_2009_2026.csv` – net negative tone of each European Central Bank press-conference statement
- `fomc_sentiment_scores.csv` – the same for Federal Open Market Committee statements

The loan files are **not** included (large, and owned by their publishers). Download them yourself and put them in this folder with exactly these names:

| File name | What it is | Where to get it |
|---|---|---|
| `cs-training.csv` | Give Me Some Credit (Part 1 and 2 only) | Kaggle, competition "Give Me Some Credit" |
| `loan.csv` | Lending Club loans, 2007 onwards (the notebook keeps loans issued up to 2015) | Kaggle, dataset "Lending Club loan data" (any copy that has `loan_status`, `issue_d`, `grade`, `int_rate` etc.) |
| `LoanData.csv` | Bondora loans | Kaggle, dataset `marcobeyer/bondora-loans` (the notebook's last cell can download it) |

Check the licence terms of each source before reusing the data.
