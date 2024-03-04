from datetime import timedelta
from icecream import ic
from helper_auto_loan import caclulate_final_payoff_date
from functions import prompt_user, auto_set_prompt
"""from ultilities import (
    principal, interest_rate, loan_start_date, loan_term_years, 
    payment_periods, original_payoff_date,
    one_time_payment, one_time_payment_month,
    extra_monthly_payment, extra_payment_month,
     addl_extra_payment, addl_extra_payment_month
)"""


def calculate_auto_loan():
    
    # Get user inputs
    #loan_data = prompt_user() #! Disable for auto prompting (in development)
    loan_data = auto_set_prompt()
    
    
    #for data in loan_data:
    #    print(loan_data[data])

    # Calculate payoff date with all extra payments
    total_loan_cost, months_to_payoff, cumulative_interest, last_payment_amount = caclulate_final_payoff_date(loan_data)
    # Calculate payoff date from total months to payoff
    payoff_date = loan_data["Loan Start Date"] + timedelta(days=months_to_payoff * 30)

    

    # Calculate payoff date without extra payments
    original_payoff_date = loan_data["Loan Start Date"] + timedelta(days=(loan_data["Loan Term Years"]*12) * 30)

    # Build printable strings for dates
    original_payoff_date_str = original_payoff_date.strftime("%Y-%m-%d")
    final_payoff_date_str = payoff_date.strftime("%Y-%m-%d")

    # Display results
    print(f"Total Loan Cost (Including Interest): ${total_loan_cost:.2f}")
    print(f"Total Interest Paid: ${cumulative_interest:.2f}")
    print(f"Original Payoff Date: {original_payoff_date_str}")
    print(f"Actual Payoff Date: {final_payoff_date_str}")
    print(f"Last Payment Amount: ${last_payment_amount:.2f}")
    print(f"Actual Months to Payoff: {months_to_payoff}")


if __name__ == "__main__":
    calculate_auto_loan()
