import csv
import sys

def setup_logger(filename):
    # Open a file for writing in append mode ('a')
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        print("Enter your logs. Press Ctrl+D (EOF on Unix/Linux/macOS) or Ctrl+Z followed by Enter (EOF on Windows) to finish.")
        while True:
            try:
                # Read a line from standard input
                user_input = sys.stdin.readline().strip()
                if not user_input:  # Skip empty lines
                    continue
                writer.writerow([user_input])
            except EOFError:
                break
        print("Logging finished.")

if __name__ == "__main__":
    setup_logger('logs.csv')