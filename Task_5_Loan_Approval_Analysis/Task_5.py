# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode

import warnings
warnings.filterwarnings('ignore')

path = "./loan_prediction.csv"
user_data_dir = "."

#Reading file
bank_data = pd.read_csv(path)

#Code starts here
categorical_var = bank_data.select_dtypes(include = "object")
print(categorical_var)

numerical_var = bank_data.select_dtypes(include = "number")
print(numerical_var)

#Step 2
banks = bank_data.drop(columns=["Loan_ID"])
print(banks.isnull().sum())
banks_mode = banks.mode()
banks = banks.fillna(banks_mode)

#Step 3
avg_loan_amount = pd.pivot_table(banks, index=["Gender", "Married", "Self_Employed"],values="LoanAmount",aggfunc='mean')

#Step 4
loan_approved_se = banks[(banks["Self_Employed"] == "Yes") & (banks["Loan_Status"] == "Y")].count()
loan_approved_nse = banks[(banks["Self_Employed"] == "No") & (banks["Loan_Status"] == "Y")].count()
percentage_se = loan_approved_se /100
percentage_nse = loan_approved_nse /100


#Step 5
loan_term = banks["Loan_Amount_Term"].apply(lambda x : x / 12)
big_loan_term = loan_term >= 25

#Step 6
loan_groupby = banks.groupby(["Loan_Status"])
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
