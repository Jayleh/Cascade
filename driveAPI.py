from __future__ import print_function
import os
import time
import httplib2

from apiclient import discovery
from googleapiclient.http import MediaFileUpload
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.file'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Cascade'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'Cascade.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def upload():
    # authorize
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    drive_service = discovery.build('drive', 'v3', http=http)

    # Rename CSV file with date and time
    timestr = time.strftime("%Y%m%d-%H%M%S")
    old_file = os.path.join(
        r"D:\Cellese Unleashed Cascade", "SalesEnquiryList.csv")
    new_filename = "SalesEnquiryList " + timestr + ".csv"
    new_file = os.path.join(
        r"D:\Cellese Unleashed Cascade\Sales Enquiries", new_filename)
    os.rename(old_file, new_file)

    # Upload CSV file to drive
    os.chdir(r"D:\Cellese Unleashed Cascade")

    folder_id = "1JUpm6FzLF5ebIT-uY-UfrsFtj9z6ilYG"
    file_metadata = {
        'name': new_filename,
        'mimeType': 'application/vnd.google-apps.spreadsheet',
        'parents': [folder_id]
    }
    media = MediaFileUpload(new_file,
                            mimetype='text/csv',
                            resumable=True)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    if file:
        print('File ID: %s' % file.get('id'))


if __name__ == '__main__':
    upload()
