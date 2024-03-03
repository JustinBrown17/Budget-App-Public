from datetime import datetime, timedelta
from icecream import ic
from amortization.amount import calculate_amortization_amount
#from amortization.period import calculate_amortization_period
#from amortization.schedule import amortization_schedule
from tabulate import tabulate
from ultilities import principal, interest_rate, loan_term_years, one_time_payment, extra_monthly_payment, extra_monthly_payment_start_date, start_date, addl_extra_payment, addl_extra_payment_start_date, extra_payment_month, addl_extra_payment_month, payment_periods

# initialize variables
payments_per_year = 12
total_num_of_payment = 0



def caclulate_final_payoff_date(principal, interest_rate, payment_periods, extra_monthly_payment, extra_payment_month, addl_extra_payment, addl_extra_payment_month):
    
    # initialize variables
    months = 0
    total_cost = 0
    cumulative_interest = 0

    table = (x for x in amortization_schedule2(principal, interest_rate, payment_periods))
    print(
        tabulate(
            table,
            headers=["Number", "Amount", "Interest", "Principal", "Balance"],
            floatfmt=",.2f",
            numalign="right"
        )
    )

    for number, amount, interest, principal, balance in amortization_schedule2(principal, interest_rate, payment_periods):
        total_cost += amount
        cumulative_interest += interest
        months = number

        # Update for last payment (overwrites until for loop ends, retrieving the last payment amount)
        last_payment_amount = amount
    
    
    
    
    
    
    """ # Iterate through the schedule and accumulate interest
    for row in table:
        # Extract the interest value from the row
        interest = row["Interest"]
        
        # Accumulate the interest
        cumulative_interest += interest
        print(interest)

        cost = row['Amount']
        total_cost += cost
        
        number = row['Number']
        print(number)
        # Print the row (you can customize this part as needed)
        #print(f"Number: {row['Number']}, Amount: {row['Amount']:.2f}, Interest: {interest:.2f}, Principal: {row['Principal']:.2f}, Balance: {row['Balance']:.2f}")

    # Print the total cumulative interest
    print(f"Total Cumulative Interest Paid: {cumulative_interest:.2f}")"""


    """
    print(
        tabulate(
            table,
            headers=["Number", "Amount", "Interest", "Principal", "Balance"],
            floatfmt=",.2f",
            numalign="right"
        )
    )
    """
    #ic(round(total_cost,2))
    
    return total_cost, months, cumulative_interest, last_payment_amount
    
    




def get_monthly_payment(balance, interest_rate, period, addl_payment):
    
    amortization_amount = calculate_amortization_amount(balance, interest_rate, 72)
    #ic('before operations', balance, interest_rate, period, addl_payment, amortization_amount)
    principal = balance
    interest_rate /= 12
    interest = balance * interest_rate
    principal = amortization_amount - interest
    balance = balance - (principal + addl_payment)
    #ic('after operations', principal, balance, interest_rate, interest, period, addl_payment, amortization_amount)
    #ic(amortization_amount, balance)

    
    return round(amortization_amount, 2), round(balance, 2)

# TODO: add onetime payment
def amortization_schedule2(principal, interest_rate, period):

    # Get amortization
    amortization_amount = calculate_amortization_amount(principal, interest_rate, period)
    
    # Start month counter
    number = 1

    # Get monthly interest rate
    interest_rate /= 12

    # Replaceable variable for principal
    balance = principal

    # Loop through months calculating each months payment
    while balance !=0: #number <= period

        # Get interest payment for month
        interest = balance * interest_rate

        # Get principal payment for month
        principal_payment = amortization_amount - interest

        # Get add'l payment amount
        addl_payment = find_addl_payment_amount(number)

        # Calculate payment, with and without interest
        #payment = principal_payment + addl_payment
        full_payment = (principal_payment + addl_payment) + interest

        # Subtract principal payment from remaining principal balance
        balance = balance - (principal_payment + addl_payment)

        if balance < 0:
            full_payment = full_payment + balance
            principal_payment = full_payment - interest
            balance = 0
            

        yield number, round(full_payment, 2), round(interest, 2), round(principal_payment, 2), round(balance, 2) if balance > 0 else 0
        number += 1   





def find_addl_payment_amount(months):

    # Straight payment
    if months <= extra_payment_month:
        #print("straight payment")
        addl_payment = 0
        return addl_payment

    # Payment with extra_payments
    elif months <= addl_extra_payment_month:
        #print("extra payments")
        addl_payment = extra_monthly_payment
        return addl_payment
    
    # Payment with Add'l extra payments
    else:
        #print("addl payment")
        addl_payment = addl_extra_payment
        return addl_payment