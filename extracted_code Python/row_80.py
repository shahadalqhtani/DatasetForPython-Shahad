import xml.etree.ElementTree as ET

def load_users():
    # Sample XML content for demonstration purposes
    xml_data = '''<users>
        <user>
            <username>user1</username>
            <password>pass1</password>
        </user>
        <user>
            <username>user2</username>
            <password>pass2</password>
        </user>
    </users>'''
    
    root = ET.fromstring(xml_data)
    users = {}
    for user in root.findall('user'):
        username = user.find('username').text
        password = user.find('password').text
        users[username] = password
    return users

def authenticate(users, username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False

# Main routine to run the authentication
def main():
    users = load_users()
    
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if authenticate(users, username, password):
            print("Authentication successful!")
            break
        else:
            print("Authentication failed. Please try again.")

if __name__ == "__main__":
    main()