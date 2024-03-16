from dotenv import load_dotenv
import os
from utils.dynamic_import import dynamic_import
from utils.gspread_setup import setup_gspread_client

# Load environment variables
load_dotenv()
print("Environment variables loaded.")

def main():
    """
    Main function to orchestrate the processing of a range of rows in a Google Sheet.
    Each row corresponds to a task or a set of tasks defined by the user. Before using
    the program to generate data in your spread sheet, you should first have your columns
    titled to plan out your steps. It's best to have the first 2 or 3 columns filled out 
    before running the program. This will give more context to the future steps. Adjust 
    your steps to take in the data from the columns of your choice.
    """
    
    # Initialize the gspread client to interact with Google Sheets
    try:
        gspread_client = setup_gspread_client()
        print("Gspread client initialized.")
    except Exception as e:
        print("Error initializing gspread client: ", e)

    # Access the Google Sheet by name
    try:
        spreadsheet = gspread_client.open("INSERT NAME OF SPREADSHEET HERE")
        print("Spreadsheet opened.")
    except Exception as e:
        print("Error opening spreadsheet: ", e)
    # Choose the first worksheet within the spreadsheet
    try:
        sheet = spreadsheet.sheet1
        print("Worksheet selected.")
    except Exception as e:
        print("Error selecting worksheet: ", e)

    # Request user input for the range of rows to process
    try:
        start_row = int(input("Enter the first row to process: "))
        end_row = int(input("Enter the last row to process: "))
        print(f"Processing rows from {start_row} to {end_row}.")
    except Exception as e:
        print("Error processing rows: ", e)


    # Get the steps from environment variables
    try:
        steps_env_var = os.getenv("STEPS")
        steps = steps_env_var.split(',') if steps_env_var else []
        print("Steps loaded from environment variables.")
    except Exception as e:
        print("Error loading steps from environment variables: ", e)

    # Iterate over the specified range of rows
    try:
        for row in range(start_row, end_row + 1):
            step_function = dynamic_import("step_1", "process_row_data_with_openai")
            step_function(sheet, row)
        print("Rows processed.")
    except Exception as e:
        print("Error processing rows: ", e)

if __name__ == "__main__":
    try:
        main()
        print("Main function executed successfully.")
    except Exception as e:
        print("Error executing main function: ", e)
