import csv
import os
import time
import pandas as pd
import pygsheets


def update():
    # read csv file
    path = r'D:\Cellese Unleashed Cascade\SalesEnquiryList.csv'

    with open(path, 'r', encoding='utf-8', errors='ignore') as infile, open('SalesReport.csv', 'w') as outfile:
        inputs = csv.reader(infile)
        output = csv.writer(outfile)

        for index, row in enumerate(inputs):
            # Create file with no header
            if index == 0:
                continue
            output.writerow(row)

    df = pd.read_csv('SalesReport.csv')
    creds = r'D:\Cellese Unleashed Cascade\cascadeSource\googleDriveAPI\client_secret_serviceKey.json'
    sheet_id = '****'

    # Open google sheet and then worksheet
    client = pygsheets.authorize(service_file=creds)
    sheet = client.open_by_key(sheet_id).sheet1

    # update the first sheet with df, starting at cell B2.
    sheet.set_dataframe(df, 'A1')

    # wait
    time.sleep(10)

    # delete csv files
    os.remove('SalesEnquiryList.csv')
    os.remove('SalesReport.csv')

    # check transfer
    data = sheet.get_all_records()
    print(data)


if __name__ == '__main__':
    update()
