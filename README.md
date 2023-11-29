# Python-Google-Sheets-OpenAI Integration Template

This project serves as a template to automate processes using Google Sheets and OpenAI's API. It allows users to define actions in Python that interact with spreadsheet data to perform tasks such as generating text, processing data, and more.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Setting Up the Environment](#setting-up-the-environment)
  - [Install Dependencies](#install-dependencies)
- [Google Sheets API Setup](#google-sheets-api-setup)
- [OpenAI API Setup](#openai-api-setup)
- [Usage](#usage)
- [Extending the steps](#extending-the-steps)
  - [Environment Variables](#environment-variables)
  - [Running the Script](#running-the-script)
- [Customizing the Steps](#customizing-the-steps)

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Before you begin, ensure you have the following prerequisites installed and set up:

1. Python 3.7 or Higher
- Python is the primary language used for scripting in this project.
- If you don't have Python installed, download it from the [official Python website](https://www.python.org/downloads/).
- Follow the installation instructions for your operating system (Windows, macOS, Linux).
- To check if Python is installed, open a terminal or command prompt and type `python --version`. You should see a version number that is 3.7 or higher.

2. Pip (Python Package Installer)
- Pip is used to install Python packages needed for the project.
- It is usually installed with Python. To check, type `pip --version` in your terminal or command prompt.
- If Pip is not installed, follow the [installation guide](https://pip.pypa.io/en/stable/installing/).

3. Google Cloud Platform Account
- You need a Google Cloud Platform (GCP) account to access the Google Sheets API.
- Sign up for an account [here](https://cloud.google.com/).
- After creating your account, enable the Google Sheets API by following these [steps](https://cloud.google.com/apis/docs/getting-started#enable-apis).

4. OpenAI Account
- An OpenAI account is required to get an API key for accessing OpenAI's services.
- Sign up for an account at [OpenAI](https://openai.com/).
- Once your account is set up, you can find your API key by following the instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key).
- Keep your API key confidential and secure.

Once you have these prerequisites ready, you can proceed with the installation and setup of the project.

## Installation
Follow these steps to install and set up the project on your local machine:

1. ## setting-up-the-environment
   - A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages.
   - Creating a virtual environment ensures that the dependencies of your project are isolated from your main system.
   - To create a virtual environment, execute:
     ```bash
     python -m venv venv
     ```
     This command creates a new directory named `venv` in your project directory, containing the virtual environment.
   - Now, activate the virtual environment:
     - On Windows, run:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS and Linux, run:
       ```bash
       source venv/bin/activate
       ```
     Your command prompt will change to show the name of the activated environment.
2. Clone the Repository
   - If you have Git installed, open a terminal or command prompt.
   - Navigate to the folder where you want the project to be using the `cd` command. For example: `cd Documents/Projects`.
   - Clone the repository by executing:
     ```bash
     git clone https://github.com/timbosTours/python-openai-google-sheets-starter.git
     ```

3. Navigate to the Project Directory
   - After cloning the repository, move into the project directory:
     ```bash
     cd python-openai-google-sheets-starter
     ```


4. ## install-dependencies
   - With the virtual environment activated, install the project dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```
     This command installs all the required Python packages as specified in the `requirements.txt` file.

After completing these steps, your project setup is complete, and you're ready to proceed to the next stages of configuring and using the application.

## Google Sheets API Setup

To interact with Google Sheets through your project, you need to set up access to the Google Sheets API. Follow these detailed steps to get started:

1. Create a Project in Google Cloud Platform
  - Go to the [Google Cloud Console](https://console.cloud.google.com/).
  - Sign in with your Google account.
  - Click on "Select a project" at the top of the page, then click on "NEW PROJECT".
  - Enter a project name and select or create an organization, then click "Create".

2. Enable the Google Sheets API
  - In your new project, navigate to the "API & Services" dashboard.
  - Click on "+ ENABLE APIS AND SERVICES".
  - Search for "Google Sheets API" in the API library.
  - Click on the Google Sheets API and then click "ENABLE".

3. Configure Consent Screen
  - Go to the "OAuth consent screen" in the sidebar.
  - Select the user type (usually "External" for public use) and click "Create".
  - Fill in the required fields like app name, user support email, and developer contact information.
  - Save and continue, adding any scopes or test users as needed (you can skip these steps for a basic setup).

4. Create Credentials
  - Go to "Credentials" in the sidebar.
  - Click on "Create Credentials" at the top of the page and select "OAuth client ID".
  - If prompted, configure the OAuth consent screen first.
  - For "Application type," select "Desktop app" and give it a name.
  - Click "Create", and you will see a dialog with your client ID and client secret.
  - Download the JSON file containing these credentials by clicking on the download icon next to the credentials.

5. Use Credentials in Your Project
  - Rename the downloaded JSON file to `credentials.json` and place it in your project directory.
  - This file should be referenced in your project's code to authenticate with the Google Sheets API.

6. Follow the Official Guide for Additional Help
  - If you need more detailed instructions or encounter issues, refer to the [official Google Sheets API guide](https://developers.google.com/sheets/api).

By following these steps, you will have set up the Google Sheets API for your project. This will enable your Python scripts to access and manipulate data in Google Sheets.

## OpenAI API Setup
To integrate OpenAI's capabilities into this project, you need to set up and configure access to the OpenAI API. Follow these steps to get your API key and configure it for use in the project:

1. Create an OpenAI Account
If you don't already have an OpenAI account, visit the OpenAI website and sign up.
Follow the instructions to create a new account, which will involve providing your email address and creating a password.

2. Access the API Key
Once your account is set up, log in to the OpenAI platform.
Navigate to the API section in your account dashboard. This is typically found under a section like "API" or "Developer."
Here, you will find your API key, a unique string that grants you access to OpenAI's API services.

3. Secure Your API Key
Treat your API key as a sensitive password. Do not share it publicly or commit it to your version control system.
To securely use the API key in your project, store it in an environment variable. This was covered in the Environment Variables section of this README.

4. Install the OpenAI Python Package
If not already installed, you need to install OpenAI's Python package to interact with the API. This can be done using pip:
Copy code
pip install openai

5. Initialize the OpenAI Client in Your Project
In your Python script, import the OpenAI package and initialize the OpenAI client using your API key.
This typically looks like:
python
Copy code
import openai
openai.api_key = os.environ['OPENAI_API_KEY']
Ensure that you have loaded the environment variable (as shown in the Environment Variables section) before using it to initialize the client.

6. Testing the API Connection
To test if your setup is correct, try making a simple request to the OpenAI API, such as generating text using a small prompt.
Handle any exceptions or errors to ensure that the API key is working correctly.

7. Review OpenAI's Usage Guidelines and Limits
Familiarize yourself with OpenAI's usage guidelines, pricing, and rate limits to ensure that your usage of the API remains within the allowed parameters.
You can find this information on the OpenAI documentation or account dashboard.

8. Update Project Dependencies
If your project uses a requirements.txt file for managing dependencies, make sure to include openai in this file.
This ensures that anyone setting up your project will automatically install the necessary OpenAI package.

By following these steps, you will have successfully set up the OpenAI API for your project. This setup allows your Python scripts to access OpenAI's powerful AI models and capabilities, enabling a wide range of automated tasks and data processing features.


## Usage

This Python-Google-Sheets-OpenAI integration can be utilized in a variety of innovative and practical ways. Below are some use cases to inspire and guide you:

1. Automated Customer Feedback Analysis

  Scenario: You have a Google Sheet filled with customer feedback comments.

  Usage: Use the integration to automatically analyze sentiment and key themes in the feedback using OpenAI's natural language processing capabilities. Generate a summary or report directly in the Google Sheet.

2. Content Generation for Marketing

  Scenario: You're managing a marketing campaign and need to generate creative content ideas.

  Usage: Input key marketing themes or product information into a Google Sheet. The script can then use OpenAI's API to generate a variety of content ideas, taglines, or even full blog post drafts.

3. Data Cleaning and Preprocessing

  Scenario: You have a dataset in Google Sheets with inconsistencies or missing values.

  Usage: Automate the process of cleaning and preparing the data for analysis. The script can format text, fill in missing values, or even suggest corrections based on patterns learned from OpenAI.

4. Language Translation for Global Teams

  Scenario: Your team works with multilingual data that needs to be translated.

  Usage: Implement a feature where the script takes text from Google Sheets in one language and provides translations in another, utilizing OpenAI's advanced language models for accuracy.

5. Educational Quizzes and Learning Materials

  Scenario: You're an educator needing to create quizzes or educational content.

  Usage: Input topics or questions into a Google Sheet. The script can generate quiz questions, answers, and even explanatory notes, tailored to the educational level and subject matter.

6. Personalized Email or Message Drafting

  Scenario: You need to send personalized emails or messages based on customer data.

  Usage: Store customer information and key points in Google Sheets. The script can generate personalized email or message drafts using this data, ready for review and sending.

These use cases demonstrate the versatility and power of integrating Python with Google Sheets and OpenAI. With this template, you can automate complex tasks, derive insights from data, and enhance productivity in creative and impactful ways.


### Environment Variables

Environment variables are used to securely store sensitive information, such as API keys, outside of your main codebase. To configure these for your project, follow these steps:

1. Create a .env File
  In the root directory of your project, create a new file named `.env`.
  This file will be used to store your private keys and other sensitive data.

2. Add Environment Variables to the .env File
  Open the `.env` file in a text editor.
  Define each variable on a new line. For this project, you will need to set variables for your Google Sheets and OpenAI API keys.
  The format should be `VARIABLE_NAME=value`. For example:
  ```plaintext
  GOOGLE_SHEETS_API_KEY=your_google_sheets_api_key
  OPENAI_API_KEY=your_openai_api_key
  ```
  Replace `your_google_sheets_api_key` and `your_openai_api_key` with your actual API keys.

3. Securing the .env File
  Make sure the `.env` file is included in your `.gitignore` file. This prevents the file from being uploaded to version control, keeping your sensitive information secure.
  If you're not sure how to do this, simply add a line containing `.env` to your `.gitignore` file.

4. Accessing Environment Variables in Your Python Script
  Use a Python package like `python-dotenv` to load the environment variables in your script.
  Install it via Pip if you haven't already:
  ```bash
  pip install python-dotenv
  ```
  At the beginning of your script, add:
  ```python
  from dotenv import load_dotenv
  load_dotenv()
  ```
  Now you can access your variables using:
  ```python
  import os
  google_sheets_api_key = os.getenv('GOOGLE_SHEETS_API_KEY')
  openai_api_key = os.getenv('OPENAI_API_KEY')
  ```

By following these instructions, you'll set up your environment variables safely and be able to access them within your Python scripts.

## Running the Script

To execute and interact with the `main.py` script, follow these steps:

1. Open your terminal or command prompt and navigate to the root directory of your project.
  ```bash
  cd /path/to/project
  ```

2. Activate the virtual environment.
  - Windows:
    ```bash
    venv\Scripts\activate
    ```
  - macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

3. Run the script.
  ```bash
  python main.py
  ```

  The script may take a few moments to initialize, especially on the first run.

4. Follow the prompts.
  The script may prompt you for input to specify its operation. Provide the required information as prompted, ensuring precision in your input.

5. Monitor the script execution.
  The script will display information in the terminal about its progress. Pay attention to any errors or important messages. If the script provides feedback or results upon completion, wait for them to be displayed.

6. Complete the execution.
  Once the script has finished running, it will typically indicate completion with a message. If the script requires you to end the execution manually, you can usually do so by pressing `Ctrl + C` in the terminal.

7. Review the results.
  After running the script, check the results of its operation. This may include changes in your Google Sheets, newly generated files, or output in the terminal.

By following these steps, you can successfully run and interact with the `main.py` script. Make sure to review any specific instructions or documentation related to the script for additional guidance or features.


## Customizing the Steps

This project is designed to be flexible and easily adaptable to your specific workflow needs. You can customize the existing step modules or add new ones as required.

### Dynamic Import Utility

The `dynamic_import` function in the `utils` package provides the ability to import and execute functions dynamically from the modules you specify. This is especially useful when the steps to be executed are not known beforehand and may be user-defined or vary during runtime.

Here's how to use the `dynamic_import` utility:


### Understanding the Provided Example

The provided `process_row_data_with_openai` function is a template that reads data from a specified row in a Google Sheet, constructs a prompt for the OpenAI API, and processes the response. The function showcases how to interact with both Google Sheets and OpenAI, offering a foundation for more complex operations.

### Customizing for Different Use Cases

#### Analyze Customer Feedback:

- Modify the function to analyze sentiment or categorize feedback.
- Adjust the OpenAI prompt to focus on sentiment analysis or categorization based on the content of each row.

#### Content Generation:

- For marketing or content creation, change the input columns to represent different aspects of the content (like style, target audience).
- Tailor the OpenAI prompt to generate creative text based on these inputs.

#### Data Cleaning:

- Integrate logic to identify inconsistencies or missing values in the data.
- Use OpenAI to suggest corrections or to fill in gaps based on context.

#### Language Translation:

- Adjust the script to send a row's content to OpenAI for translation.
- Ensure the prompt is structured to request translation into the desired language.

#### Educational Material Creation:

- Design prompts that instruct OpenAI to generate quiz questions or educational content based on the inputs from Google Sheets.

#### Email or Message Drafting:

- Customize the script to use customer data for drafting personalized emails or messages.
- The prompt should instruct OpenAI to draft a message considering the customer's information and history.

### Incorporating Additional Python Libraries

Depending on your use case, you might need additional Python libraries. For example, use pandas for advanced data manipulation, matplotlib for data visualization, or numpy for numerical operations. To integrate a new library, import it into your script and modify the steps to utilize its functionality.

### Writing Custom Functions

For each unique task, consider writing a separate function in the modules directory. This modular approach keeps your code organized and makes it easier to manage complex workflows.

### Testing and Iteration

After customizing a step, test it thoroughly with different datasets to ensure it behaves as expected. Iterate based on test results and refine the logic or OpenAI prompts as needed.

By understanding and modifying these steps, you can tailor the Python-Google-Sheets-OpenAI integration to fit a diverse array of applications, from data analysis to automated content creation. The flexibility of the template allows for creativity and innovation in how you choose to leverage these powerful tools.

