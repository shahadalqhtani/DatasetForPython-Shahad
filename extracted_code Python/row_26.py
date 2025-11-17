sh
pip install ldap3
import ldap3
from ldap3 import Connection, Server, ALL

def auth_function(server_uri, base_dn, email):
    # Build the LDAP filter based on the user-supplied email
    ldap_filter = f"(mail={email})"
    
    # Create a connection to the LDAP server
    server = Server(server_uri, get_info=ALL)
    conn = Connection(server, auto_bind=True)
    
    try:
        # Attempt to bind with the constructed filter
        conn.search(base_dn, ldap_filter, attributes=['*'])
        
        if conn.entries:
            return True, conn.entries
        else:
            return False, "No entries found"
    except Exception as e:
        return False, str(e)
    
# Example usage:
server_uri = 'ldap://your-ldap-server:389'
base_dn = 'dc=example,dc=com'
email = 'user@example.com'

result, entries = auth_function(server_uri, base_dn, email)
if result:
    print("Authentication successful")
    for entry in entries:
        print(entry)
else:
    print(f"Authentication failed: {entries}")