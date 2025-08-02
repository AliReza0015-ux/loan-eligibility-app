import pandas as pd

def preprocess_input(gender, married, education, income, loan_amount):
    data = {
        'Gender': [gender],
        'Married': [married],
        'Education': [education],
        'ApplicantIncome': [income],
        'LoanAmount': [loan_amount]
    }
    df = pd.DataFrame(data)
    return df
