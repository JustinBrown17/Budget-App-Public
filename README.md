# This file is meant to be implemented into a budget app for financial tracking #

## Currently in developement ##

- More information will be released as developement progresses!

----------------------------------------------------------------

## find_pay_info.py ##

Finds what paycheck # of the year was your first paycheck

References:

- Users pay frequency
- Month, Day and Year of the first paycheck
  - May remove year

Returns:

- Month of first paycheck
- How many months receiveing paychecks
- Paycheck number out of total yearly paychecks
- Total number of paycheck to be receive this year

Future adds?:

- Reference current date
- Return remaining paychecks for the year

----------------------------------------------------------------

## Transform_Excel_Script ##

Takes the current Excel budget and updates cell formulas

Uses:

Issue with dragging formulas in Excel?

- Now you can input your cell locations and logic
- File is adaptable to your specific use case

Current Use:

- For referencing the Income 1 location and determining if the month should be accounted for on the averages page
- Builds an Excel formula to check all months values, if they are valid, add them all together to get total spend thus far
