from oauth2client.service_account import ServiceAccountCredentials
import gspread
from dotenv import load_dotenv
import os

def setup_gspread_client():
    """
    Sets up and returns a gspread client for interacting with Google Sheets.
    
    This function reads the Google service account credentials from an environment
    variable and uses them to authenticate with the Google Sheets API via the gspread library.
    
    Returns:
    An authorized gspread client object that can be used to perform operations on Google Sheets.
    """
    
    print("Setting up gspread client...")
    
    # Load environment variables from .env file, which should include the path to the
    # Google service account credentials file.
    load_dotenv()
    print(".env file loaded.")

    # Retrieve the path to the credentials JSON file from an environment variable.
    # This environment variable should be set to the file path of the service account
    # JSON file that contains the Google Cloud credentials.
    creds_json_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if not creds_json_path:
        print("Error: GOOGLE_APPLICATION_CREDENTIALS not found in environment variables.")

    # Define the scope of the authorization, which indicates what services the
    # credentials should have access to. In this case, the scope allows for
    # reading from and writing to Google Sheets.
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    print("Scope defined.")

    # Create a credentials object from the credentials JSON file path and the scope.
    # This object will be used to authenticate the gspread client.
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_json_path, scope)
        print("Credentials object created.")
    except Exception as e:
        print(f"Error creating credentials object: {e}")

    # Authorize the gspread client with the credentials object, which allows
    # the client to interact with the Google Sheets API.
    try:
        gspread_client = gspread.authorize(creds)
        print("Gspread client authorized.")
    except Exception as e:
        print(f"Error authorizing gspread client: {e}")

    # Return the authorized gspread client.
    return gspread_client
