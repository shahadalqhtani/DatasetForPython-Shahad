import subprocess
import sys

def run_command(command):
    # Ensure the command and its arguments are safe by splitting them into a list
    if isinstance(command, str):
        parts = command.split()
    elif isinstance(command, list):
        parts = command
    else:
        raise ValueError("Command must be a string or a list of strings.")

    # Use subprocess to safely execute the command
    result = subprocess.run(parts, check=True)
    return result.stdout

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py '<command>'")
        sys.exit(1)

    command = sys.argv[1]
    try:
        output = run_command(command)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")