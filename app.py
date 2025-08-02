import streamlit as st
import pandas as pd
from model import load_model, predict_eligibility
from utils import preprocess_input

# ---- USER AUTH ----
def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if username == "admin" and password == "1234":
        return True
    elif username and password:
        st.sidebar.error("Invalid credentials.")
        return False
    else:
        return False

# ---- MAIN APP ----
def main():
    st.set_page_config(page_title="Loan Eligibility Predictor", layout="centered")
    st.title("🏦 Loan Eligibility Prediction")

    if not login():
        st.stop()

    st.subheader("Enter Applicant Information")

    try:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        applicant_income = st.number_input("Applicant Income", min_value=0)
        loan_amount = st.number_input("Loan Amount", min_value=0)

        if st.button("Predict"):
            # Show input preview
            input_df = preprocess_input(gender, married, education, applicant_income, loan_amount)
            st.write("🔍 Input Preview:", input_df)

            # Load model
            model = load_model()
            st.write("📦 Model Loaded:", type(model).__name__)

            # Predict
            result = predict_eligibility(model, input_df)
            st.success(f"🎯 Loan Eligibility: {result}")
    except Exception as e:
        st.error(f"❌ Something went wrong: {e}")

if __name__ == '__main__':
    main()
