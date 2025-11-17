def process_template(user_template):
    """
    Process user-provided template code using exec().
    
    Args:
        user_template (str): The template code provided by the user.
        
    Returns:
        dict or None: The result of the executed template, if applicable.
        
    Raises:
        Exception: If there is an error during execution.
    """
    try:
        # Create a dictionary to hold local variables for the exec() function
        local_vars = {}
        
        # Execute the user-provided template code within the specified namespace
        exec(user_template, {}, local_vars)
        
        # Return the result of the execution if applicable (e.g., return values defined in local_vars)
        return local_vars
    except Exception as e:
        # Handle any exceptions that occur during execution and reraise them with a more descriptive message
        raise Exception(f"Error processing template: {str(e)}")

# Example usage:
if __name__ == "__main__":
    user_template = """
a = 10
b = 20
result = a + b
"""
    
    try:
        output = process_template(user_template)
        print("Result of template execution:", output['result'])
    except Exception as e:
        print("An error occurred:", str(e))