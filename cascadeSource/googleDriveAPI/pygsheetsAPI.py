import os
import time
import sys
import pandas as pd
import pygsheets

# Change sys path
sys.path.insert(0, 'cascadeSource/googleDriveAPI/creds/')
from sheet_keys import tsheet_id, gsheet_id


def update():
    # Set complete sales csv path
    complete_sales_path = 'SalesEnquiries/NewSalesReport.csv'

    # Read csv and set as dataframe
    complete_sales_df = pd.read_csv(complete_sales_path, encoding='utf-8')

    # Set credentials and designate sheet id
    creds = 'cascadeSource/googleDriveAPI/creds/client_secret_serviceKey.json'
    tabDash_sheet_id = tsheet_id
    gDash_sheet_id = gsheet_id

    # Open google sheet and then worksheet
    client = pygsheets.authorize(service_file=creds)
    tab_sheet = client.open_by_key(tabDash_sheet_id).sheet1
    g_sheet = client.open_by_key(gDash_sheet_id).sheet1

    # Clear worksheet
    g_sheet.clear()

    # Update the first sheet with df, starting at cell B2.
    tab_sheet.set_dataframe(complete_sales_df, 'A1')
    g_sheet.set_dataframe(complete_sales_df, 'A1')

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
