# Importing libraries
import pandas as pd
import plotly.express as px


def fraud_summary(csv_path="data/sample.csv"):
    df = pd.read_csv(csv_path)
    total_claims = len(df)
    flagged = df[df["flag"] == "Suspicious"].shape[0]
    fig = px.pie(df, names="flag", title="Fraudulent vs Legitimate Claims")
    return {"total_claims": total_claims, "flagged": flagged}, fig

def predict_fraud(amount, claim_type):
    base_risk = 0.4 if claim_type == "auto" else 0.3
    score = base_risk + (amount / 100000)
    label = "Suspicious" if score > 0.6 else "OK"
    return score, label
