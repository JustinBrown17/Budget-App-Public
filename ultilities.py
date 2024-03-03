from datetime import datetime, timedelta
from functions import get_float_input, get_date_input, diff_month

# Get user inputs
"""
principal = get_float_input("Enter the loan amount (principal): ")
interest_rate = get_float_input("Enter the annual interest rate (as a decimal): ")
loan_term_years = int(input("Enter the loan term (in years): "))
one_time_payment = get_float_input("Enter any one-time extra payment (if applicable): ")
extra_monthly_payment = get_float_input("Enter the recurring extra payment (monthly, quarterly, or yearly): ")
extra_monthly_payment_start_date = get_date_input("Enter the start date for extra payments (YYYY-MM-DD): ")
start_date = get_date_input("Enter the start date of the loan (YYYY-MM-DD): ")
"""

# Auto inputs (for development)
principal = 14441
interest_rate = 0.0418
loan_term_years = 6
one_time_payment = 0
one_time_payment_date = datetime.strptime("2022-03-20", "%Y-%m-%d")
extra_monthly_payment = 33
extra_monthly_payment_start_date = datetime.strptime("2022-02-20", "%Y-%m-%d")
start_date = datetime.strptime("2022-01-20", "%Y-%m-%d")
addl_extra_payment = 0#40
addl_extra_payment += extra_monthly_payment
addl_extra_payment_start_date = datetime.strptime("2024-03-20", "%Y-%m-%d")

#TODO push to amortization
payment_periods = loan_term_years * 12
monthly_interest_rate = interest_rate / 12

# Calculate payoff date without extra payments
original_payoff_date = start_date + timedelta(days=payment_periods * 30)



#! Get time deltas for extra payments and add'l payments (in months)
extra_payment_month = diff_month(extra_monthly_payment_start_date, start_date)
addl_extra_payment_month = diff_month(addl_extra_payment_start_date, start_date)
one_time_payment_month = diff_month(one_time_payment_date, start_date)

#print("end of set variables")

