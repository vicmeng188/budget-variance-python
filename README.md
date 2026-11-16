\# Budget vs Actual Variance Analysis (Python)



A small Python script that combines six monthly Budget vs Actual files, summarises spend by department, and checks the result against verified totals.



\## What it does



1\. Reads six monthly CSV files from the `data` folder.

2\. Appends them into one table (72 rows).

3\. Groups by department and sums Budget and Actual.

4\. Calculates Variance (Actual minus Budget).

5\. Checks that the overall totals match the verified figures, and stops with an error if they do not.



\## Data



Synthetic data covering 3 departments, 4 cost categories and 6 months (January to June 2026).



\## Reconciliation check



The script asserts that Total Budget is 1,217,482 and Total Actual is 1,214,413. I verified these totals separately in Excel, SQL and Power BI on the same dataset, so the Python result is the fourth independent match.



\## How to run



```

pip install pandas

python analysis.py

```



\## Output



| Department | Budget | Actual | Variance |

|---|---|---|---|

| Marketing | 415,882 | 423,337 | 7,455 |

| Operations | 327,484 | 324,106 | -3,378 |

| Sales | 474,116 | 466,970 | -7,146 |

