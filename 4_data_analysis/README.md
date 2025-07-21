# 4. Data Analysis

This section details the comprehensive data analysis performed on the Lending Club
dataset to predict loan default risk. It covers the methodologies, model evaluations,
and key findings from the application of various machine learning models, including
Logistic Regression, Random Forest, and XGBoost.

## 4.1 Introduction

The primary objective of this data analysis phase was to develop robust predictive
models for identifying loan default risk within the peer-to-peer (P2P) lending
ecosystem. Leveraging a comprehensive dataset from Lending Club, we aimed to uncover
the key borrower and loan characteristics that best predict default outcomes. This
analysis is crucial for improving credit assessment, informing smarter lending
decisions, and enhancing investor confidence in alternative finance platforms. The
insights derived from this phase are intended to support platforms, investors, and
regulators with transparent and data-backed risk insights.

## 4.2 Data Preparation and Feature Engineering

Before model training, the raw Lending Club dataset underwent significant
 data preparation and feature engineering to ensure data quality
  and create meaningful variables for analysis. The initial dataset
   contained over 2 million loans with 151 features. Key steps included:

* **Filtering Relevant Columns**: Only columns deemed relevant to the research
 question, such as `loan_amnt`, `term`, `int_rate`, `grade`, `purpose`
 , `annual_inc`, `dti`, `delinq_2yrs`, `inq_last_6mths`, `home_ownership`,
 `emp_length`, `issue_d`, `earliest_cr_line`, `open_acc`, `pub_rec`,
 `revol_bal`, `revol_util`, `total_acc`, `verification_status`, and
 `application_type`, were selected. The target variable, `loan_status`,
 was also included.
* **Target Variable Transformation**: The `loan_status` column was transformed
 into a binary target variable, `is_default`, where 'Charged Off' and 'Default'
 statuses were mapped to 1 (default), and other statuses (e.g., 'Fully Paid')
 were mapped to 0 (non-default). Loans without a resolved outcome were excluded
 from the analysis.
* **Handling Missing Values**: Missing values were addressed by imputing
 numerical columns with their mean and categorical columns with their mode.
 This ensured that all features were complete for model training.
* **Date-Time Feature Engineering**: The `issue_d` (loan issue date) and
 `earliest_cr_line` (earliest credit line) columns were used to engineer a new
 feature, `credit_history_length`, representing the duration of the borrower's
 credit history in months. This was calculated as the difference between
 `issue_d` and `earliest_cr_line`, divided by 30 days.
* **Categorical Feature Processing**:
  * Leading/trailing white spaces were stripped from object-type columns.
  * The `emp_length` (employment length) column was cleaned and converted to a
   numerical format.
  * The `home_ownership` categories 'ANY', 'OTHER', and 'NONE' were grouped
   into 'OTHER' to simplify the feature.
  * The top 5 most frequent `purpose` categories were identified, and less
   frequent categories were grouped into 'other'. One-hot encoding was then
   applied to the `purpose` column to convert it into numerical features.

These steps were crucial in preparing a clean and well-structured dataset for
 the subsequent machine learning modeling. The final dataset used for modeling
  consisted of 1,345,350 resolved loans with 23 features, including the
 `is_default` target variable.

## 4.3 Model Evaluation

Three classification models—Logistic Regression, Random Forest, and
 XGBoost—were employed to predict loan default. The models were evaluated based
 on several key metrics, including Accuracy, Precision, Recall, F1-score, and
 ROC AUC Score. Given the inherent class imbalance in loan default datasets
 (significantly fewer defaults than non-defaults), special attention was paid
 to metrics that are robust to imbalance, particularly Recall for the default
 class and ROC AUC.

### 4.3.1 Initial Model Performance (Before Class Balancing)

Initially, all models exhibited high overall accuracy (around 80%) but
 struggled to correctly identify the minority class (defaults). This is a
 common issue in imbalanced datasets, where models tend to be biased towards
 the majority class.

#### Logistic Regression

| Metric                | Value   | Notes                                       |
| :-------------------- | :------ | :-------------------------------------------|
| Accuracy   | ~80%    | Looks high, but can be misleading due to class imbalance|
| Precision (Class 0)   | 0.81    | Model is usually correct when predicting no-default|
| Recall (Class 0)      | 0.99    | Catches nearly all no-defaults             |
| Precision (Class 1)   | 0.55    | Only 55% of predicted defaults are actually defaults|
| Recall (Class 1) | 0.05 | Misses 95% of actual defaults|
| ROC AUC Score   | ~0.66   | Some ability to distinguish classes, but not great|
| Confusion Matrix      | 📉 Imbalanced | Many false negatives (missed defaults)|

