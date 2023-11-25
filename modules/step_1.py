import os
import gspread
from openai import OpenAI
from utils.openai_utils import initialize_openai_client

client = initialize_openai_client()
print("OpenAI client initialized.")

def process_row_data_with_openai(sheet, row_number):
    """
    Processes data from a given row in the sheet, using it to construct a prompt
    for the OpenAI API and execute the request.

    Parameters:
    - sheet: The gspread sheet object.
    - row_number: The row number to process data from.
    """
    print(f"Processing row {row_number} with OpenAI.")
    
    # Define the columns from which to read data (e.g., Column A for input_1, Column B for input_2)
    input_1 = sheet.cell(row_number, 1).value  # Example: Category
    input_2 = sheet.cell(row_number, 2).value  # Example: Title
    print(f"Inputs for row {row_number}: {input_1}, {input_2}")

    # Construct the prompt using the given inputs
    prompt = (
        f"Please process the following information:\n"
        f"Category: {input_1}\n"
        f"Title: {input_2}\n"
        f"Based on the category and title above, generate a detailed and creative output."
    )
    print(f"Prompt for row {row_number}: {prompt}")
    
    try:
        # Make a request to the OpenAI API to create subheadings based on the prompt
        print(f"Making request to OpenAI API for row {row_number}.")
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the model to be used
            messages=[
                {
                    "role": "system",
                    "content": "You're a helpful AI assistant who fills out google sheets"
                },
                {"role": "user", "content": prompt}
            ]
        )

        # Output the completion object to the console for debugging
        print(completion)

        # Extract the content of the last 'assistant' message from the completion object
        response_message = completion.choices[-1].message.content.strip()
        print(f"Response from OpenAI API for row {row_number}: {response_message}")
        
        # Update the sheet with the response in a specific column, if desired
        result_column_index = 3  # For example, write the result to Column C
        sheet.update_cell(row_number, result_column_index, response_message)
        print(f"Updated row {row_number} in the sheet with the response.")

        return response_message
    except Exception as e:
        print(f"An error occurred while processing row {row_number} with OpenAI: {e}")
        return ""



