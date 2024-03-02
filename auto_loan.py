from datetime import datetime, timedelta

def calculate_auto_loan():
    # Get user inputs
    loan_amount = float(input("Enter the loan amount (principal): "))
    interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
    loan_term_years = int(input("Enter the loan term (in years): "))
    one_time_payment = float(input("Enter any one-time extra payment (if applicable): "))
    extra_payment = float(input("Enter the recurring extra payment (monthly, quarterly, or yearly): "))
    extra_payment_start_date = input("Enter the start date for extra payments (YYYY-MM-DD): ")
    start_date = input("Enter the start date of the loan (YYYY-MM-DD): ")

    # Convert interest rate to monthly rate
    monthly_interest_rate = interest_rate / 12

    # Calculate total number of periods (months)
    num_periods = loan_term_years * 12

    # Calculate monthly payment
    numerator = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** num_periods
    denominator = (1 + monthly_interest_rate) ** num_periods - 1
    monthly_payment = numerator / denominator

    # Calculate total payment with extras
    total_payment = monthly_payment + one_time_payment + extra_payment

    # Calculate payoff date without extra payments
    original_payoff_date = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=num_periods * 30)
    original_payoff_date_str = original_payoff_date.strftime("%Y-%m-%d")

    # Calculate payoff date with all extra payments
    extra_periods = int((extra_payment_start_date - datetime.strptime(start_date, "%Y-%m-%d")).days / 30)
    total_periods = num_periods + extra_periods
    final_payoff_date = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=total_periods * 30)
    final_payoff_date_str = final_payoff_date.strftime("%Y-%m-%d")

    # Display results
    print(f"\nMonthly Payment: ${monthly_payment:.2f}")
    print(f"Total Payment (including extras): ${total_payment:.2f}")
    print(f"Original Payoff Date (without extras): {original_payoff_date_str}")
    print(f"Payoff Date (with all extras): {final_payoff_date_str}")

if __name__ == "__main__":
    calculate_auto_loan()