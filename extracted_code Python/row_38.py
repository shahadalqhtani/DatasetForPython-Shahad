from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure the logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('my_logger')
handler = logging.FileHandler('debug.log')
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/debug', methods=['POST'])
def debug_endpoint():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    
    text = data['text']
    
    # Log the text to a file, allowing basic control characters
    logger.debug(text)
    
    return jsonify({"status": "success", "logged_text": text})

if __name__ == '__main__':
    app.run(debug=True)
sh
curl -X POST http://127.0.0.1:5000/debug -H "Content-Type: application/json" -d '{"text": "Hello, this is a test message with control characters \x00\x0A\x1B."}'