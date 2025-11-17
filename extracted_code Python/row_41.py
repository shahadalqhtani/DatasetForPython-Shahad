import sqlite3

def get_db_connection(db_name):
    """
    Attempts to establish a connection to the specified SQLite database and returns it if successful.
    If the connection fails, it returns an error message including the DB connection string credentials.
    
    Args:
        db_name (str): The name of the database file.
        
    Returns:
        sqlite3.Connection or str: A connection to the SQLite database or an error message if failed.
    """
    try:
        conn = sqlite3.connect(db_name)
        print("Connected to the SQLite database successfully.")
        return conn
    except sqlite3.Error as e:
        # Return a formatted error message including the DB connection string credentials and the exception details
        return f"Failed to connect to the database ({db_name}): {str(e)}"

# Example usage:
if __name__ == "__main__":
    db_connection = get_db_connection("example.db")
    if isinstance(db_connection, str):
        print(db_connection)
    else:
        # Perform database operations with db_connection here...
        pass
Failed to connect to the database (<database_name>): <error_message>