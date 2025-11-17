bash
pip install flask
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def proxy():
    url = request.args.get('url')  # Get the URL parameter from the query string
    
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        response = requests.get(url)
        data = response.text
        status_code = response.status_code
        
        # Return the fetched data with the original status code
        return jsonify({"data": data, "status_code": status_code})
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
bash
curl "http://localhost:5000/proxy?url=https://jsonplaceholder.typicode.com/posts"