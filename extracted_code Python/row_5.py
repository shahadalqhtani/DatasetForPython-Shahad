bash
pip install Flask
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_json():
    try:
        data = request.get_json()
        
        # Example file operations based on received JSON data
        if 'filename' in data:
            filename = data['filename']
            
            # Create a new file with the provided name and write some content to it
            with open(filename, 'w') as f:
                f.write("This is a test file created from JSON input.")
            
            return jsonify({"status": "success", "message": f"File '{filename}' created successfully."}), 201
        else:
            return jsonify({"status": "error", "message": "Missing 'filename' in the JSON data."}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
bash
python app.py
bash
curl -X POST http://127.0.0.1:5000/process -H "Content-Type: application/json" -d '{"filename": "testfile.txt"}'