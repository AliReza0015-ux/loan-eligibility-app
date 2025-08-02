#  Loan Eligibility Prediction App

This Streamlit web application predicts **loan eligibility** based on basic applicant information using a trained machine learning model.

---

##  Demo

 **Live App**: [https://loan-eligibility-app.streamlit.app](https://loan-eligibility-app.streamlit.app)

---

##  Project Structure

```bash
loan-eligibility-app/
│
├── app.py                  # Streamlit app entry point
├── model.py                # Contains model loading and prediction logic
├── utils.py                # Input preprocessing helper
├── credit.csv              # Sample input dataset
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── model/
    └── loan_model.pkl      # Trained machine learning model
________________________________________
Features
•	User authentication (simple login)
•	Interactive form to collect applicant data
•	Real-time prediction of loan eligibility
•	Robust error handling and data validation
________________________________________
 Built With
•	Python 3.10
•	Streamlit
•	Scikit-learn
•	Pandas
•	Cloudpickle
________________________________________
How to Run Locally
1.	Clone the repository:
2.	git clone https://github.com/AliReza0015-ux/loan-eligibility-app.git
3.	cd loan-eligibility-app
4.	Create a virtual environment:
5.	python -m venv env
6.	source env/bin/activate  # On Windows: env\Scripts\activate
7.	Install dependencies:
8.	pip install -r requirements.txt
9.	Run the app:
10.	streamlit run app.py
________________________________________
Author
•	Ali Reza Mohseni
•	CST2216 | Business Intelligence System Infrastructure | Algonquin College
________________________________________
 License
This project is for academic use only.
