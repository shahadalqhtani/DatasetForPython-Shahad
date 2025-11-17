import ldap3
from ldap3 import Connection, Server, ALL

def perform_ldap_search(group_name):
    # Configure the LDAP server and connection details
    server = Server('ldap://your-ldap-server', get_info=ALL)
    conn = Connection(server, auto_bind=True)

    # Perform an LDAP search for the specified group
    base_dn = 'ou=groups,dc=example,dc=com'  # Modify this to match your LDAP structure
    search_filter = f'(cn={group_name})'
    conn.search(base_dn, search_filter)

    if conn.entries:
        print(f"Found entries for group '{group_name}':")
        for entry in conn.entries:
            print(entry.entry_to_json())
    else:
        print(f"No entries found for group '{group_name}'.")

if __name__ == "__main__":
    # Prompt the user for a group name
    group_name = input("Enter the group name to search for: ")
    
    # Perform the LDAP search
    perform_ldap_search(group_name)