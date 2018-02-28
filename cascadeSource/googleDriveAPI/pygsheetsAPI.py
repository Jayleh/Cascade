import os
import time
import pandas as pd
import pygsheets


def update():
    # Set complete sales csv path
    complete_sales_path = 'SalesEnquiries/NewSalesReport.csv'

    # Read csv and set as dataframe
    complete_sales_df = pd.read_csv(complete_sales_path, encoding='utf-8')

    # Set credentials and designate sheet id
    creds = 'cascadeSource/googleDriveAPI/config/client_secret_serviceKey.json'
    tabDash_sheet_id = ''
    gDash_sheet_id = ''

    # Open google sheet and then worksheet
    client = pygsheets.authorize(service_file=creds)
    tab_sheet = client.open_by_key(tabDash_sheet_id).sheet1
    goo_sheet = client.open_by_key(gDash_sheet_id).sheet1

    # Clear worksheet
    goo_sheet.clear()

    # Update the first sheet with df, starting at cell B2.
    tab_sheet.set_dataframe(complete_sales_df, 'A1')
    goo_sheet.set_dataframe(complete_sales_df, 'A1')

    # Wait
    time.sleep(10)

    # Delete csv files
    os.remove('SalesEnquiries/SalesEnquiryList.csv')
    os.remove('SalesEnquiries/SalesReport.csv')
    # os.remove('SalesEnquiries/NewSalesReport.csv')

    # Check transfer
    data = tab_sheet.get_all_records()
    print(data)


if __name__ == '__main__':
    update()
