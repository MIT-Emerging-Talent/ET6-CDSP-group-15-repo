# 💰 DataCents: Decoding Financial Patterns

[![DataCents Finance Analytics](https://img.shields.io/badge/DataCents-Finance%20Analytics-2196F3?style=for-the-badge&logo=python&logoColor=white)](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-15-repo)
[![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com)

![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=40&pause=1000&color=2196F3&center=true&vCenter=true&width=600&height=100&lines=Welcome+to+DataCents!;Where+Data+Meets+Finance)

## About Our Team

**DataCents** is a collaborative research team using data science to decode  
credit risk in peer-to-peer (P2P) lending platforms.

We apply machine learning and interpretability tools to large-scale lending  
data to identify the strongest predictors of loan default. Our goal is to  
improve credit assessment, inform smarter lending decisions, and enhance  
investor confidence in the evolving alternative finance ecosystem.

---

### Our Mission

[![Project Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]
(<https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-15-repo>)

We are on a mission to:

- Build an open, data-driven framework for assessing default risk in P2P lending.
- Identify borrower and loan traits most predictive of default.  
- Apply interpretable machine learning to improve credit assessment.  
- Support investors, platforms, and regulators with transparent risk insights.  

## Research Aim

Our aim is to uncover the key drivers of default risk in P2P lending systems.
Using historical data from Lending Club, we analyze borrower behavior,
loan characteristics, and repayment outcomes to predict risk.  

We train models that balance accuracy with explainability, enabling decisions  
that are both data-backed and transparent. The ultimate goal is to build  
tools that help platforms and investors reduce risk and improve outcomes.

---

## Problem Statement

P2P platforms offer flexible credit access to millions, yet face  
a persistent challenge: borrower default. Unpaid loans hurt investors,  
threaten platform stability, and erode trust in digital finance.  

Conventional credit scoring may miss key behavioral signals. Many borrowers,  
especially younger users, accumulate invisible debt across platforms.  
Without reliable models, lenders can't detect risk early or fairly.  

By studying a large dataset of loan records and repayment history,  
we aim to reveal the hidden indicators of credit default risk  
and build interpretable models for real-world risk prediction.

### Research Question

What are the key borrower and loan characteristics that best predict  
default risk in peer-to-peer (P2P) lending platforms in the United States?

### 🔍 Modeling the Research Question

To address our research question, we analyze Lending Club data  
to identify the borrower and loan features that best predict default risk.

Our modeling approach includes the following stages:

- **Data Cleaning**: Filter loans with known outcomes, remove anomalies,  
  and handle missing values for consistent analysis.

- **Feature Engineering**: Create meaningful variables from raw data,  
  such as debt-to-income ratios, credit history flags, and loan grade scores.

- **Exploratory Analysis**: Visualize patterns of default by borrower  
  demographics, loan purpose, FICO ranges, and installment size.

- **Modeling Techniques**: Use classification models like  
  Logistic Regression, Random Forest, and XGBoost  
  to estimate default likelihood.

- **Interpretability Tools**: Apply SHAP analysis and feature importance  
  methods to explain model decisions and highlight key predictors.

- **Validation**: Evaluate models with train-test splits and performance metrics
  (AUC, accuracy, recall) to ensure generalizability and robustness.

---

## 📁 Datasets Used

All datasets are stored in our  
[`/1_datasets/`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-15-repo/tree/main/1_datasets)  
folder, with cleaning and prep scripts in  
[`/2_data_preparation/`](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-15-repo/tree/main/2_data_preparation).

The primary dataset used in our analysis is the Lending Club loan dataset,  
which includes over 2 million loans with borrower traits and repayment outcomes.

**Key dataset features include:**

- Borrower attributes: employment length, annual income, FICO scores  
- Loan details: loan amount, term, purpose, interest rate, installment amount  
- Credit history: earliest credit line, delinquencies, open accounts  
- Loan outcome: loan status (fully paid, charged-off, default)  

## 👥 Meet the Team

<!-- markdownlint-disable MD033 -->
<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/NoorelsalamAlmakki">
          <img src="https://avatars.githubusercontent.com/NoorelsalamAlmakki"
               width="150px;"
               alt="Noorelsalam Almakki"
               style="border-radius: 50%; border: 3px solid #2196F3;"/>
          <br/>
          <b>Noorelsalam Almakki</b>
        </a>
        <br/>
        <a href="https://github.com/NoorelsalamAlmakki">
          <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"
               alt="GitHub"/>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/MadiMalik">
          <img src="https://avatars.githubusercontent.com/MadiMalik"
               width="150px;"
               alt="Madiha Maikzada"
               style="border-radius: 50%; border: 3px solid #2196F3;"/>
          <br/>
          <b>Madiha Maikzada</b>
        </a>
        <br/>
        <a href="https://github.com/MadiMalik">
          <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"
               alt="GitHub"/>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/MyatCharm">
          <img src="https://avatars.githubusercontent.com/MyatCharm"
               width="150px;"
               alt="Myint Myat Zaw"
               style="border-radius: 50%; border: 3px solid #2196F3;"/>
          <br/>
          <b>Myint Myat Zaw</b>
        </a>
        <br/>
        <a href="https://github.com/MyatCharm">
          <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"
               alt="GitHub"/>
        </a>
      </td>
    </tr>
    <tr>
      <td align="center">
        <a href="https://github.com/AhmedKhalifa7">
          <img src="https://avatars.githubusercontent.com/AhmedKhalifa7"
               width="150px;"
               alt="Ahmed Hussein"
               style="border-radius: 50%; border: 3px solid #2196F3;"/>
          <br/>
          <b>Ahmed Hussein</b>
        </a>
        <br/>
        <a href="https://github.com/AhmedKhalifa7">
          <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"
               alt="GitHub"/>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/AlhassenSabeeh">
          <img src="https://avatars.githubusercontent.com/AlhassenSabeeh"
               width="150px;"
               alt="Al-Hassan Sabeeh"
               style="border-radius: 50%; border: 3px solid #2196F3;"/>
          <br/>
          <b>Al-Hassan Sabeeh</b>
        </a>
        <br/>
        <a href="https://github.com/AlhassenSabeeh">
          <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"
               alt="GitHub"/>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/dadishimwe">
          <img src="https://avatars.githubusercontent.com/dadishimwe"
               width="150px;"
               alt="Dadi Ishimwe"
               style="border-radius: 50%; border: 3px solid #2196F3;"/>
          <br/>
          <b>Dadi Ishimwe</b>
        </a>
        <br/>
        <a href="https://github.com/dadishimwe">
          <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"
               alt="GitHub"/>
        </a>
      </td>
    </tr>
  </table>
</div>
<!-- markdownlint-enable MD033 -->

## 🔍 Research Focus

Our project explores the intersection of behavioral finance and machine
learning,  
with a focus on peer-to-peer (P2P) credit risk prediction. We aim to:

- Identify key borrower and loan features linked to default outcomes  
- Build predictive models using Lending Club loan performance data  
- Analyze behavioral and demographic traits influencing credit risk  
- Apply feature importance tools to surface critical default indicators  
- Support fairer, data-driven credit assessment in alternative lending  

## 🛠️ Technical Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Scikit Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org)

## 📁 Project Structure

Our repository is organized into key sections:

- `/0_domain_study/` - Financial domain research and background
- `/1_datasets/` - Financial datasets and market data
- `/2_data_preparation/` - Data cleaning and preprocessing scripts
- `/3_data_exploration/` - Initial data analysis and visualization
- `/4_data_analysis/` - Advanced analysis and modeling
- `/5_communication_strategy/` - How we share our findings
- `/6_final_presentation/` - Final project presentation

## 🚀 Getting Started

1. Clone and setup

    ```bash
    # Clone the repository
    git clone https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-15-repo.git
    cd ET6-CDSP-group-15-repo

    # Create environment
    conda env create -f environment.yml
    conda activate datacents

    # Or install manually
    pip install -r requirements.txt
    ```

2. Start exploring

    ```bash
    # Launch Jupyter Notebook
    jupyter notebook
    ```

Navigate to the `4_data_analysis` directory to begin exploring our financial
data analysis.

## 📈 Project Progress

[![Progress](https://img.shields.io/badge/Progress-15%25-blue?style=for-the-badge)](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-15-repo)

## 📈 Key Findings

- Initial data analysis reveals promising patterns
- Machine learning models show high accuracy
- Market trends indicate significant opportunities

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for
guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
for details.

---

[![Quote](https://img.shields.io/badge/Quote-Finance%20%26%20Data-blue?style=for-the-badge)](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-15-repo)

> *"The goal is to turn data into information, and information into insight." -
> Carly Fiorina*

Join us as we make sense — and DataCents — out of information.