*Conclusion*: The Logistic Regression model was heavily biased towards
 predicting non-defaults, resulting in a very low recall for the default class.

#### Random Forest

| Metric                | Value   | Notes                                     |
| :-------------------- | :------ | :-------------------------------------------|
| Accuracy              | ~80%    | Same as logistic regression             |
| Precision (Class 0)   | 0.81    | Still good at predicting no-defaults   |
| Recall (Class 0)      | 0.99    | Similar to logistic regression    |
| Precision (Class 1)   | 0.55| Same as logistic regression  |
| Recall (Class 1)      | 0.06    | Slightly better than logistic regression|
| ROC AUC Score         | ~0.70   | Better at separating the classes than LR |
| Confusion Matrix      | 📉 Imbalanced | Still many false negatives, < LR|

*Conclusion*: Random Forest showed a marginal improvement in ROC AUC but still
suffered from poor recall for the default class. This indicates a persistent
bias towards the majority class.

#### XGBoost

| Metric                | Value   | Notes                                    |
| :-------------------- | :------ | :---------------------------------------|
| Precision (Class 1)   | 0.56    | 56% of prediction accuracy|
| Recall (Class 1)      | 0.09    | Only 9% of actual defaults correctly got|
| F1-score (Class 1)    | 0.16    | Low, poor balance between precision and recall|
| Overall Accuracy      | 0.80    | Biased due to class imbalance            |
| ROC AUC Score         | 0.72    | Decent discrimination ability, best so far|

*Conclusion*: XGBoost performed the best among the initial models in terms of
 ROC AUC, showing a better ability to distinguish between classes, though
  recall for defaults remained low.

### 4.3.2 Model Performance After Class Balancing

To address the class imbalance, techniques such as class weighting (for
 Logistic Regression and Random Forest) and `scale_pos_weight` (for XGBoost)
  were applied. The objective was to improve the recall of the minority class
 (loan defaults) without excessively compromising precision.

#### Logistic Regression (with class weighting)

* **Accuracy**: 0.65
* **Precision (Class 1)**: 0.32
* **Recall (Class 1)**: 0.67
* **F1-score (Class 1)**: 0.44
* **Confusion Matrix**:

    ```bash
    [[139796  75477]
     [ 17555  36147]]
    ```

  * **True Negatives (TN)**: 139,796 (Correctly predicted not default)
  * **False Positives (FP)**: 75,477 (Predicted default but were not)
  * **False Negatives (FN)**: 17,555 (Missed actual defaulters ❌)
  * **True Positives (TP)**: 36,147 (Correctly predicted defaulters ✅)

*Conclusion*: This model showed strong recall (67%) for defaults, which is
 critical for risk prediction. However, it also resulted in a high number of
  false positives, meaning many non-defaulting loans were wrongly flagged as risky.

#### Random Forest (with `class_weight="balanced"`)

* **Accuracy**: 0.80
* **Precision (Class 1)**: 0.55
* **Recall (Class 1)**: 0.06
* **F1-score (Class 1)**: 0.11
* **ROC AUC Score**: 0.705
* **Confusion Matrix**:

    ```bash
    [[212579   2694]
     [ 50408   3294]]
    ```

*Conclusion*: Despite applying class weighting, the Random Forest model still
 struggled significantly with recall for the default class (only 6%),
  indicating it remained biased towards the majority class. It was very strong
   at predicting non-defaults but failed to detect most actual defaulters.

#### XGBoost (with `scale_pos_weight`)

* **Accuracy**: 0.65
* **Precision (Class 1)**: 0.32
* **Recall (Class 1)**: 0.67
* **F1-score (Class 1)**: 0.44
* **ROC AUC Score**: 0.723
* **Confusion Matrix**:

    ```bash
    [[139796  75477]
     [ 17555  36147]]
    ```

*Conclusion*: XGBoost, with `scale_pos_weight`, matched Logistic Regression in
 achieving high recall (67%) for defaults. It also demonstrated a slightly
  better ROC AUC score (0.723), suggesting superior overall class separation
   compared to Logistic Regression after balancing.

