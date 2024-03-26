from datetime import timedelta
from dateutil.relativedelta import relativedelta
from icecream import ic
from helper_auto_loan import caclulate_final_payoff_date
from functions import prompt_user, auto_set_prompt


def calculate_auto_loan():
    
    # Get user inputs
    loan_data = prompt_user() #! Disable for auto prompting (in development)
    #loan_data = auto_set_prompt()
    
    
    #for data in loan_data:
    #    print(loan_data[data])

    # Calculate payoff date with all extra payments
    total_loan_cost, months_to_payoff, cumulative_interest, last_payment_amount, payoff_date = caclulate_final_payoff_date(loan_data)
    
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
