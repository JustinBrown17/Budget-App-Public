from datetime import datetime
# TODO: finish 2nd ont-time payment logic
# TODO: finish and fully implement the "monthly" payment into a payment that could be weekly, bi-weekly or monthly

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
    This function prompts the user for all necessary data to calculate the loan.

    Returns:
        dict: A dictionary containing all the user input data.
    """
    # TODO: add frequency into user_data
    # TODO: add more payments??

    # Initialize an empty dictionary to store user data
    user_data = {}

    # Get loan information
    user_data["Principal"] = get_float_input("Enter the loan amount (principal): ")
    user_data["Interest Rate"] = get_float_input("Enter the annual interest rate (as a decimal): ")
    user_data["Loan Term Years"] = int(input("Enter the loan term (in years): "))
    user_data["Loan Start Date"] = get_date_input("Enter the start date of the loan (YYYY-MM-DD): ")
    # TODO: do i need this?   vvv
    #user_data["Payment Frequency"] = int(input("Enter the loan payment frequency : "))

    # Get one-time payment information
    user_data["One Time Payment Amount"] = get_float_input("Enter one-time extra payment (if applicable): ")

    # If there is a one-time payment, get the date and check for a second one-time payment
    if user_data["One Time Payment Amount"] != 0:
        user_data["One Time Payment Date"] = get_date_input("Enter the date for one-time payment (YYYY-MM-DD): ")
        user_data["Second One Time Payment Amount"] = get_float_input("Enter 2nd one-time extra payment (if applicable): ")
        
        # If there is a second one-time payment, get its date
        if user_data["Second One Time Payment Amount"] != 0:
            user_data["Second One Time Payment Date"] = get_date_input("Enter the date for 2nd one-time payment (YYYY-MM-DD): ")

    # If no one-time payments are made, set the dates to the loan start date
    else:
        user_data["One Time Payment Date"] = user_data["Loan Start Date"]
        user_data["Second One Time Payment Amount"] = 0
        user_data["Second One Time Payment Date"] = user_data["Loan Start Date"]

    # Get recurring extra payment information
    user_data["Extra Payment Amount"] = get_float_input("Enter the recurring extra payment: ")

    # If there is a recurring extra payment, get its start date
    if user_data["Extra Payment Amount"] != 0:
        # TODO: add this back in  vvv
        #user_data["Extra Payment Frequency"] = int(input("Enter the extra payment frequency (12 = Monthly, 26 = bi-weekly, 52 = weekly): "))
        user_data["Extra Payment Start Date"] = get_date_input("Enter the start date for extra payments (YYYY-MM-DD): ")
    else:
        user_data["Extra Payment Start Date"] = user_data["Loan Start Date"]

    # Get additional extra payment information
    user_data["Additional Extra Payment Amount"] = get_float_input("Enter the later date additional payment (if applicable): ")

    # If there is an additional extra payment, get its start date
    if user_data["Additional Extra Payment Amount"] != 0:
        user_data["Additional Extra Payment Start Date"] = get_date_input("Enter the start date for the additional extra payments (YYYY-MM-DD): ")
    else:
        user_data["Additional Extra Payment Start Date"] = user_data["Loan Start Date"]

    # Get the last payment amount
    user_data["Last Payment Amount"] = get_float_input("Enter the increased last payment amount (if desired): ")

    return user_data



def auto_set_prompt():
    """
    #! FOR DEVELOPMENT USE ONLY
    This function sets the user prompts automatically, for rapid development use

    Returns:
    dict: With all the 'user' data inputs 
    """

    # Set user data automatically
    user_data = {
                              "Principal" : 14441,
                          "Interest Rate" : 0.0418,
                        "Loan Term Years" : 6,
                        "Loan Start Date" : datetime.strptime("2022-01-20", "%Y-%m-%d"),
                "One Time Payment Amount" : 3000,
                 "One Time Payement Date" : datetime.strptime("2024-05-20", "%Y-%m-%d"),
         "Second One Time Payment Amount" : 1500,
          "Second One Time Payment Date"  : datetime.strptime("2024-11-20", "%Y-%m-%d"),
                   "Extra Payment Amount" : 33,
               "Extra Payment Start Date" : datetime.strptime("2022-02-20", "%Y-%m-%d"),
        "Additional Extra Payment Amount" : 0,
    "Additional Extra Payment Start Date" : datetime.strptime("2024-03-20", "%Y-%m-%d"),
                    "Last Payment Amount" : 1600, # Desired last payment
    }

    return user_data