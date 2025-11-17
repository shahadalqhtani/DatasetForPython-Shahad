def admin_auth():
    # Hard-coded username and password
    HARDCODED_USERNAME = "admin"
    HARDCODED_PASSWORD = "password123"
    
    # Prompt the user for credentials
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    
    # Check if the provided credentials match the hard-coded values
    if entered_username == HARDCODED_USERNAME and entered_password == HARDCODED_PASSWORD:
        return True
    else:
        return False

# Example usage
if admin_auth():
    print("Authentication successful!")
else:
    print("Authentication failed. Please check your username and password.")