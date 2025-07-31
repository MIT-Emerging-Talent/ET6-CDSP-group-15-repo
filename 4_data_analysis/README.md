# P2P Loan Default Prediction: Model Training & Evaluation

This directory contains the Jupyter notebooks used to train, evaluate, and tune
 machine learning models for predicting loan defaults on the Lending Club
 dataset. Each notebook represents a complete workflow, from data preprocessing
 to model performance analysis.

## Notebooks Overview

### 1. `07_p2p_lending_(logreg,RF,XGB).ipynb`

- **Purpose:** This notebook provides an end-to-end workflow, including
 extensive data cleaning, feature engineering, and model training. It uses
  **class weighting** to handle the imbalanced nature of the dataset.
- **Data Source:** Raw data (`accepted_2007_to_2018Q4.csv.gz`) downloaded
   directly from [Kaggle Hub](https://www.kaggle.com/datasets/wordsforthewise/lending-club).
- **Output:** A tuned XGBoost model saved as `xgb_final_model.pkl`.

#### Workflow Summary for `07_p2p_lending_(logreg,RF,XGB).ipynb`

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
    - **Feature Importance:** The final tuned XGBoost model is analyzed
   with **SHAP (SHapley Additive exPlanations)** to identify the most
   influential features in predicting loan defaults.

---

### 2. `modeling-2.ipynb`

- **Purpose:** This notebook focuses on model training and evaluation using
 a different strategy for handling class imbalance: **downsampling**. It starts
  with an already cleaned dataset.
- **Data Source:** Pre-cleaned data (`clean_lendingclub_data.csv`) downloaded
   from a Google Drive link.
- **Output:** Comparative analysis and visualizations of model performance.

#### Workflow Summary for `modeling.ipynb`

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

---

### Summary of Approaches

| Feature     | `07_p2p_lending_(logreg,RF,XGB).ipynb`  | `modeling-2.ipynb`  |
| ---------------------- | -------- | --------- |
| **Data Source** | Raw data from Kaggle Hub |Pre-cleaned CSV from Google Drive |
| **Data Preparation** | Cleaning and feature engineering| mostly cleaned data |
| **Imbalance Handling** |**Class Weighting**| **Downsampling** of majority class|
| **Models Trained** | Logistic Regression, XGBoost| Same + XGBoost|
| **Hyperparameter Tuning** | `RandomizedSearchCV` for XGBoost | Same + `GridSearchCV`|

## Visualizations

Here are some visualizations to illustrate key concepts and model performance:

### Peer-to-Peer Lending Overview

![P2P Lending](https://private-us-east-1.manuscdn.com/sessionFile/QzTYV1DVgbrOdMbmXYQraJ/sandbox/KOBe3Kq0CFms6oGReqz8R1-images_1753118632439_na1fn_L2hvbWUvdWJ1bnR1LzRfZGF0YV9hbmFseXNpcy9pbWFnZXMvcDJwX2xlbmRpbmc.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvUXpUWVYxRFZnYnJPZE1ibVhZUXJhSi9zYW5kYm94L0tPQmUzS3EwQ0ZtczZvR1JlcXo4UjEtaW1hZ2VzXzE3NTMxMTg2MzI0MzlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUx6UmZaR0YwWVY5aGJtRnNlWE5wY3k5cGJXRm5aWE12Y0RKd1gyeGxibVJwYm1jLmpwZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=XGcoq0nfHiwq~fnQPjo6o2d3hGQKWiW987YdTQ3TI8mTBTiVTc41mpYyIGl02GhXzRjtdQpEAsP~iZOuH4kR0VIzOXotWbvPbFrocbM13Q12okNXZBzx5GMCXXiD~Jwj8VXUuSh9aF1R~ILSCOyaMf2emyHORTLVriozeTmy9lue44N~AYBGUhvQz5bvKnO7UKy-B9FsLaLJ8JzDn~p6GzQTvnRuMrwRfu7~n5JjIBRjcK8JcQPQzyxsFKHWDTtK~anUTAcC86ht4KNwEo9wYZp1gV9Q4EfTg-NbXA2wnZ5GRlRBocfgMLZJpu0gfcI4j4698mkg-RBUqiQWukijlg__)

*Figure 1: Illustrates the basic concept of Peer-to-Peer Lending.*

### Credit Risk Analysis

![Credit Risk Analysis](https://private-us-east-1.manuscdn.com/sessionFile/QzTYV1DVgbrOdMbmXYQraJ/sandbox/KOBe3Kq0CFms6oGReqz8R1-images_1753118632440_na1fn_L2hvbWUvdWJ1bnR1LzRfZGF0YV9hbmFseXNpcy9pbWFnZXMvY3JlZGl0X3Jpc2tfYW5hbHlzaXM.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvUXpUWVYxRFZnYnJPZE1ibVhZUXJhSi9zYW5kYm94L0tPQmUzS3EwQ0ZtczZvR1JlcXo4UjEtaW1hZ2VzXzE3NTMxMTg2MzI0NDBfbmExZm5fTDJodmJXVXZkV0oxYm5SMUx6UmZaR0YwWVY5aGJtRnNlWE5wY3k5cGJXRm5aWE12WTNKbFpHbDBYM0pwYzJ0ZllXNWhiSGx6YVhNLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=WIQdZG9s4tT1RVAyUZT~xb6juwgaE5LRGKLmHPHS5008L8ss-6ht3Gfc42BzBCIr9sI~-6ru3nOxIEa70Iu3gy-8y5QqglwWqNz8kfT6fjVDcJlOsFVnUWxXgYfoBU9rP39dRT6k2Obb4ToG0IQ0d9TUTr8v9QTJ4v6BMM~fQeu~i9D3qOFkzD8~rNFZ7mrvtbYjLLwC58W-Ij9bhgDK8PuVeVrHbNizLrdNvl3CaqHFF80A4cO1SIdQhQQjl2pCBwqZA0j18-NwyC0hWpDq1XQYbUgw8~SbtuzJgMty-txrjF-8frI9f248GfcCUKd~oCQh3z3jTjPItOv0cUoT6Q__)

*Figure 2: Depicts key components and techniques involved in credit risk analysis.*

### Confusion Matrix Example

![Confusion Matrix](https://private-us-east-1.manuscdn.com/sessionFile/QzTYV1DVgbrOdMbmXYQraJ/sandbox/KOBe3Kq0CFms6oGReqz8R1-images_1753118632503_na1fn_L2hvbWUvdWJ1bnR1LzRfZGF0YV9hbmFseXNpcy9pbWFnZXMvY29uZnVzaW9uX21hdHJpeA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvUXpUWVYxRFZnYnJPZE1ibVhZUXJhSi9zYW5kYm94L0tPQmUzS3EwQ0ZtczZvR1JlcXo4UjEtaW1hZ2VzXzE3NTMxMTg2MzI1MDNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUx6UmZaR0YwWVY5aGJtRnNlWE5wY3k5cGJXRm5aWE12WTI5dVpuVnphVzl1WDIxaGRISnBlQS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=FSovm0OVL5zv1EOaZensvyTfB2qwNDq0~TNA51Umkj0BOu6Y4rwTfleIncG8~2yHeko7H-kcSnbjdf2MPxicnOGr9quA4bLUZbhVaJenFX-WObJmOb5sdRz7FVNSygkVzAYGf66WuSEvRZMjQllp47Ql1A8nvCNh7tX9Hx6RJApX5DFzcgbNoCKAUDK3VI5lUxTsWS0Za0KY1zSDD0TLfp8FUj2d5~8sRoEa4rn6tELibX-MSeACexdbyYg80VJzrTKASmucHQrc~4Ko68n81PSfNrZQADp1PWki~RNJkQg2R0fUtwiIY5iw7eZJFrKmx~r3LGFy~6eEytOyPM8KrQ__)

*Figure 3: An example of a Confusion Matrix, used to evaluate the performance
 of a classification model.*

### ROC AUC Curve Example

![ROC AUC Curve](<https://private-us-east-1.manuscdn.com/sessionFile/QzTYV1DVgbrOdMbmXYQraJ/sandbox/KOBe3Kq0CFms6oGReqz8R1-images_1753118632504_na1fn_L2hvbWUvdWJ1bnR1LzRfZGF0YV9hbmFseXNpcy9pbWFnZXMvcm9jX2F1Y19jdXJ2ZQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvUXpUWVYxRFZnYnJPZE1ibVhZUXJhSi9zYW5kYm94L0tPQmUzS3EwQ0ZtczZvR1JlcXo4UjEtaW1hZ2VzXzE3NTMxMTg2MzI1MDRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUx6UmZaR0YwWVY5aGJtRnNlWE5wY3k5cGJXRm5aWE12Y205algyRjFZMTlqZFhKMlpRLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=wAwMP9-MMQknaJlagaL9Uc042iVRfn-U4BnjT4hQ8WGCw8BUQg7evJTVxDqzT3V~3jwUd90ZuRqXDZNfrcSPk8WOPct3XzJuObexM6tWn2idtBch4IJJd1uwW6X3EvZZ2CQWgUPo2HEPZUkiMKHLRZ2Zcu7PIeVoY9FTZQZltWNRkdsEL7ACzL2Wp-xmwFb5dMOQfJNfdd7hstyELtGlSIDrc3ttsGxbvHIi5zLzO7hY-2c19LXkX3X~a6PvzH4ohC1U3LRROAjnD8byG8gHmZF~EwjWqYOEuUrTevKSfwOoyeoDSWghnBWduizIFoea-e8ULZ1RTL6JHL7oIJ3FmQ__>)

*Figure 4: An example of an ROC AUC Curve, illustrating a model's ability to
 distinguish between classes.*
