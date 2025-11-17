bash
pip install flask
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    
    # Basic validation to ensure the user input is present and not empty
    if 'pattern' not in data or not data['pattern']:
        return jsonify({"error": "Pattern must be provided"}), 400
    if 'text' not in data or not data['text']:
        return jsonify({"error": "Text to search must be provided"}), 400
    
    pattern = data['pattern']
    text = data['text']
    
    try:
        # Attempt to compile the regex pattern
        compiled_pattern = re.compile(pattern)
        
        # Search for the pattern in the text
        matches = compiled_pattern.findall(text)
        
        return jsonify({"matches": matches})
    except re.error as e:
        # Handle invalid regex patterns
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
bash
curl -X POST http://127.0.0.1:5000/search -H "Content-Type: application/json" -d '{"pattern": "a+", "text": "banana"}'