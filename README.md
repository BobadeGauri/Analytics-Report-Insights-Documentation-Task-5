# Task 5 — Analytics Report & Insights Documentation

## Overview
This project demonstrates a complete analytics reporting workflow: defining business objectives, validating data, calculating KPIs, producing visualizations, interpreting findings, and recommending next steps.

**Important:** `sample_sales_data.csv` is synthetic illustrative data created for this assignment. It does not represent a real company or real customers. Replace it with authorized business data before making operational decisions.

## Files
- `Analytics_Report_Insights_Documentation.docx` — completed Word report
- `sample_sales_data.csv` — sample dataset
- `analysis.py` — reproducible Python analysis and chart generation
- `monthly_trend.png`, `category_revenue.png`, `region_revenue.png` — report visuals

## Requirements
Python 3.10 or newer, pandas, matplotlib.

## Run
```bash
python -m pip install pandas matplotlib
python analysis.py
```
Charts are generated in the `outputs/` directory.

## Main KPIs
- Total revenue
- Total profit
- Total orders
- Weighted profit margin
- Revenue by month, category, and region

## Method
1. Validate required columns, missing values, duplicate grouping keys, and negative values.
2. Calculate overall and grouped KPIs using pandas.
3. Plot monthly trends and category/region comparisons using matplotlib.
4. Use the Word report to document findings, limitations, and recommendations.

## Suggested GitHub repository
Create a new public repository named `Analytics-Report-Insights-Documentation`, upload these files, and use the repository URL shown by GitHub in the internship form. Do not submit a placeholder URL.
