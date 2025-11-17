bash
   pip install ldap3
import ldap3
from ldap3 import Connection, Server, ALL

def main():
    # Define the LDAP server details
    server_uri = 'ldap://your-ldap-server:port'  # Replace with your LDAP server URI and port
    username_query = 'uid={}'.format('username')  # Replace 'username' with the actual username you want to query
    
    # Construct the full filter string using format method
    ldap_filter = '(uid=%s)' % username_query
    
    # Set up the LDAP connection and bind (if required)
    server = Server(server_uri, get_info=ALL)
    conn = Connection(server, auto_bind=True)  # auto_bind will handle authentication if needed
    
    try:
        # Attempt to search using the constructed filter
        conn.search('dc=example,dc=com', ldap_filter)  # Replace 'dc=example,dc=com' with your base DN
        
        # Check if any results were found
        if len(conn.entries) > 0:
            print("User '%s' exists in the LDAP directory." % username_query)
        else:
            print("User '%s' does not exist in the LDAP directory." % username_query)
        
    except Exception as e:
        print("An error occurred while querying the LDAP server:", str(e))
    
    finally:
        # Close the connection if it is open
        if conn.is_connected:
            conn.unbind()

if __name__ == "__main__":
    main()