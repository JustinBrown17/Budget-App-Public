from functions import diff_month


def time_deltas(loan_data):

    # Extract data from loan data
    extra_monthly_payment_start_date = loan_data["Extra Payment Start Date"]
    loan_start_date = loan_data["Loan Start Date"]
    addl_extra_payment_start_date = loan_data["Additional Extra Payment Start Date"]
    one_time_payment_date = loan_data["One Time Payment Date"]
    one_time_payment2_date = loan_data["Second One Time Payment Date"]

    #Get time deltas for extra payments and add'l payments (in months)
    extra_payment_month = diff_month(extra_monthly_payment_start_date, loan_start_date)
    addl_extra_payment_month = diff_month(addl_extra_payment_start_date, loan_start_date)
    one_time_payment_month = diff_month(one_time_payment_date, loan_start_date)
    one_time_payment2_month = diff_month(one_time_payment2_date, loan_start_date)
    
    return extra_payment_month, addl_extra_payment_month, one_time_payment_month, one_time_payment2_month


