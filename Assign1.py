'''Arjun Atwal
This code takes a year of interest from the user, then using the current and past year expenses 
calculates the user's inflation rate and determines the type of inflation using the inflation rate'''


year = input('Input the year that you want to calculate the personal interest rate for: ')
categories = int(input('Input the number of expenditure categories: '))
previous_year_expense = 0
year_of_interest_expense = 0
total_expenses_previous_year = 0
total_expenses_year_of_interest = 0

for i in range(categories):
    previous_year_expense = float(input('Enter expenses for previous year: '))
    year_of_interest_expense = float(input('Enter expenses for year of interest: '))

    total_expenses_previous_year = total_expenses_previous_year + previous_year_expense
    total_expenses_year_of_interest = total_expenses_year_of_interest + year_of_interest_expense

inflation_rate = (total_expenses_year_of_interest - total_expenses_previous_year)/total_expenses_year_of_interest

if inflation_rate < 0.03:
    type_of_inflation = 'Low'
elif inflation_rate >= 0.03 and inflation_rate < 0.05:
    type_of_inflation = 'Moderate'
elif inflation_rate > 0.05 and inflation_rate < 0.1:
    type_of_inflation = 'High'
else:
    type_of_inflation = 'Hyper'


print('Personal inflation rate for',year,'is',inflation_rate*100,'%')
print('Type of inflation:',type_of_inflation)

