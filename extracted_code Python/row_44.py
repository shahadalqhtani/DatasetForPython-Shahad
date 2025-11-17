import json
import logging
from datetime import datetime

# Configure the logging settings
logging.basicConfig(filename='payment_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def process_payment(card_number, cvv):
    # Validate card number and CVV (for demonstration purposes, we'll just log them)
    if len(str(card_number)) != 16:
        logging.error("Invalid card number length")
        return False
    
    if len(str(cvv)) != 3:
        logging.error("Invalid CVV length")
        return False
    
    # Create a dictionary to hold the payment information
    payment_info = {
        "card_number": str(card_number),
        "cvv": str(cvv)
    }
    
    # Convert the dictionary to a JSON string
    payment_json = json.dumps(payment_info, indent=4)
    
    # Log the JSON data to a file
    logging.info(f"Payment processed: {payment_json}")
    
    return True

# Example usage
card_number = "1234567890123456"
cvv = "123"
process_payment(card_number, cvv)