import csv

print('2018 Sales and Expenditure Analysis')
print()

# Code to read sales data from a csv file

def sales_data():

    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data

# Code to analyse sales data

def summary():

    data = sales_data()

    sales = []

    for column in data:
        sale = int(column['sales'])
        sales.append(sale)

    expenditure = []

    for column in data:
        expense = int(column['expenditure'])
        expenditure.append(expense)

    months = []

    for row in data:
        month = row ['month']
        months.append(month)


    total_sales = sum(sales)
    average_sales= round(sum(sales)/12)
    total_expense = sum(expenditure)
    average_expense = round(sum(expenditure)/12)

    highest_salesmonth = months[sales.index(max(sales))]
    highest_salesvalue = max(sales)
    lowest_salesmonth = months[sales.index(min(sales))]
    lowest_salesvalue = min(sales)

    highest_expendmonth = months[expenditure.index(max(expenditure))]
    highest_expendvalue = max(expenditure)
    lowest_expendmonth =  months[expenditure.index(min(expenditure))]
    lowest_expendvalue =  min(expenditure)


    print('Total Sales = £{}'.format(total_sales))
    print('Average Sales Per Month = £{}' .format(average_sales))
    print('Highest sales month: {} £{}'.format(highest_salesmonth,highest_salesvalue))
    print('Lowest sales month: {} £{}'.format(lowest_salesmonth,lowest_salesvalue))

    print()
    print('Total Expenditure = £{}'.format(total_expense))
    print('Average Expenditure Per Month = £{}'.format(average_expense))
    print('Highest Expenditure Month: {} £{}'.format(highest_expendmonth,highest_expendvalue))
    print('Lowest Expenditure Month: {} £{}'. format(lowest_expendmonth,lowest_expendvalue))

summary()

# Code to ask the user to input a month and receive sales data

def question():

    data = sales_data()

    sales = []

    for column in data:
        sale = int(column['sales'])
        sales.append(sale)

    expenditure = []

    for column in data:
        expense = int(column['expenditure'])
        expenditure.append(expense)

    months = []

    for row in data:
        month = row['month']
        months.append(month)


    while True:
        print()
        request = input('What month would you like sales data on?').capitalize()

        if request not in months:
            print('Invalid: Please check your spelling.')

        else:
            print('Total Sales {}: £'.format(request), (sales[months.index(request)]))
            print('Total Expenditure {}: £'.format(request), (expenditure[months.index(request)]))
            break

question()
