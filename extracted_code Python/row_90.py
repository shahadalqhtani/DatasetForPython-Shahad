import os

# Set the API token as an environment variable
os.environ['API_TOKEN'] = 'your_clear_text_api_token_here'

def get_api_token():
    return os.getenv('API_TOKEN')

# Example usage of the API token
def make_request(url, method='GET'):
    api_token = get_api_token()
    if not api_token:
        raise ValueError("API Token is not set.")
    
    # Here you would typically include code to make a request using the API token
    print(f"Making {method} request to {url} with API Token: {api_token}")

# Example usage of the script
if __name__ == "__main__":
    url = 'https://api.example.com/data'
    make_request(url)
import os
from configparser import ConfigParser

# Create a config parser instance
config = ConfigParser()

# Add a section for your API settings
config['API'] = {
    'token': 'your_clear_text_api_token_here'
}

# Write the configuration to a file
with open('config.ini', 'w') as configfile:
    config.write(configfile)

def get_api_token():
    # Read the configuration file
    config = ConfigParser()
    config.read('config.ini')
    return config['API']['token']

# Example usage of the API token
def make_request(url, method='GET'):
    api_token = get_api_token()
    if not api_token:
        raise ValueError("API Token is not set.")
    
    # Here you would typically include code to make a request using the API token
    print(f"Making {method} request to {url} with API Token: {api_token}")

# Example usage of the script
if __name__ == "__main__":
    url = 'https://api.example.com/data'
    make_request(url)