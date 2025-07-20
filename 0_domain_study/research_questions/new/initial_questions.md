# Initial Research Questions

This document summarizes the initial exploratory research questions that
informed the early direction of our study into credit risk and default
prediction in U.S. peer-to-peer (P2P) lending.

## Main Questions

1. What are the key borrower and loan characteristics that best predict default
   risk in P2P lending platforms in the United States?
2. How effectively can machine learning models leverage these variables to
   predict loan defaults on P2P platforms?
3. Which modeling techniques and data engineering approaches yield the most
   robust and interpretable risk predictions?
4. How do macroeconomic, demographic, and geographic factors influence default
   risk patterns among P2P borrowers?

## Supporting Questions

### Technical

- Which data cleaning and feature engineering steps are critical for preparing
  P2P loan datasets?
- How do models such as logistic regression, random forest, and gradient
  boosting compare for default prediction?
- What role do explainability frameworks (e.g., SHAP, LIME) play in model
  transparency?

### Business

- How can P2P platforms enhance loan origination and pricing using predictive
  risk analytics?
- What characteristics should investors prioritize when selecting loans for
  their portfolios?

### User

- Which borrower demographics and financial behaviors most strongly correlate
  with default risk?
- What patterns emerge when examining default outcomes by borrower or loan
  attribute?

## Next Steps

- [ ] Obtain and preprocess the Lending Club dataset from Kaggle
- [ ] Perform exploratory data analysis (EDA) to identify predictive patterns
- [ ] Fit baseline and advanced machine learning models for risk prediction
- [ ] Analyze feature importance, refine models, and document findings
