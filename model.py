import cloudpickle

def load_model(path="model/loan_model.pkl"):
    with open(path, "rb") as f:
        return cloudpickle.load(f)

def predict_eligibility(model, input_df):
    return model.predict(input_df)[0]
