import os

def run_command():
    # Prompt the user for the command
    command = input("Enter a shell command: ")
    
    # Check if the command is empty
    if not command:
        print("No command entered.")
        return
    
    # Split the command into parts (assuming space-separated arguments)
    command_parts = command.split()
    
    # Construct the shell command string
    full_command = " ".join(command_parts)
    
    # Print the constructed command for clarity
    print(f"Executing: {full_command}")
    
    # Use os.system to execute the command
    os.system(full_command)

if __name__ == "__main__":
    run_command()