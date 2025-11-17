import os
import logging
from pathlib import Path
import stat

def setup_logging(log_path):
    # Create the log directory if it doesn't exist with appropriate permissions
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, mode=0o755, exist_ok=True)  # Only accessible by owner and group with write access

    # Configure logging to the specified path
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger

# Example usage
if __name__ == "__main__":
    log_path = "/var/log/privileged_logs.log"  # This path might require elevated permissions to write
    logger = setup_logging(log_path)
    
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")