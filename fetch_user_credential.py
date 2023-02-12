import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CLIENT_SECRET_FILE = 'client_secret.json'

# This OAuth 2.0 access scope allows for read-only access to the authenticated
# user's account, but not other types of account access.
SCOPES = [
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.force-ssl',
]
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


# Authorize the request and store authorization credentials.
def fetch_user_credential(arg_credential):
    if not arg_credential:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        credentials = flow.run_local_server()
        return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    else:
        credential_file_name = 'credentials/%s.pickle' % arg_credential
        loaded_credential = fetch_user_credential_with_file(credential_file_name)
        return build(API_SERVICE_NAME, API_VERSION, credentials=loaded_credential)


def fetch_user_credential_with_file(credential_file_name):
    loaded_credential = None
    if os.path.isfile(credential_file_name):
        with open(credential_file_name, 'rb') as credential_file:
            loaded_credential = pickle.load(credential_file)
    if not loaded_credential or not loaded_credential.valid:
        if loaded_credential and loaded_credential.expired and loaded_credential.refresh_token:
            loaded_credential.refresh(Request())
            return loaded_credential
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            credentials = flow.run_local_server()
            with open(credential_file_name, 'wb') as credential_file:
                pickle.dump(credentials, credential_file)
            return credentials
    else:
        return loaded_credential
