import sys

def main():
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    # Get the filename from the command-line arguments
    filename = sys.argv[1]

    try:
        # Open the file and read its contents
        with open(filename, 'r') as file:
            content = file.read()
            print("File contents:\n", content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

if __name__ == "__main__":
    main()
sh
python readfile.py example.txt