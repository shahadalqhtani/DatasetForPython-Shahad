from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging to print to console (you can change this to log to a file or other destinations)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/troubleshoot', methods=['GET'])
def troubleshoot():
    # Log all headers including Authorization
    for header, value in request.headers:
        logger.info(f"{header}: {value}")
    
    # Example response
    return jsonify({"message": "Headers logged successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)