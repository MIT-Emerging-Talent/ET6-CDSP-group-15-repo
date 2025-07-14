## Dataset: `accepted_2007_to_2018Q4.csv`

**Description:**  
This dataset contains detailed loan-level data from LendingClub for all accepted  
loan applications between 2007 and Q4 2018. It includes borrower information,  
loan terms, interest rates, installment amounts, FICO scores, employment details,  
credit history, and final loan statuses (e.g., Fully Paid, Charged Off, etc.).

It is compiled from LendingClub's public release, originally fragmented across  
many smaller files on their website. The dataset was preprocessed and cleaned  
by a Kaggle contributor to ease accessibility and analysis.

Key fields include:  

- `loan_amnt`, `term`, `int_rate`, `installment`, `grade`, `emp_length`,  
  `home_ownership`, `annual_inc`, `loan_status`, `dti`, `fico_range_low/high`,  
  `revol_util`, `total_acc`, `issue_d`, and `purpose`.  

FICO scores are available only for accepted loans. Fields like `int_rate` and  
`revol_util` have been cleaned (percent symbols removed, converted to float).  
The data also retains the `url` field as of 2018 Q2 for record traceability.

**Why We Need It:**  
This is our **primary dataset** for modeling loan default risk in P2P lending.  
It enables us to build and train machine learning models using real-world  
financial features and outcomes. It is central to our analysis of risk factors  
in borrower behavior and platform-level trends in loan performance.

**Source and Notes:**  
Originally sourced and preprocessed by the Kaggle contributor  
[Wordsforthewise](https://www.kaggle.com/datasets/wordsforthewise/lending-club)  
with supporting code available at:  
<https://github.com/nateGeorge/preprocess_lending_club_data>

**File Type:**  
CSV (gzip-compressed) – decompression needed before use.  
