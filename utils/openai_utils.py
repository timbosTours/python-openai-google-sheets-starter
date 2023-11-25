from openai import OpenAI
import os

def initialize_openai_client():
    """
    Initializes the OpenAI client using the API key from the environment variable.
    """
    try:
        print("Initializing OpenAI client...")
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        print("OpenAI client initialized successfully.")
        return client
    except Exception as e:
        print("Error occurred while initializing OpenAI client: ", e)
        return None
