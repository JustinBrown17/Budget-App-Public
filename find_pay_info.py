from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import sys

# find the pay number of the users first paycheck


def main():

    # get users first paycheck date + validate date:
    while True:
        try:
            FIRST_PAY_DATE = datetime.strptime(
                input("What was your first pay date? Use YYYY-MM-DD format "), "%Y-%m-%d")
            break
        except ValueError:
            print('invalid date: use YYYY-MM-DD',
                  '\n', 'Example: 2023-12-31 is valid')

    # get users pay frequency
    while True:
        try:
            PAY_FREQUENCY = int(input("How many pays in a year? "))
            if PAY_FREQUENCY == 12 or PAY_FREQUENCY == 24 or PAY_FREQUENCY == 26 or PAY_FREQUENCY == 52:
                break
            else:
                print(
                    'Not a valid pay schedule:', '\n',
                    'Use "12" for yearly', '\n',
                    'Use "24" for bi-monthly', '\n',
                    'Use "26" for bi-weekly', '\n',
                    'Use "52" for weekly'
                )
        except ValueError:
            print('not a number')

    # find days between paychecks
    time_shift = 7*(52/PAY_FREQUENCY)

    # bi_monthly = False
    # if paid bi-weekly or weekly
    if (time_shift % 7 == 0):
        delta = timedelta(days=time_shift)
    else:
        time_shift = (PAY_FREQUENCY/12)  # == pays per month

        # paid monthly
        if time_shift == 1:
            delta = relativedelta(months=1)
        # paid bi-monthly
        elif time_shift == 2:
            delta = timedelta(days=15)
            bi_monthly = True
        else:
            sys.exit('this is an invalid pay schedule')

    # initialize variables
    count = 0
    check_date = FIRST_PAY_DATE  # intialize date to check as user inputted date

    # if time delta causes year to roll back to previous year, funct will break
    while (True):

        # check date is valid and count as a pay
        if (check_date.year == FIRST_PAY_DATE.year):
            count += 1
        else:
            # last checked date was out of bounds

            # handle bi-monthly pays different
            if 'bi_monthly' in globals():
                # check pay amount didn't overflow into 25 / 24
                if FIRST_PAY_DATE.day < 16 and count != 0:
                    count -= 1
                # add 1 extra pay if first paydate was after the 15th
                elif FIRST_PAY_DATE.day >= 16 and count != PAY_FREQUENCY:
                    count += 1

                '''if count > PAY_FREQUENCY:
                    print('error: counter out of bounds')'''
            firstPayNum = count
            break

        check_date -= delta

    remaining_months_of_pay = 12 - (FIRST_PAY_DATE.month - 1)
    total_pays_of_year = PAY_FREQUENCY-(firstPayNum-1)

    # output useful data
    print('')  # seperate data from inputs

    print('{}{}'.format(
        'Month of first pay = ',
        FIRST_PAY_DATE.month
    ))
    print('{}{}'.format(
        'Months of the year paid = ',
        remaining_months_of_pay
    ))
    print('{}{}{}{}'.format(
        'Your first pay = #',
        firstPayNum,
        ' out of #',
        PAY_FREQUENCY
    ))
    print('{}{}{}{}'.format(
        'Total # of pays received in ',
        FIRST_PAY_DATE.year,
        ' = ',
        total_pays_of_year
    ))


# run main
if __name__ == "__main__":
    main()
