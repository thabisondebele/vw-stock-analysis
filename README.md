# Volkswagen Stock Analysis (2000–2026)

A complete end-to-end data science project analyzing 25 years of Volkswagen 
AG stock data. Built as a portfolio project demonstrating Python data analysis 
and Power BI dashboard development.

---

## Project Overview

This project explores daily trading data for Volkswagen AG (VOW) from 2000 
to 2026, covering major market events including the 2008 financial crisis, 
the 2015 Dieselgate scandal, and the COVID-19 crash of 2020.

---

## Tools & Technologies

- Python 3.12
- pandas, numpy, matplotlib, seaborn
- Jupyter Notebooks
- Microsoft Power BI Desktop
- Dataset: Kaggle — Volkswagen Stock Data 1995–2026

---

## Project Structure

```
vw_project/
├── data/
│   ├── raw/                  # Original dataset (not uploaded to GitHub)
│   └── processed/            # Cleaned and exported data files
├── notebooks/
│   ├── 01_data_loading_cleaning.ipynb
│   ├── 02_eda_visualization.ipynb
│   ├── 03_insights.ipynb
│   └── 04_export_powerbi.ipynb
├── output/                   # Saved chart images
├── powerbi/                  # Power BI dashboard file
└── README.md
```

---

## Key Findings

- VW stock grew from ~€50 in 2000 to a peak of €520 in 2008 during the 
  Porsche short squeeze — briefly making VW the most valuable company 
  in the world

- The 2008 financial crisis produced the worst annual return in the dataset 
  at -70% in 2009

- The best consecutive years were 2006 (+90%) and 2007 (+84%), both driven 
  by pre-crisis economic growth and Porsche's secret accumulation of shares

- Dieselgate (September 2015) caused an immediate ~40% crash in weeks, 
  visible as a sharp drop across price, volatility, and RSI charts

- COVID-19 (March 2020) caused a sharp crash followed by a strong recovery 
  to €320 by 2021, driven by EV investment optimism

- VW has declined consistently from 2022 to 2025, returning to 2010 price 
  levels — reflecting factory closures, EV profitability struggles, and 
  Chinese competition

- July and August are historically the strongest months for VW stock. 
  September through November are consistently the weakest

- Maximum single-day volatility reached 28.64 during the 2008 crisis — 
  nearly 14 times the average of 2.12

---

## Dashboard Pages

| Page | Description |
|---|---|
| Executive Overview | Full price history, volume, and core KPI cards |
| Annual Performance | Year by year returns with best and worst years highlighted |
| Technical Analysis | Price vs moving averages and MACD momentum indicator |
| Volatility & Risk | 30-day rolling volatility, RSI, and annual risk comparison |
| Seasonal Patterns | Monthly return heatmap and average return by month |

---

## How to Reproduce This Project

1. Clone this repository
2. Navigate to the project folder
3. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Download the dataset from Kaggle and place it in data/raw/
6. Run notebooks in order from 01 to 04
7. Open powerbi/VW_Stock_Dashboard.pbix in Power BI Desktop

---

## Data Cleaning Decisions

- Dataset trimmed to 2000 onwards — 1995 to 1999 excluded due to severe 
  volume data gaps (109 zero-volume days in 1995 alone)
- 243 zero-volume days replaced using forward fill
- Null values in Close price filled using forward fill
- Volatility_30d column added as it was missing from the source dataset

---

## Dataset Source

Kaggle: Volkswagen Stock Data 1995–2026  
https://www.kaggle.com/datasets/bsthere/volkswagen-stock-data-1995-2026

---

*This project was built as part of a data science portfolio. 
All analysis is for educational purposes only and does not 
constitute financial advice.*
