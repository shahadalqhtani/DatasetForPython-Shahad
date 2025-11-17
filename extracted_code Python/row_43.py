import logging

# Configure the logging settings
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Simulated database of users (username: password)
users_db = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3"
}

def authenticate(username, password):
    if username in users_db and users_db[username] == password:
        logger.info(f"Authentication successful for user: {username}")
        return True
    else:
        logger.warning(f"Failed authentication attempt for user: {username}")
        return False

# Example usage
if __name__ == "__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if authenticate(username, password):
        print("Login successful!")
    else:
        print("Login failed. Please check your credentials.")