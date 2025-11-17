import re
import sys

def parse_logs(log_file_path, filter_pattern):
    # Read the log file
    with open(log_file_path, 'r') as log_file:
        logs = log_file.readlines()

    # Compile the regex pattern if it's a string
    if isinstance(filter_pattern, str):
        filter_pattern = re.compile(filter_pattern)

    # Filter logs based on the regex pattern
    filtered_logs = []
    for log in logs:
        match = filter_pattern.search(log)
        if match:
            filtered_logs.append(log)

    return filtered_logs

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <log_file_path> <filter_pattern>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    filter_pattern = sys.argv[2]

    # Parse the logs and apply the regex filter
    filtered_logs = parse_logs(log_file_path, filter_pattern)

    # Print the filtered logs
    for log in filtered_logs:
        print(log.strip())

if __name__ == "__main__":
    main()
sh
   python log_parser.py <log_file_path> <filter_pattern>
sh
python log_parser.py access.log "ERROR"
import re
import sys

def parse_logs(log_file_path, filter_pattern):
    # Read the log file
    with open(log_file_path, 'r') as log_file:
        logs = log_file.readlines()

    # Compile the regex pattern if it's a string
    if isinstance(filter_pattern, str):
        filter_pattern = re.compile(filter_pattern)

    # Filter logs based on the regex pattern
    filtered_logs = []
    for log in logs:
        match = filter_pattern.search(log)
        if match:
            filtered_logs.append(log)

    return filtered_logs

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <log_file_path> <filter_pattern>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    
    # Prompt for the regex filter pattern
    filter_pattern = input("Enter the regex filter pattern: ")

    # Parse the logs and apply the regex filter
    filtered_logs = parse_logs(log_file_path, filter_pattern)

    # Print the filtered logs
    for log in filtered_logs:
        print(log.strip())

if __name__ == "__main__":
    main()