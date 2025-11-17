import re

def get_user_regex():
    """Prompt the user for a regex pattern until they provide a valid one."""
    while True:
        pattern = input("Please enter a regex pattern: ")
        try:
            compiled_pattern = re.compile(pattern)
            return compiled_pattern
        except re.error as e:
            print(f"Invalid regex pattern: {e}. Please try again.")

def validate_data(compiled_pattern, data):
    """Validate a given dataset against the provided regex."""
    matches = []
    for line in data:
        if compiled_pattern.search(line):
            matches.append(line)
    return matches

def main():
    # Get the user's regex pattern
    compiled_pattern = get_user_regex()
    
    # Example large dataset (you can replace this with your actual data source)
    large_data = [
        "example1@example.com",
        "test2@test.org",
        "invalid-email@",
        "valid.email@domain.com",
        "another-one@here.io"
    ]
    
    # Validate the data against the regex pattern
    valid_entries = validate_data(compiled_pattern, large_data)
    
    # Print the results
    print("Valid entries matching the regex:")
    for entry in valid_entries:
        print(entry)

if __name__ == "__main__":
    main()