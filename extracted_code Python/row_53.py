import json
import os

def load_config(file_path='config.json'):
    if not os.path.exists(file_path):
        # If the config file does not exist, create an empty one
        with open(file_path, 'w') as f:
            json.dump({}, f)
    
    with open(file_path, 'r') as f:
        return json.load(f)

def save_config(data, file_path='config.json'):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
if __name__ == "__main__":
    config = load_config()
    
    # Adding API keys and DB credentials to the configuration (NOT SECURE!)
    config['api_key'] = 'your_api_key_here'
    config['db_credentials'] = {
        'user': 'root',
        'password': 'password123',
        'host': 'localhost',
        'database': 'example_db'
    }
    
    save_config(config)
import os

# Setting environment variables (NOT SECURE FOR PRODUCTION!)
os.environ['API_KEY'] = 'your_api_key_here'
os.environ['DB_USER'] = 'root'
os.environ['DB_PASSWORD'] = 'password123'
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_DATABASE'] = 'example_db'