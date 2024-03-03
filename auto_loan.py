from datetime import timedelta
from icecream import ic
from helper_auto_loan import caclulate_final_payoff_date
from ultilities import (
    principal, interest_rate, start_date, loan_term_years, 
    payment_periods, original_payoff_date,
    one_time_payment, one_time_payment_month,
    extra_monthly_payment, extra_payment_month,
     addl_extra_payment, addl_extra_payment_month
)


def calculate_auto_loan():
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

    
    # Calculate payoff date with all extra payments
    total_loan_cost, months_to_payoff, cumulative_interest, last_payment_amount = caclulate_final_payoff_date(principal, interest_rate, payment_periods, extra_monthly_payment, extra_payment_month, addl_extra_payment, addl_extra_payment_month)
    
    # Calculate payoff date from total months to payoff
    payoff_date = start_date + timedelta(days=months_to_payoff * 30)

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
