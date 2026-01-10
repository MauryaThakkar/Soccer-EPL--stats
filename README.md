# Sports Analytics Project: Match & Team Performance Analysis

## Project Overview
This project analyzes English Premier League (EPL) football match data to identify key factors influencing match outcomes and team performance. Using a combination of **Python** and **R**, the project demonstrates skills in data cleaning, exploratory data analysis, statistical analysis, visualization, and predictive modeling.

Python is primarily used for data preprocessing, feature engineering, and modeling, while R is used for statistical summaries and high-quality visualizations.

---

## Objectives
- Analyze team performance trends across a season
- Compare home vs. away performance
- Identify variables associated with winning matches
- Build a simple predictive model for match outcomes
- Demonstrate proficiency in both Python and R for data analysis

---

## Data Sources

### 1. Match Results Data
Match-level data is sourced from **football-data.co.uk**. 

We have automated the data ingestion process. The script will download the 2021-2022 EPL season data automatically.

## Setup & Usage

### 1. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 2. Run Data Pipeline
This script downloads the raw data, processes it, and saves the cleaned version.
```bash
python3 src/python/main.py
```

### 3. View Processed Data
You can view the cleaned dataset (`data/processed/EPL_Cleaned.csv`) using the command line or by opening it in Excel/Numbers.

**Terminal Quick View (First 5 rows):**
```bash
python3 -c "import pandas as pd; df = pd.read_csv('data/processed/EPL_Cleaned.csv'); print(df.head())"
```

**Open in Default App (Excel/Numbers):**
```bash
open data/processed/EPL_Cleaned.csv
```

## Data Dictionary
For a detailed explanation of all columns (stats, betting odds, etc.), please refer to:
- **[EPL Data Cheat Sheet](data/EPL_Data_Cheat_Sheet.md)**
