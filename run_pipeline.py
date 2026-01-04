import pandas as pd
import joblib
import numpy as np

from src.preprocessing.encode_features import encode_and_scale
from src.preprocessing.split_data import split
from src.modeling.pd_model import train_pd_model, save_model
from src.modeling.evaluate_model import evaluate
from src.modeling.scorecard import pd_to_score
from src.decisioning.risk_segmentation import segment
from src.decisioning.decision_rules import decision
from src.explainability.shap_explainer import shap_global
from src.explainability.lime_explainer import lime_instance

#  Load cleaned data
df = pd.read_csv("data/processed/credit_default_clean.csv")

#  Encode & scale
X_scaled, y, scaler = encode_and_scale(df)

#  Train-test split
X_train, X_test, y_train, y_test = split(X_scaled, y)

#  Train PD model
model = train_pd_model(X_train, y_train)
save_model(model)

#  Evaluate model
auc = evaluate(model, X_test, y_test)
print(f"ROC-AUC: {auc:.3f}")

#  PD → Score → Risk → Decision
pd_values = model.predict_proba(X_test)[:, 1]
scores = pd_to_score(pd_values)

risk_levels = [segment(s) for s in scores]
decisions = [decision(r) for r in risk_levels]

#  Save final decisions
output_df = pd.DataFrame({
    "PD": pd_values,
    "Score": scores,
    "Risk": risk_levels,
    "Decision": decisions
})

output_df.to_csv("outputs/decisions/loan_decisions.csv", index=False)

# 8. Explainability
shap_global(model, X_train)
lime_instance(model, X_train, X_test[0])

print("Pipeline completed successfully.")
