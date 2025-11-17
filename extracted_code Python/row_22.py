import sqlite3

# Function to build and execute the SQL query
def run_query(name):
    # Connect to SQLite database (or use another method to establish connection)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Build the SQL query using string interpolation
    sql_query = "SELECT * FROM users WHERE name = '{}'".format(name)
    
    # Execute the query
    cursor.execute(sql_query)
    
    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)
    
    # Close the connection
    conn.close()

# Example usage
if __name__ == "__main__":
    name_to_search = "John Doe"  # Replace with actual user input or variable value
    run_query(name_to_search)