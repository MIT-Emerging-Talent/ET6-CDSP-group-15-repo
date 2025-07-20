# Domain Study: Peer-to-Peer (P2P) Lending Risk

This document outlines our foundational research into the domain of Peer-to-Peer
(P2P) lending and the critical challenge of modeling loan default risk. It also
provides an overview of the contents of this folder.

## Folder Contents

This `0_domain_study` folder is organized to document our research process and
findings.

- **`README.md` (This File):** Provides a high-level summary of our research
  domain, the evolution of our research question, and the overall folder
  structure.
- **`guide.md`:** Offers a detailed orientation to the folder's contents,
  explaining the purpose of each file and sub-directory.
- **`research_questions/`:** Contains the history of our research questions.
  - `old/`: Documents our initial research on "Buy Now, Pay Later" (BNPL).
  - `new/`: Details our current, refined research questions on P2P lending.
- **`sources/`:** Lists the data and literature that support our research.
  - `old/`: Contains sources related to our initial BNPL research.
  - `new/`: Contains sources for our current P2P lending research.

## Evolution of Our Research

Our initial research focused on the risks associated with "Buy Now, Pay Later"
(BNPL) services. However, due to the limited availability of public datasets
required to rigorously investigate our initial questions, we pivoted our
research.

Our new focus is on **Peer-to-Peer (P2P) lending**, a domain with rich, publicly
available data that allows for robust modeling and analysis of credit risk.

## The P2P Lending Landscape

Peer-to-Peer (P2P) lending platforms have emerged as a significant alternative
to traditional banking, connecting individual borrowers with investors directly.
These platforms offer greater access to credit for borrowers and potentially
higher returns for investors. However, the decentralized nature of P2P lending
introduces unique challenges in assessing borrower creditworthiness and
predicting the likelihood of default, which is crucial for sustainable growth
and investor confidence.

## Problem Statement

While P2P platforms provide extensive data on loans and borrowers, accurately
predicting which loans will default remains a complex problem. Investors face
the risk of capital loss due to insufficient or ineffective risk assessment
models. Therefore, there is a critical need to develop robust predictive models
that can identify the key drivers of default risk, enabling investors to make
more informed decisions and platforms to refine their underwriting standards.

## Research Question

_What are the key borrower and loan characteristics that best predict default
risk in peer-to-peer (P2P) lending platforms in the United States?_

### Secondary Questions

1. Which machine learning approaches most accurately model default risk in P2P
   lending data?
2. How do features such as credit grade, interest rate, debt-to-income ratio,
   income, loan term, and loan purpose contribute to risk prediction?
3. How do default risk patterns change across time, different regions, or
   borrower segments?
4. In what ways can advanced risk modeling support investor decisions and
   improve P2P platform underwriting?

## Key Focus Areas

Our research is structured around three core areas:

- **Technical Focus**: We will concentrate on advanced data cleaning, feature
  engineering, and benchmarking machine learning models (Logistic Regression,
  Random Forest, XGBoost). We will also use explainability techniques like SHAP
  to interpret model predictions.
- **Business Focus**: The insights from our models will be framed to improve
  loan pricing, enhance underwriting processes, and develop actionable risk
  management tools for investors.
- **User Focus**: We aim to identify risk signals across different borrower
  types and investigate factors related to financial health, while ensuring
  fairness in risk assessment.

## Methodology and Dataset

Our study will utilize a quantitative approach, applying machine learning
techniques to a large-scale dataset.

### Dataset

The primary dataset for this research is the **Lending Club Loan Data** from
Kaggle, which contains comprehensive information on loans issued in the U.S.

### Modeling Approach

We will employ a systems thinking lens to understand the interconnected factors
influencing default risk. Our modeling process will involve:

- **Data Preparation**: Cleaning and preparing the Lending Club dataset.
- **Model Training**: Building and training predictive models.
- **Evaluation**: Assessing model performance using metrics like AUC-ROC.
- **Interpretation**: Using SHAP to understand the key features driving
  predictions.

This structured approach will ensure our findings are both statistically robust
and practically applicable for investors and P2P platforms.
