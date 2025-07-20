import pandas as pd


def wrangle_lending_club_data(filepath):
    """
    This function takes the filepath to the Lending Club dataset from Kaggle,
    cleans it, renames columns for clarity, and prepares it for analysis.
    """
    # --- 1. Load Data with Selected Columns ---
    # Based on your selection, we specify which columns to load to save memory.
    relevant_columns = [
        "loan_amnt",
        "term",
        "int_rate",
        "grade",
        "installment",
        "purpose",
        "annual_inc",
        "dti",
        "delinq_2yrs",
        "inq_last_6mths",
        "home_ownership",
        "emp_length",
        "fico_range_low",
        "fico_range_high",
        "issue_d",
        "earliest_cr_line",
        "open_acc",
        "pub_rec",
        "revol_bal",
        "revol_util",
        "total_acc",
        "loan_status",
        "verification_status",
        "application_type",
        "addr_state",
    ]
    df = pd.read_csv(filepath, usecols=relevant_columns)

    # --- 2. Define the Target Variable ---
    # Keep only loans with a final, resolved status.
    final_statuses = ["Fully Paid", "Charged Off", "Default"]
    df = df[df["loan_status"].isin(final_statuses)].copy()

    # Create a binary 'is_default' target variable.
    # 'Charged Off' and 'Default' are considered default events.
    df["is_default"] = df["loan_status"].apply(
        lambda x: 1 if x in ["Charged Off", "Default"] else 0
    )

    # --- 3. Clean and Transform Features ---
    # Clean 'term' column (e.g., ' 36 months' -> 36)
    df["term"] = df["term"].str.extract("(\d+)").astype(int)

    # Clean 'int_rate' column (e.g., '12.5%' -> 12.5)
    df["revol_util"] = df["revol_util"].str.replace("%", "").astype(float)
    df["int_rate"] = df["int_rate"].astype(float)  # Already clean in some versions

    # Clean and map 'emp_length' to numerical values
    emp_length_map = {
        "< 1 year": 0.5,
        "1 year": 1,
        "2 years": 2,
        "3 years": 3,
        "4 years": 4,
        "5 years": 5,
        "6 years": 6,
        "7 years": 7,
        "8 years": 8,
        "9 years": 9,
        "10+ years": 10,
    }
    df["emp_length"] = df["emp_length"].map(emp_length_map)

    # --- 4. Feature Engineering ---
    # Create a single, average FICO score
    df["fico_score"] = (df["fico_range_low"] + df["fico_range_high"]) / 2

    # Engineer credit history length
    df["issue_d"] = pd.to_datetime(df["issue_d"], format="%b-%Y")
    df["earliest_cr_line"] = pd.to_datetime(df["earliest_cr_line"], format="%b-%Y")
    df["credit_history_length_days"] = (df["issue_d"] - df["earliest_cr_line"]).dt.days

    # --- 5. Handle Missing Values ---
    # For key columns, we'll impute with the median which is robust to outliers.
    for col in [
        "dti",
        "revol_util",
        "emp_length",
        "delinq_2yrs",
        "inq_last_6mths",
        "open_acc",
        "pub_rec",
        "total_acc",
    ]:
        if col in df.columns:
            df[col].fillna(df[col].median(), inplace=True)

    # --- 6. Drop Original/Intermediate Columns ---
    # Drop columns that have been transformed or are no longer needed.
    df = df.drop(
        columns=[
            "loan_status",
            "fico_range_low",
            "fico_range_high",
            "issue_d",
            "earliest_cr_line",
        ]
    )

    # --- 7. Rename Columns for Clarity ---
    # Create a mapping from old names to new, more descriptive names.
    column_rename_map = {
        "loan_amnt": "LoanAmount",
        "term": "LoanTermMonths",
        "int_rate": "InterestRate",
        "grade": "LoanGrade",
        "installment": "MonthlyInstallment",  # Note: This is highly correlated with LoanAmount, InterestRate, and Term.
        "purpose": "LoanPurpose",
        "annual_inc": "AnnualIncome",
        "dti": "DebtToIncomeRatio",
        "delinq_2yrs": "DelinquenciesLast2Yrs",
        "inq_last_6mths": "InquiriesLast6Mths",
        "home_ownership": "HomeOwnership",
        "emp_length": "EmploymentLengthYrs",
        "open_acc": "OpenAccounts",
        "pub_rec": "PublicRecords",
        "revol_bal": "RevolvingBalance",
        "revol_util": "RevolvingUtilizationRate",
        "total_acc": "TotalAccounts",
        "verification_status": "VerificationStatus",
        "application_type": "ApplicationType",
        "addr_state": "AddressState",
        "fico_score": "FICOScore",
        "credit_history_length_days": "CreditHistoryLengthDays",
        "is_default": "IsDefault",
    }
    df = df.rename(columns=column_rename_map)

    print("Data wrangling complete.")
    return df


# --- How to Use the Function ---
# Provide the path to your Kaggle dataset file.
# This assumes the file is named 'loan.csv' and is in the same directory.
# If you are using Google Colab, you will need to upload the file first.
try:
    cleaned_df = wrangle_lending_club_data("loan.csv")
    print("\nPreview of the cleaned and renamed data:")
    print(cleaned_df.head())
    print("\nInfo of the final DataFrame:")
    cleaned_df.info()
except FileNotFoundError:
    print(
        "Error: 'loan.csv' not found. Please ensure the file is in the correct directory."
    )
