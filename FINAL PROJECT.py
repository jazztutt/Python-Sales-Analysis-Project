import csv

def read_data():
    data=[]

    with open('Sales.csv','r')as sales_file:
        monthly_sales= csv.DictReader(sales_file)
        for rows in monthly_sales:
            data.append(rows)

    return data

def run():
    data = read_data()

    sales=[]
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

        total = sum(sales)
        by_month = (row['month'])
        by_year = (row['year'])

    print('Total Sales {} {}: {}'.format(by_month, by_year, total))

run()







