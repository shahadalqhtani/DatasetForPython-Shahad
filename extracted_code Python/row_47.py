sh
pip install flask
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/privileged-operation', methods=['POST'])
def privileged_operation():
    data = request.get_json()
    
    # Check if the client sent a JSON payload with an 'is_admin' field
    is_admin = data.get('is_admin')
    
    if is_admin is None:
        return jsonify({"error": "Missing 'is_admin' field in the request"}), 400
    
    # Allow or deny privileged operations based on the value of 'is_admin'
    if is_admin:
        # Perform privileged operation here
        result = {"status": "Privileged operation allowed"}
    else:
        result = {"status": "Access denied. You are not an admin."}
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
sh
curl -X POST http://localhost:5000/privileged-operation -H "Content-Type:application/json" -d '{"is_admin": true}'