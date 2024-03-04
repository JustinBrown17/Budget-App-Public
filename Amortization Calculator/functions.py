from datetime import datetime


def get_float_input(prompt):
    """
    This function validates a user input of a float

    Returns:
    float: User input as a float
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def get_date_input(prompt):
    """
    This function validates user input of a date

    Returns:
    date: User input as a datetime
    """
    while True:
        try:
            date_str = input(prompt)
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def diff_month(d1, d2):
    """
    This function calculates the difference between two dates in months

    Returns:
    int: The difference
    """
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def prompt_user():
    """
    This function prompts the user with all necessary data for calculation of the loan

    Returns:
    dict: With all the user data inputs
    """
    user_data = {}

    # Get loan info
    principal = get_float_input("Enter the loan amount (principal): ")
    interest_rate = get_float_input("Enter the annual interest rate (as a decimal): ")
    loan_term_years = int(input("Enter the loan term (in years): "))
    loan_start_date = get_date_input("Enter the start date of the loan (YYYY-MM-DD): ")

    # Get one time payment info
    one_time_payment = get_float_input("Enter any one-time extra payment (if applicable): ")

    # If user did not make a one time payment do not ask them the date
    if one_time_payment != 0:
        one_time_payment_date = get_date_input("Enter the start date for one time payment (YYYY-MM-DD): ")
    else: 
        one_time_payment_date = loan_start_date
    

    # Get extra payment info
    extra_monthly_payment = get_float_input("Enter the recurring extra payment (monthly, quarterly, or yearly): ")

    if extra_monthly_payment != 0:
        extra_monthly_payment_start_date = get_date_input("Enter the start date for extra payments (YYYY-MM-DD): ")
    else: 
        extra_monthly_payment_start_date = loan_start_date
    

    # Get additional payment info
    addl_extra_payment = get_float_input("Enter the later date additional payment (if applicable): ")
    
    if addl_extra_payment != 0:
        addl_extra_payment_start_date = get_date_input("Enter the start date for the additional extra payments (YYYY-MM-DD): ")
    else:
        addl_extra_payment_start_date = loan_start_date

    # Adjust, adding original extra payment to make more sense to user
    addl_extra_payment += extra_monthly_payment

    # Collect user data into dict
    user_data = {
        "Principal" : principal,
        "Interest Rate" : interest_rate,
        "Loan Term Years" : loan_term_years,
        "Loan Start Date" : loan_start_date,
        "One Time Payment Amount" : one_time_payment,
        "One Time Payement Date" : one_time_payment_date,
        "Extra Payment Amount" : extra_monthly_payment,
        "Extra Payment Start Date" : extra_monthly_payment_start_date,
        "Additional Extra Payment Amount" : addl_extra_payment,
        "Additional Extra Payment Start Date" : addl_extra_payment_start_date
    }
    
    return user_data

def auto_set_prompt():
    """
    #! FOR DEVELOPMENT USE ONLY
    This function sets the user prompts automatically for developer use

    Returns:
    dict: With all the 'user' data inputs 
    """

    # Set user data automatically
    user_data = {
                              "Principal" : 14441,
                          "Interest Rate" : 0.0418,
                        "Loan Term Years" : 6,
                        "Loan Start Date" : datetime.strptime("2022-01-20", "%Y-%m-%d"),
                "One Time Payment Amount" : 1000,
                 "One Time Payement Date" : datetime.strptime("2024-03-20", "%Y-%m-%d"),
                   "Extra Payment Amount" : 33,
               "Extra Payment Start Date" : datetime.strptime("2022-02-20", "%Y-%m-%d"),
        "Additional Extra Payment Amount" : 40+33,
    "Additional Extra Payment Start Date" : datetime.strptime("2024-03-20", "%Y-%m-%d"),
    }

    return user_data