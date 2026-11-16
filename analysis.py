import glob
import pandas as pd

files = sorted(glob.glob("data/*.csv"))

tables = [ ]
for f in files:
      tables.append(pd.read_csv(f))

df = pd.concat(tables)
print(len(df))

summary = df.groupby("Department")[["Budget", "Actual"]].sum()
summary["Variance"] = summary["Actual"] - summary["Budget"]
print(summary)

total_budget = df["Budget"].sum()
total_actual = df["Actual"].sum()
assert total_budget == 1217482, "Budget total does not reconcile"
assert total_actual == 1214413, "Actual total does not reconcile"
print("Reconciled: totals match the verified check totals")