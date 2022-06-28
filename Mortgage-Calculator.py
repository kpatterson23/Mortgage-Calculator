import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

home_price = float(input("Enter sales price of home in USD $: "))

down_payment = float(input("Enter down payment amount as a percentage of sales price, e.g. 10 for 10%: "))

loan_amount = home_price * (1 - down_payment / 100)

mortgage_type = float(input("Enter mortgage length in years, e.g. 30 for 30 years: "))

loan_term = int(12 * mortgage_type)

interest_rate = float(input("Enter loan interest rate as a percentage, 10 for 10%: "))

R = 1 +(interest_rate) / (12 * 100)

X = loan_amount*(R**loan_term)*(1-R) / (1-R**loan_term)

monthly_interest = []
monthly_balance = []

for i in range(1, loan_term + 1):
    interest = loan_amount * (R-1)
    loan_amount = loan_amount - (X - interest)
    monthly_interest = np.append(monthly_interest, interest)
    monthly_balance = np.append(monthly_balance, loan_amount)
    
print("The Home Sales Price is: = " + str("$") + str(home_price))
print("The Down Payment as a Percentage of Sales Price is: " + str(down_payment) + str(" %"))
print("The Loan Amount is: = " + str(home_price* (1-down_payment / 100)) + str(" %"))
print("The Interest Rate on Annual Percentage Basis is: = " + str(interest_rate) + str(" %"))
print("The duration of this loan, that is the Loan Term (in months) is: = " + str(loan_term) + str(" months"))
print("Monthly Payment for this Mortgage(P & I) is: = " + str("$") + str(np.round(X, 2)))
print("Total interest paid over life cycle of the loan is: = " + str("$") + str(np.round(np.sum(monthly_interest), 2)))

plt.plot(range(1, loan_term + 1), monthly_interest, 'r', lw=2)
plt.xlabel('month')
plt.ylabel('monthly interest ($)')
plt.show()

plt.plot(range(1, loan_term + 1), monthly_balance, 'b', lw=2)
plt.xlabel('month')
plt.ylabel('monthly loan balance ($)')
plt.show()