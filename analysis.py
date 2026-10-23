"""
Task 5: Analytics Report & Insights Documentation
Demonstration project using illustrative synthetic sales data.
Run: python analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "sample_sales_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
required = {"Month", "Region", "Category", "Orders", "Revenue_USD", "Profit_USD"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")
if df[list(required)].isnull().any().any():
    raise ValueError("Missing values detected in required fields.")
if df.duplicated(subset=["Month", "Region", "Category"]).any():
    raise ValueError("Duplicate month-region-category records detected.")
if (df[["Orders", "Revenue_USD", "Profit_USD"]] < 0).any().any():
    raise ValueError("Negative order/revenue/profit values detected.")

total_revenue = df["Revenue_USD"].sum()
total_profit = df["Profit_USD"].sum()
total_orders = df["Orders"].sum()
weighted_margin = total_profit / total_revenue * 100 if total_revenue else 0
print(f"Rows: {len(df)}")
print(f"Total revenue: ${total_revenue:,.2f}")
print(f"Total profit: ${total_profit:,.2f}")
print(f"Total orders: {total_orders:,}")
print(f"Weighted profit margin: {weighted_margin:.2f}%")
print("\nRevenue by category:")
print(df.groupby("Category")["Revenue_USD"].sum().sort_values(ascending=False))
print("\nRevenue by region:")
print(df.groupby("Region")["Revenue_USD"].sum().sort_values(ascending=False))

monthly = df.groupby("Month", as_index=False)[["Revenue_USD", "Profit_USD"]].sum()
plt.figure(figsize=(9, 5))
plt.plot(monthly["Month"], monthly["Revenue_USD"], marker="o", label="Revenue")
plt.plot(monthly["Month"], monthly["Profit_USD"], marker="s", label="Profit")
plt.xticks(rotation=45, ha="right")
plt.ylabel("USD")
plt.title("Monthly Revenue and Profit")
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "monthly_trend.png", dpi=160)
plt.close()

for column, metric, filename, title in [
    ("Category", "Revenue_USD", "category_revenue.png", "Revenue by Category"),
    ("Region", "Revenue_USD", "region_revenue.png", "Revenue by Region"),
]:
    summary = df.groupby(column)[metric].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    summary.plot(kind="bar")
    plt.ylabel("USD")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(OUT / filename, dpi=160)
    plt.close()

print(f"\nCharts saved in: {OUT}")
