# Credit Risk Modelling & Explainable AI for Loan Decisioning

## Project Overview
This project implements an end-to-end credit risk modelling pipeline to support loan approval decisions.  
The system estimates the Probability of Default (PD) for loan applicants, converts PD into interpretable credit scores, segments applicants into risk categories, and provides transparent explanations for decisions using Explainable AI (XAI).

The workflow mirrors real-world banking and fintech credit risk systems, with a strong focus on interpretability, governance, and business decisioning.

---

## Dataset
- Source: UCI Credit Card Default Dataset
- Target Variable: Default in the following month (binary)

### Feature Categories
- Demographics (age, gender, education, marital status)
- Credit limit information
- Repayment history (past 6 months)
- Bill amounts (past 6 months)
- Payment amounts (past 6 months)

Encoded variables are documented in a dedicated data dictionary to reflect real-world credit risk practices.

---

## Methodology

### 1. Data Preprocessing
- Removal of identifier fields
- Handling encoded categorical variables
- Feature scaling using standardization
- Stratified train-test split

### 2. Probability of Default (PD) Modelling
- Logistic Regression used for PD estimation
- Chosen for interpretability and regulatory acceptance
- PD derived from predicted probabilities

### 3. Model Evaluation
- ROC-AUC used as primary metric
- Achieved ROC-AUC ≈ 0.71
- ROC curve generated for diagnostics

### 4. Credit Scoring
- PD values transformed into credit scores using a log-odds-based scorecard formulation
- Higher PD corresponds to lower credit scores

### 5. Risk Segmentation & Decisioning
Applicants are segmented into:
- Low Risk → Approve
- Medium Risk → Manual Review
- High Risk → Reject

Rule-based logic ensures transparent and auditable decisions.

### 6. Explainable AI (XAI)
- SHAP used for global feature importance and portfolio-level explainability
- LIME used for instance-level explanations of individual loan decisions

These explanations support compliance, audits, and customer communication.


---

## Results
- ROC-AUC ≈ 0.71
- End-to-end generation of PDs, scores, risk categories, and decisions
- Transparent global and local model explanations



