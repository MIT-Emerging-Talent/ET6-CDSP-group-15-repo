import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import xgboost as xgb
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split

# --- Import SHAP for model interpretability ---
# This will be used in Phase 5.
try:
    import shap
except ImportError:
    print("SHAP library not found. Please install it using: pip install shap")
    shap = None


def run_p2p_lending_analysis(filepath):
    """
    This function runs the complete P2P lending analysis workflow on a pre-cleaned dataset.
    It loads the data, generates EDA plots, trains a model, evaluates it, and interprets it with SHAP.
    """

    # --- Phase 1: Load Pre-Cleaned Data ---
    print("--- Phase 1: Loading Pre-Cleaned Data ---")

    try:
        df = pd.read_csv(filepath, low_memory=False)
        print("Successfully loaded pre-cleaned data.")
    except FileNotFoundError:
        print(f"FATAL ERROR: The file '{filepath}' was not found.")
        return

    # --- Critical Column Check ---
    if "is_default" not in df.columns:
        print(
            "\nFATAL ERROR: The required target column 'is_default' was not found in the dataset."
        )
        print(
            "This script expects a pre-cleaned file where the target variable is already created."
        )
        return

    # --- Phase 2: Exploratory Data Analysis (EDA) on available features ---
    print("\n--- Phase 2: Generating and Saving EDA Visualizations ---")

    if not os.path.exists("eda_plots"):
        os.makedirs("eda_plots")

    sns.set_style("whitegrid")
    sns.set_palette("viridis")

    # Plot 1: Target Variable Distribution
    plt.figure(figsize=(8, 6))
    ax = sns.countplot(x="is_default", data=df)
    plt.title("Distribution of Loan Outcomes (Class Imbalance)", fontsize=16)
    plt.xticks([0, 1], ["Fully Paid (0)", "Defaulted (1)"])
    total = len(df)
    for p in ax.patches:
        percentage = f"{(p.get_height() / total) * 100:.1f}%"
        x = p.get_x() + p.get_width() / 2
        y = p.get_height()
        ax.annotate(percentage, (x, y), ha="center", va="bottom", fontsize=12)
    plt.savefig("eda_plots/01_target_distribution.png")
    plt.close()

    # Plot 2: Numerical Feature Distributions
    numerical_features_to_plot = ["int_rate", "fico_range_low", "loan_amnt"]
    existing_numerical = [
        col for col in numerical_features_to_plot if col in df.columns
    ]

    if existing_numerical:
        fig, axes = plt.subplots(
            1, len(existing_numerical), figsize=(7 * len(existing_numerical), 6)
        )
        fig.suptitle("Distribution of Key Characteristics", fontsize=18)
        if len(existing_numerical) == 1:
            axes = [axes]
        for i, col in enumerate(existing_numerical):
            sns.histplot(df[col], kde=True, bins=30, ax=axes[i])
            axes[i].set_title(col)
        plt.savefig("eda_plots/02_numerical_distributions.png")
        plt.close()

    # Plot 3: [NEW] Correlation of Loan Grades with Default
    grade_cols = [col for col in df.columns if col.startswith("grade_")]
    if grade_cols:
        grade_corr = df[grade_cols + ["is_default"]].corr()["is_default"].sort_values()
        grade_corr = grade_corr.drop("is_default")  # Exclude the target itself
        plt.figure(figsize=(10, 6))
        sns.barplot(x=grade_corr.values, y=grade_corr.index, palette="viridis")
        plt.title("Correlation of Loan Grade with Default Status", fontsize=16)
        plt.xlabel("Correlation with Default", fontsize=12)
        plt.ylabel("Loan Grade", fontsize=12)
        plt.savefig("eda_plots/03_grade_correlation.png")
        plt.close()

    # Plot 4: [NEW] Correlation of Top States with Default
    state_cols = [col for col in df.columns if col.startswith("addr_state_")]
    if state_cols:
        state_corr = df[state_cols + ["is_default"]].corr()["is_default"].sort_values()
        state_corr = state_corr.drop("is_default")

        # Combine top positive and top negative correlations for a focused view
        top_and_bottom_states = pd.concat([state_corr.head(10), state_corr.tail(10)])

        plt.figure(figsize=(12, 10))
        sns.barplot(
            x=top_and_bottom_states.values,
            y=top_and_bottom_states.index,
            palette="coolwarm_r",
        )
        plt.title(
            "Correlation of Top/Bottom 10 States with Default Status", fontsize=16
        )
        plt.xlabel("Correlation with Default", fontsize=12)
        plt.ylabel("State", fontsize=12)
        plt.savefig("eda_plots/04_state_correlation.png")
        plt.close()

    # Plot 5: Correlation Matrix
    plt.figure(figsize=(18, 14))
    corr_cols = [
        col
        for col in df.columns
        if not col.startswith(("addr_state_", "purpose_", "home_"))
    ][:25]
    corr_matrix = df[corr_cols].corr(numeric_only=True)
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Matrix of Key Numerical Features (Subset)", fontsize=16)
    plt.savefig("eda_plots/05_correlation_matrix.png")
    plt.close()

    print("Phase 2: EDA plots saved in the 'eda_plots' directory.")

    # --- Phase 3 & 4: Modeling and Evaluation ---
    print("\n--- Phase 3 & 4: Starting Model Training and Evaluation ---")

    df_model = df.copy()

    X = df_model.drop("is_default", axis=1)
    y = df_model["is_default"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scale_pos_weight = y_train.value_counts()[0] / y_train.value_counts()[1]
    print(f"Calculated scale_pos_weight: {scale_pos_weight:.2f}")

    xgb_classifier = xgb.XGBClassifier(
        objective="binary:logistic",
        eval_metric="logloss",
        scale_pos_weight=scale_pos_weight,
        use_label_encoder=False,
        random_state=42,
    )
    print("Training XGBoost model...")
    xgb_classifier.fit(X_train, y_train)
    print("Training complete.")

    y_pred = xgb_classifier.predict(X_test)
    y_pred_proba = xgb_classifier.predict_proba(X_test)[:, 1]

    print("\n--- Model Evaluation Results ---")
    print("\nClassification Report:")
    print(
        classification_report(y_test, y_pred, target_names=["Fully Paid", "Defaulted"])
    )

    auc_score = roc_auc_score(y_test, y_pred_proba)
    print(f"\nArea Under the ROC Curve (AUC): {auc_score:.4f}")

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Predicted: Fully Paid", "Predicted: Defaulted"],
        yticklabels=["Actual: Fully Paid", "Actual: Defaulted"],
    )
    plt.title("Confusion Matrix", fontsize=16)
    plt.savefig("eda_plots/06_confusion_matrix.png")
    plt.close()
    print("Confusion matrix plot saved to 'eda_plots/06_confusion_matrix.png'")

    # --- Phase 5: Model Interpretation with SHAP ---
    if shap:
        print("\n--- Phase 5: Interpreting Model with SHAP ---")

        explainer = shap.TreeExplainer(xgb_classifier)
        X_test_sample = X_test.sample(n=2000, random_state=42)
        shap_values = explainer.shap_values(X_test_sample)

        print("Generating SHAP summary plot...")
        plt.figure()
        shap.summary_plot(shap_values, X_test_sample, show=False)
        plt.title("SHAP Summary Plot: Global Feature Importance", fontsize=16)
        plt.tight_layout()
        plt.savefig("eda_plots/07_shap_summary_plot.png")
        plt.close()
        print("SHAP summary plot saved to 'eda_plots/07_shap_summary_plot.png'")

        print("Generating SHAP force plot for a single prediction...")
        force_plot = shap.force_plot(
            explainer.expected_value,
            shap_values[0, :],
            X_test_sample.iloc[0, :],
            matplotlib=False,
        )
        shap.save_html("eda_plots/08_shap_force_plot.html", force_plot)
        print("SHAP force plot saved to 'eda_plots/08_shap_force_plot.html'")

    print("\nAnalysis finished successfully.")


# --- Main execution block ---
if __name__ == "__main__":
    dataset_path = "loan.csv"

    if os.path.exists(dataset_path):
        run_p2p_lending_analysis(dataset_path)
    else:
        print(f"FATAL ERROR: The file '{dataset_path}' was not found.")
        print(
            "Please download the dataset and place it in the same directory as this script."
        )
