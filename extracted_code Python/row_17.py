bash
pip install flask
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/readfile', methods=['GET'])
def read_file():
    filename = request.args.get('filename')
    
    if not filename:
        return jsonify({"error": "Filename parameter is required"}), 400
    
    try:
        result = subprocess.check_output(f'cat {filename}', shell=True, text=True)
        return jsonify({"content": result.decode('utf-8')})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Failed to read file: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
bash
python app.py
http://localhost:5000/readfile?filename=example.txt