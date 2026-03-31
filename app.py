import streamlit as st
import pandas as pd
from data_generator import generate_data
from reconciliation import reconcile
from anomaly_detector import detect_anomalies
from ai_explainer import generate_explanation

st.title("💳 AI Payment Reconciliation System")

# Generate Data
transactions, settlements = generate_data()

st.subheader("Transactions")
st.dataframe(transactions)

st.subheader("Settlements")
st.dataframe(settlements)

# Reconcile
merged = reconcile(transactions, settlements)

st.subheader("Merged Data")
st.dataframe(merged)

# Detect Issues
issues = detect_anomalies(merged)

st.subheader("🚨 Detected Issues Summary")

summary = {}
for key, value in issues.items():
    count = len(value)
    summary[key] = count
    st.write(f"{key}: {count}")

# AI Explanation
if st.button("Explain with AI"):
    explanation = generate_explanation(summary)
    st.write(explanation)