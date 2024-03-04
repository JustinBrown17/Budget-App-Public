# Transform Excel Script
from openpyxl import load_workbook

# Open Budget and select desired sheet
workbook = load_workbook('2024_budget--python_scripted.xlsx')
sheet = workbook['Averages']

# Cell to check if month is a completed month (if month is not completed, value == 0)
is_valid_month_cell = 'E11'

# Setup pointer locations to read into logic line
info_cell_letter = 'E'
info_cell_num = 11  
end_info_cell_num = 13

# Setup Excel formula
month_list = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
logic_line = '='

# Cursor cell thats updated
cursor_cell_letter = 'F'
cursor_cell_num = info_cell_num - 1 # Same column number

# While in range of cells to be updated
while info_cell_num <= end_info_cell_num:

    # Loop through all months
    for month in month_list:

        # Build info location where logic is read in Excel formula
        info_cell = f'{info_cell_letter}{info_cell_num}'

        # Build cursor location (where cell will be updated)
        cursor_cell = f'{cursor_cell_letter}{cursor_cell_num}'

        # Python example of what Excel logic does:
        '''
        if month-validator-cell != 0:
            total += month_cell_amount
        else:
            total += 0
        '''
        logic_line += (f'IF({month}!{is_valid_month_cell} <> 0, {month}!{info_cell}, 0) + ')

        # remove " + " from last entry
        if month == 'DEC':
            logic_line = logic_line[:-3]

            # At cursor paste full logic
            sheet[cursor_cell] = logic_line
            print(logic_line + '\n')
            # Reset logic
            logic_line = '='
    
    # Build next cells logic
    info_cell_num += 1
    cursor_cell_num += 1 # Move cursor


workbook.save('2024_budget--python_scripted.xlsx') #2024_budget--python_scripted.xlsx

print('Script Complete')