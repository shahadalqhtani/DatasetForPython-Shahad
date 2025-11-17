import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Assuming you have an API endpoint for fetching user data
API_ENDPOINT = "https://api.example.com/users/{user_id}"

def fetch_user_data(user_id):
    # Fetch the token from environment variables or any other secure way
    api_token = os.getenv("API_TOKEN")
    
    if not api_token:
        raise ValueError("API Token is not set in the environment variables.")
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    # Make a request to fetch user data
    response = requests.get(API_ENDPOINT.format(user_id=user_id), headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch user data: {response.status_code} - {response.text}")

# Example usage
if __name__ == "__main__":
    try:
        user_id = input("Enter the user ID to fetch data for: ")
        user_data = fetch_user_data(user_id)
        print("Fetched User Data:", user_data)
    except Exception as e:
        print(f"Error: {e}")