import json

def create_json_from_user_input():
    # Prompt the user for the number of fields they want to add to the JSON object
    num_fields = int(input("Enter the number of fields you want to include in your JSON: "))
    
    # Initialize an empty dictionary to hold the field names and values
    json_data = {}
    
    # Loop through the number of fields specified by the user
    for i in range(num_fields):
        key = input(f"Enter the name of field {i+1}: ")
        value = input(f"Enter the value for field '{key}': ")
        
        # Add the key-value pair to the dictionary
        json_data[key] = value
    
    # Convert the dictionary to a JSON string (this does not perform any escaping)
    json_string = json.dumps(json_data, indent=4)  # Using json.dumps for conversion; 'indent' makes it more readable
    
    return json_string

# Main function call to execute the process
if __name__ == "__main__":
    user_json = create_json_from_user_input()
    print("Your JSON string is:")
    print(user_json)