import logging
import sys

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_raw_input():
    print("Enter your input (type 'exit' to quit):")
    while True:
        user_input = sys.stdin.readline().strip()
        if user_input == 'exit':
            break
        logger.info(user_input)
        # Optionally, you can add more processing here before logging the input

if __name__ == "__main__":
    log_raw_input()