# from datetime import datetime, timedelta
# from tabulate import tabulate
from icecream import ic
from amortization.amount import calculate_amortization_amount
from pandas import DataFrame
from ultilities import time_deltas
from dateutil.relativedelta import relativedelta


def caclulate_final_payoff_date(loan_data):

    # Create variables
    principal = loan_data["Principal"]
    interest_rate = loan_data["Interest Rate"]
    loan_years = loan_data["Loan Term Years"]

    # Get total payments of loan
    payment_periods = loan_years * 12

    # Initialize variables
    total_cost = 0
    cumulative_interest = 0
    total_months = 0

    # Create a list for dicts
    amortization_table = []
    
    # Loop through loan until paid off
    for number, amount, interest_payment, principal_payment, balance in amortization_schedule2(principal, interest_rate, payment_periods, loan_data):
        
        date = loan_data["Loan Start Date"] + relativedelta(months = number)

        # Create a new dictionary for each iteration
        dict_structure = {
            #"Month": number,
            "Date": date,
            "Payment": amount,
            "Interest Payment": interest_payment,
            "Principal Payment": principal_payment,
            "Remaining Balance": balance
        }

        # Keep track of total interest
        cumulative_interest += interest_payment

        # Append payment info to end of list
        amortization_table.append(dict_structure)

    # Payoff date
    payoff_date = date

    # Get total payment months
    total_months = number

    # Create table of payments
    print(DataFrame(amortization_table))

    # Get total length of loan as last month
    #total_months = amortization_table[-1]["Month"]

    # Get last payment
    last_payment_amount = amortization_table[-1]["Payment"]

    # Calculate total payment with interest
    total_cost =  principal + cumulative_interest
    
    return total_cost, total_months, cumulative_interest, last_payment_amount, payoff_date
    

# TODO: add onetime payment
def amortization_schedule2(principal, interest_rate, period, loan_data):

    # Get amortization
    amortization_amount = calculate_amortization_amount(principal, interest_rate, period)
    
    # Start month counter
    number = 1

    # Get monthly interest rate
    interest_rate /= 12

    # Replaceable variable for principal
    balance = principal

    # Loop through months calculating each months payment
    while balance != 0:

        # Get interest payment for month
        interest = balance * interest_rate

        # Get principal payment for month
        principal_payment = amortization_amount - interest

        # Get add'l payment amount
        addl_payment = find_addl_payment_amount(number, loan_data)

        # Calculate actual payment (inculding additional payments and interest)
        full_payment = (principal_payment + addl_payment) + interest
        
        # Calculate actual principal payment including additional principal payment
        principal_payment = principal_payment + addl_payment

        # Calculate remaining balance
        balance = balance - principal_payment

        

        # Check balance can be paid off
        if full_payment + balance <= loan_data["Last Payment Amount"]:
            full_payment = balance + (full_payment - interest)
            principal_payment = full_payment
            interest = 0
            balance = 0
        
        # Balance was over paid (last month), return a 0 balance with reduced last payment
        elif balance < 0:
            full_payment = full_payment + balance
            #principal_payment = full_payment - interest
            balance = 0

        

        yield number, round(full_payment, 2), round(interest, 2), round(principal_payment, 2), round(balance, 2) if balance > 0 else 0
        number += 1   


def find_addl_payment_amount(current_month, loan_data):

    # Get time deltas
    extra_payment_month, addl_extra_payment_month, one_time_payment_month, one_time_payment2_month = time_deltas(loan_data)

    # Set addl_payment to 0
    addl_payment = 0
    
    # TODO: figure out why we need this -1
    # One time Payment
    if one_time_payment_month == current_month -1:
        addl_payment = loan_data["One Time Payment Amount"]

    if one_time_payment2_month == current_month -1:
        addl_payment = loan_data["Second One Time Payment Amount"]

    # Straight payment
    if current_month <= extra_payment_month:
        return addl_payment

    # Payment with extra_payments
    elif current_month <= addl_extra_payment_month:
        addl_payment += loan_data["Extra Payment Amount"]
        return addl_payment
    
    # Payment with extra payments and Add'l extra payments
    else:
        addl_payment += loan_data["Extra Payment Amount"]
        addl_payment += loan_data["Additional Extra Payment Amount"]
        return addl_payment