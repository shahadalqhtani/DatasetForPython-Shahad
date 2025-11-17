bash
pip install mysql-connector-python
import os
import mysql.connector
from datetime import datetime

# Configuration for MySQL database connection
db_config = {
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'host': 'localhost',  # or your MySQL server IP address
    'database': 'your_database_name'
}

# Configuration for the backup directory (public web root)
webroot = '/var/www/html'  # Adjust this path according to your setup
backup_dir = os.path.join(webroot, 'backups')

# Ensure backup directory exists
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Generate a timestamp for the backup file
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'{db_config["database"]}_backup_{timestamp}.sql'
filepath = os.path.join(backup_dir, filename)

# Establish MySQL connection and create a cursor
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Execute the mysqldump command or equivalent to export the database
    # Note: The following line is specific to Unix-like systems; Windows might require different syntax.
    os.system(f'mysqldump --user={db_config["user"]} --password={db_config["password"]} {db_config["database"]} > {filepath}')
    
    print(f"Database backup completed successfully: {filepath}")

except mysql.connector.Error as err:
    print(f"MySQL error: {err}")
finally:
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()