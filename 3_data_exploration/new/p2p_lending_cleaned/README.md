# Exploratory Data Analysis: P2P Lending Cleaned Dataset

This folder contains exploratory data analysis (EDA) for the processed P2P lending dataset (`p2p_df_final_cleaned_1000.csv`).

## Dataset Description

- **Source:** `1_datasets/processed_data/p2p_df_final_cleaned_1000.csv`
- **Rows:** 1,000
- **Columns:** Loan amount, term, interest rate, installment, employment length, income, DTI, FICO ranges, loan grades (B-G), home ownership, verification status, loan purpose (one-hot), and loan status (binary).

## Analysis Steps

1. **Data Overview:**
   - Printed info, descriptive statistics, and null value counts.
   - Saved summary statistics to `figures/p2p_descriptive_stats.csv`.
2. **Numeric Feature Distributions:**
   - Histograms and boxplots for all numeric columns (e.g., loan amount, interest rate, income, DTI, FICO scores, etc.).
3. **Categorical Feature Distributions:**
   - Bar plots for loan grades, home ownership, verification status, application type, loan status, and all loan purposes.
4. **Correlation Analysis:**
   - Correlation heatmap for all numeric features.

All figures are saved in the `figures/` subfolder.

## How to Reproduce

Open and run the Jupyter notebook in this folder to reproduce the EDA and generate figures. All outputs will be saved in the `figures/` subfolder.

---
For more details, see the notebook and generated figures.
