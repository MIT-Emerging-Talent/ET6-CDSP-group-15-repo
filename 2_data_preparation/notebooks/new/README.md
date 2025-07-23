# P2P Loan Default Prediction: Model Training & Evaluation

This directory contains the Jupyter notebooks used to train, evaluate, and tune
 machine learning models for predicting loan defaults on the Lending Club
 dataset. Each notebook represents a complete workflow, from data preprocessing
 to model performance analysis.

## Notebooks Overview

### 1. `07_p2p_lending_(logreg,RF,XGB).ipynb`

- **Purpose:** This notebook provides an end-to-end workflow, including
 extensive data cleaning, feature engineering, and model training. It
 uses **class weighting** to handle the imbalanced nature of the dataset.
- **Data Source:** Raw data (`accepted_2007_to_2018Q4.csv.gz`) downloaded
 directly from [Kaggle Hub](https://www.kaggle.com/datasets/wordsforthewise/lending-club).
- **Output:** A tuned XGBoost model saved as `xgb_final_model.pkl`.

#### Workflow Summary (Notebook 1)

1. **Data Loading & Filtering:**
    - Loads the complete raw dataset from Kaggle Hub.
    - Selects a subset of 24 relevant features for the initial analysis.

2. **Target Variable Engineering:**
    - Defines "bad" loan statuses (`Charged Off`, `Default`) to create the
   binary target variable `is_default`.
    - Filters the dataset to only include loans with resolved outcomes
   (`Fully Paid`, `Charged Off`, `Default`), removing active loans.

3. **Feature Engineering & Preprocessing:**
    - **Categorical Encoding:**
        - `verification_status` is converted into a binary `is_verified` feature.
        - `home_ownership` and `grade` are one-hot encoded.
        - `purpose` is consolidated into the top 5 categories plus an "other"
   category before one-hot encoding.
        - `application_type` is mapped to binary values (0 for Individual, 1
   for Joint App).
    - **Numerical & Date Cleaning:**
        - `term` is cleaned from string format (e.g., "36 months") to an
   integer (36).
        - `emp_length` is converted from string to a numerical scale, handling
   special cases like `< 1 year` and `10+ years`.
        - `credit_history_length` is engineered by calculating the time between
   the loan `issue_d` and the `earliest_cr_line`.
    - **Final Touches:** All object-type columns are stripped of
   leading/trailing whitespaces, and unnecessary columns like `addr_state` are dropped.

4. **Model Training & Evaluation:**
    - **Models:** Trains and evaluates Logistic Regression and XGBoost models.
   *Note: A Random Forest model is initialized but commented out in the final run.*
    - **Imbalance Handling:** Uses the `class_weight="balanced"` and
   `scale_pos_weight` parameters to address the class imbalance during training.
    - **Evaluation:** Performance is measured using Classification Reports,
   Confusion Matrices, ROC-AUC curves, and Precision-Recall curves.

5. **Hyperparameter Tuning & Feature Importance:**
    - **Tuning:** `RandomizedSearchCV` is used to find the optimal
   hyperparameters for the XGBoost model based on the ROC-AUC score.
    - **Feature Importance:** The final tuned XGBoost model is analyzed with
   **SHAP (SHapley Additive exPlanations)** to identify the most influential
 features in predicting loan defaults.

---

### 2. `modeling-2.ipynb`

- **Purpose:** This notebook focuses on model training and evaluation using a
   different strategy for handling class imbalance: **downsampling**. It
   starts with an already cleaned dataset.
- **Data Source:** Pre-cleaned data (`clean_lendingclub_data.csv`) downloaded
   from a Google Drive link.
- **Output:** Comparative analysis and visualizations of model performance.

#### Workflow Summary

1. **Data Loading:**
    - Loads a pre-cleaned dataset, bypassing the extensive feature engineering
   steps seen in the other notebook.

2. **Imbalance Handling:**
    - Applies **downsampling** by taking a random sample of the majority class
   (non-defaults) to match the number of samples in the minority class
   (defaults), creating a balanced training set.

3. **Preprocessing:**
    - Splits the data into 80% training and 20% testing sets using
   stratification to maintain class balance.
    - Handles missing values using `SimpleImputer` and scales numerical
   features with `StandardScaler`.

4. **Model Training & Evaluation:**
    - **Models:** Trains and evaluates three models: **Logistic Regression**,
   **Random Forest**, and **XGBoost**.
    - **Evaluation:** Compares the models based on:
        - Classification Reports and Confusion Matrices.
        - ROC-AUC and Precision-Recall curves.
        - A final summary bar chart visualizing the performance across all key metrics.

5. **Hyperparameter Tuning:**
    - Demonstrates hyperparameter tuning for the XGBoost model using both
   `GridSearchCV` and `RandomizedSearchCV` to find the best parameters and
   improve the AUC score.
