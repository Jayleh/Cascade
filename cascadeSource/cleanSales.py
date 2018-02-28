import csv
import time
import pandas as pd


def cleanSales():
    # Read exported csv file and write to new csv file
    file_path = 'SalesEnquiries/SalesEnquiryList.csv'

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile, \
            open('SalesEnquiries/SalesReport.csv', 'w') as outfile:

        inputs = csv.reader(infile)
        output = csv.writer(outfile)

        for index, row in enumerate(inputs):
            # Create file with no header
            if index == 0:
                continue
            output.writerow(row)

    # Set sales path
    sales_path = 'SalesEnquiries/SalesReport.csv'

    # Read sales csv
    sales_df = pd.read_csv(sales_path)

    # Delete deleted, parked, placed, backordered, d totals rows
    status = ['Deleted', 'Parked', 'Placed', 'Backordered', 'Totals']
    complete_sales_df = sales_df[~sales_df['Status'].isin(status)]

    # Rename sub total column
    complete_sales_df = complete_sales_df.rename(columns={'Sub Total': 'Sales'})

    # Drop commas in number strings
    complete_sales_df['Quantity'] = complete_sales_df['Quantity'].str.replace(',', '')
    complete_sales_df['Sales'] = complete_sales_df['Sales'].str.replace(',', '')

    # Change number objects to numeric
    complete_sales_df['Quantity'] = pd.to_numeric(complete_sales_df['Quantity']).round(2)
    complete_sales_df['Sales'] = pd.to_numeric(complete_sales_df['Sales']).round(2)

    # Format dates to datetime
    complete_sales_df['Order Date'] = pd.to_datetime(complete_sales_df['Order Date'])
    complete_sales_df['Completed Date'] = pd.to_datetime(complete_sales_df['Completed Date'])

    # Sort rows by date
    complete_sales_df = complete_sales_df.sort_values(by='Order Date')

    # Format dates with strftime
    complete_sales_df['Order Date'] = complete_sales_df['Order Date'].dt.strftime('%m/%d/%Y')
    complete_sales_df['Completed Date'] = complete_sales_df['Completed Date'].dt.strftime(
        '%m/%d/%Y')

    # Convert new dataframe into csv
    complete_sales_df.to_csv('SalesEnquiries/NewSalesReport.csv',
                             sep=',', index=False, encoding='utf-8')

    # Wait
    time.sleep(5)


if __name__ == '__main__':
    cleanSales()
