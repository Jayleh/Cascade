import csv
import os
import time
import pandas as pd
import pygsheets


def update():
    # Read exported csv file and write to new csv file
    path = r'D:\Cellese Unleashed Cascade\SalesEnquiryList.csv'

    with open(path, 'r', encoding='utf-8', errors='ignore') as infile, open('SalesReport.csv', 'w') as outfile:
        inputs = csv.reader(infile)
        output = csv.writer(outfile)

        for index, row in enumerate(inputs):
            # Create file with no header
            if index == 0:
                continue
            output.writerow(row)

    # Read new csv and set to dataframe
    df = pd.read_csv('SalesReport.csv')

    # Rename columns
    df = df.rename(columns={'Sub Total': 'Sales'})
    df.Sales = df.Sales.str.replace(',', '')
    df.Quantity = df.Quantity.str.replace(',', '')
    df.Sales = df.Sales.astype('float64')
    df.Sales = df.Sales.round(2)
    df.Quantity = df.Quantity.astype('float64')
    df.Quantity = df.Quantity.round(2)

    # Delete rows
    status = ['Deleted', 'Totals']
    df = df[~df['Status'].isin(status)]

    # Format dates to datetime and sort rows by date
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Completed Date'] = pd.to_datetime(df['Completed Date'])
    df = df.sort_values(by='Order Date')

    # Format dates to strings with strftime
    df['Order Date'] = df['Order Date'].dt.strftime('%m/%d')
    df['Completed Date'] = df['Completed Date'].dt.strftime('%m/%d')

    # Set credentials and designate sheet id
    creds = r'D:\Cellese Unleashed Cascade\cascadeSource\googleDriveAPI\client_secret_serviceKey.json'
    sheet_id = '****'

    # Open google sheet and then worksheet
    client = pygsheets.authorize(service_file=creds)
    sheet = client.open_by_key(sheet_id).sheet1

    # Update the first sheet with df, starting at cell B2.
    sheet.set_dataframe(df, 'A1')

    # Wait
    time.sleep(10)

    # Delete csv files
    os.remove('SalesEnquiryList.csv')
    os.remove('SalesReport.csv')

    # Check transfer
    data = sheet.get_all_records()
    print(data)


if __name__ == '__main__':
    update()
