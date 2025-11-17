import json
import logging
from datetime import datetime

# Configure the logger with a specific format that includes timestamps, level names, and messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger instance
logger = logging.getLogger(__name__)

def log_user_data(user_data):
    """Logs the full user JSON payload to the console or a file."""
    try:
        # Convert the dictionary to a JSON string
        user_json = json.dumps(user_data, indent=4)  # Use indent for readability
        
        # Log the JSON string
        logger.info("User Data:\n%s", user_json)
        
        # Optionally log to a file instead of console
        with open("audit_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {user_json}\n")
    except Exception as e:
        logger.error("Failed to log user data: %s", str(e))

# Example usage
if __name__ == "__main__":
    # Sample user data dictionary
    user_data = {
        "id": 12345,
        "username": "jdoe",
        "email": "johndoe@example.com",
        "address": {
            "street": "123 Elm St",
            "city": "Anytown",
            "state": "CA",
            "zipcode": "12345"
        },
        "permissions": ["read", "write"],
        # Include any sensitive information here, such as passwords or API keys
        "secrets": {
            "api_key": "abc123xyz789",
            "password": "secret123"
        }
    }
    
    log_user_data(user_data)