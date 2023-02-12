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
def fetch_user_credential():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_local_server()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
