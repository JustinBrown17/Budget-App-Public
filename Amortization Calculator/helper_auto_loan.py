# from datetime import datetime, timedelta
# from tabulate import tabulate
from icecream import ic
from amortization.amount import calculate_amortization_amount
from pandas import DataFrame
from ultilities import time_deltas


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

    # Create a list for dicts
    amortization_table = []
    
    # Loop through loan until paid off
    for number, amount, interest_payment, principal_payment, balance in amortization_schedule2(principal, interest_rate, payment_periods, loan_data):
        
        # Create a new dictionary for each iteration
        dict_structure = {
            "Month": number,
            "Payment": amount,
            "Interest Payment": interest_payment,
            "Principal Payment": principal_payment,
            "Remaining Balance": balance
        }

        # Keep track of total interest
        cumulative_interest += interest_payment

        # Append payment info to end of list
        amortization_table.append(dict_structure)

    # Create table of payments
    print(DataFrame(amortization_table))

    # Get total lenght of loan
    total_months = amortization_table[-1]["Month"]

    # Get last payment
    last_payment_amount = amortization_table[-1]["Payment"]

    # Calculate total payment with interest
    total_cost =  principal + cumulative_interest
    
    return total_cost, total_months, cumulative_interest, last_payment_amount
    

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

        # Calculate payment, with and without interest
        full_payment = (principal_payment + addl_payment) + interest

        # Subtract principal payment from remaining principal balance
        balance = balance - (principal_payment + addl_payment)

        # Balance was over paid (last month), return a 0 balance with reduced last payment
        if balance < 0:
            full_payment = full_payment + balance
            principal_payment = full_payment - interest
            balance = 0
            

        yield number, round(full_payment, 2), round(interest, 2), round(principal_payment, 2), round(balance, 2) if balance > 0 else 0
        number += 1   


def find_addl_payment_amount(current_month, loan_data):

    # Get time deltas
    extra_payment_month, addl_extra_payment_month, one_time_payment_month = time_deltas(loan_data)

    # Set addl_payment to 0
    addl_payment = 0

    # TODO: figure out why we need this -1
    # One time Payment
    if one_time_payment_month == current_month -1:
        addl_payment = loan_data["One Time Payment Amount"]

    # Straight payment
    if current_month <= extra_payment_month:
        return addl_payment

    # Payment with extra_payments
    elif current_month <= addl_extra_payment_month:
        addl_payment += loan_data["Extra Payment Amount"]
        return addl_payment
    
    # Payment with Add'l extra payments
    else:
        addl_payment += loan_data["Additional Extra Payment Amount"]
        return addl_payment
    






"""# Build table and print to console
table = (x for x in amortization_schedule2(principal, interest_rate, payment_periods))
print(
    tabulate(
        table,
        headers=["Number", "Amount", "Interest", "Principal", "Balance"],
        floatfmt=",.2f",
        numalign="right"
    )
)
# TODO: refactor this code
# Loop through table to calculate total_cost and cumulative_interest
for number, amount, interest, principal, balance in amortization_schedule2(principal, interest_rate, payment_periods):
    total_cost += amount
    cumulative_interest += interest
    months = number

    # Update for last payment (overwrites until for loop ends, retrieving the last payment amount)
    last_payment_amount = amount"""