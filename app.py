import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("🏦 Bank Customer Risk Analyzer")

st.subheader("Enter Customer Details")

# ---------------- INPUTS ----------------
creditscore = st.number_input("Credit Score", 300, 900, 650)
age = st.number_input("Age", 18, 100, 35)
tenure = st.slider("Tenure (Years)", 0, 10, 3)
balance = st.number_input("Account Balance", 0.0, 500000.0, 50000.0)
num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
has_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
active = st.selectbox("Active Member?", ["Yes", "No"])
salary = st.number_input("Estimated Salary", 0.0, 300000.0, 60000.0)

geo = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])
card_type = st.selectbox("Card Type", ["Silver", "Gold", "Platinum"])
complain = st.selectbox("Any Complaint?", ["Yes", "No"])
satisfaction = st.slider("Satisfaction Score", 1, 10, 5)
points = st.number_input("Points Earned", 0, 10000, 500)

# ---------------- LOGIC ----------------
if st.button("Analyze Customer Risk"):

    risk_score = 0

    if creditscore < 600: risk_score += 2
    if age > 45: risk_score += 1
    if balance < 10000: risk_score += 2
    if active == "No": risk_score += 2
    if complain == "Yes": risk_score += 2
    if satisfaction < 5: risk_score += 1

    if risk_score >= 6:
        verdict = "🔴 High Churn Risk"
    elif risk_score >= 3:
        verdict = "🟠 Medium Churn Risk"
    else:
        verdict = "🟢 Low Churn Risk"

    # ---------------- OUTPUT ----------------
    st.subheader("📊 Customer Risk Result")
    st.success(verdict)

    st.write("### Insight Summary")
    st.write(f"""
    • Risk Score: **{risk_score}**  
    • Engagement Status: **{active}**  
    • Complaint History: **{complain}**  
    • Satisfaction Level: **{satisfaction}/10**  
    """)

    if verdict.startswith("🔴"):
        st.error("Immediate retention action recommended.")
    elif verdict.startswith("🟠"):
        st.warning("Targeted engagement can reduce churn.")
    else:
        st.info("Customer is stable. Maintain experience.")
