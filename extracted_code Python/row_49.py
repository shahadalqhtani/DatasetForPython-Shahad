sh
pip install requests
import requests
import json

# Define the API URL (replace with your actual API endpoint)
api_url = 'https://api.example.com/data'

try:
    # Make a GET request to the API URL with SSL verification disabled
    response = requests.get(api_url, verify=False)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            
            # Process sensitive data from the response
            # For demonstration, let's print some fields
            if 'sensitiveData' in data:
                sensitive_data = data['sensitiveData']
                print("Sensitive Data:", json.dumps(sensitive_data, indent=4))
            else:
                print("No sensitive data found in the response.")
        except ValueError as e:
            print("Error parsing JSON from API response:", str(e))
    else:
        print("Failed to retrieve data from API. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("An error occurred while making the request:", str(e))