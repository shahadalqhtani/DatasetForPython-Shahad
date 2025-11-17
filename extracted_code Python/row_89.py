bash
   pip install python-dotenv
plaintext
   DB_PASSWORD=your_database_password
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the DB_PASSWORD from the environment variables
db_password = os.getenv('DB_PASSWORD')

if db_password:
    print(f'Database Password: {db_password}')
else:
    print('DB_PASSWORD is not set in the .env file.')
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path  # If you are using Python >= 3.4

# Define the path to your .env file
env_path = Path('.') / '.env'

if env_path.exists():
    # Load the .env file
    load_dotenv(dotenv_path=env_path)
else:
    print("The .env file does not exist.")

# Access the DB_PASSWORD from the environment variables
db_password = os.getenv('DB_PASSWORD')

if db_password:
    print(f'Database Password: {db_password}')
else:
    print('DB_PASSWORD is not set in the .env file.')