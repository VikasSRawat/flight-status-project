import os

class Config:
    API_KEY = os.getenv('API_KEY', '85b623d3992995bd6634125903844f0c') # Replace 'your_default_api_key' with your actual default key if needed
    API_URL = 'http://api.aviationstack.com/v1/flights'

    if not API_KEY:
        raise ValueError("No API key found. Please set the API_KEY environment variable.")
    print(f"API_KEY is : {API_KEY}")  # Debug statement to print API key