### 4.3.3 Hyperparameter Tuning (XGBoost)

Further optimization was performed on the XGBoost model using hyperparameter
 tuning to enhance its performance. Both GridSearchCV and RandomizedSearchCV
  were utilized.

#### GridSearchCV Best Parameters

```json
{
    'learning_rate': 0.1,
    'max_depth': 5,
    'n_estimators': 100,
    'scale_pos_weight': 4.008668246379308
}
```

* `learning_rate=0.1`: Controls the step size shrinkage to prevent overfitting.
* `max_depth=5`: Limits the depth of each tree, balancing complexity and performance.
* `n_estimators=100`: Number of boosting rounds (trees).
* `scale_pos_weight=4.01`: Addresses class imbalance by giving more weight to
 the minority class.

#### Performance Metrics on Test Set (after GridSearchCV tuning)

* **Accuracy**: 65%
* **Precision (Class 1)**: 32%
* **Recall (Class 1)**: 68% (Good, caught 68% of actual defaulters)
* **F1-score (Class 1)**: 43%
* **ROC AUC Score**: 0.647

#### Confusion Matrix (after GridSearchCV tuning)

```bash
  ------------ ---------------------- -------------------
               Predicted No Default   Predicted Default
  Actual No    137,919 (TN)           77,354 (FP)
  Actual Yes   17,321 (FN)            36,381 (TP)
  ------------ ---------------------- -------------------
```

* **True Positives (TP)**: 36,381 (Correctly caught defaulters)
* **False Positives (FP)**: 77,354 (Wrongly marked as default)
* **False Negatives (FN)**: 17,321 (Missed defaults)

*Key Takeaway*: The tuned XGBoost model achieved high recall (68%) for
 defaults, which is crucial for risk prediction, but at the cost of higher
 false positives.

#### RandomizedSearchCV Best Parameters

```json
{
    'colsample_bytree': 0.6923,
    'learning_rate': 0.0823,
    'max_depth': 6,
    'n_estimators': 298,
    'subsample': 0.8440
}
```

* `colsample_bytree=0.69`: Uses ~69% of features per tree to prevent overfitting.
* `learning_rate=0.082`: Slower, more precise learning.
* `max_depth=6`: Allows trees to grow deeper, balancing complexity.
* `n_estimators=298`: More trees in the ensemble for better accuracy.
* `subsample=0.84`: Uses 84% of training samples per tree to reduce overfitting.

*Best Score (AUC)*: 0.7219

*Conclusion*: RandomizedSearchCV yielded an XGBoost model with an AUC of 0.
7219, indicating a strong ability to distinguish between defaults an
 non-defaults, performing significantly better than random guessing.

## 4.4 Key Takeaways and Conclusion

### Key Takeaways

* **High Recall for Defaults**: Both Logistic Regression and XGBoost, after
 applying class balancing techniques, achieved high recall (around 67-68%) on
  the default class. This is critical for credit risk prediction, where
   identifying potential defaulters is paramount.
* **Trade-off with False Positives**: The improved recall often came with a
 trade-off: an increase in false positives (i.e., borrowers wrongly flagged as
  risky). This is a common challenge in imbalanced classification problems.
* **Random Forest's Performance**: Even with class weighting, Random Forest
   struggled to effectively detect the minority class, performing exceptionally
    well on the majority class but failing to identify most actual defaulters.
* **XGBoost as the Best Performer**: XGBoost consistently demonstrated the best
   overall performance, particularly in terms of ROC AUC score (up to 0.723
   after balancing and 0.7219 after RandomizedSearchCV tuning). This indicates
    its superior ability to distinguish between defaulting and non-defaulting loans.

### Conclusion

In the context of P2P lending default prediction, where the cost of missing a
 defaulter (false negative) is typically higher than wrongly flagging a
  non-defaulter (false positive), models with high recall for the default class
   are preferred. After comprehensive analysis and hyperparameter tuning, the
    **XGBoost model** emerged as the most effective solution. Its ability to
     achieve a high recall for the default class while maintaining a strong ROC
      AUC score makes it a robust choice for identifying and mitigating credit
 risk in P2P lending platforms. While a balance between precision and recall is
  always sought, the emphasis on recall for this specific problem makes XGBoost
   and, to a lesser extent, Logistic Regression, more suitable than Random
    Forest for this application.

## 4.5 Visualizations

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
