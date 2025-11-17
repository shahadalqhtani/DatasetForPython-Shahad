bash
pip install flask
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# In-memory storage for simplicity (not recommended for production)
users = {'user1': 'password1', 'user2': 'password2'}
authenticated_users = {}

def authenticate():
    cookie = request.cookies.get('session')
    if not cookie:
        return False, None
    user = authenticated_users.get(cookie)
    if user is None:
        return False, None
    return True, user

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username] == password:
        session_id = app.secret_key + username  # Simple session ID creation
        response = make_response(jsonify({'message': 'Login successful'}))
        authenticated_users[session_id] = username
        response.set_cookie('session', session_id)
        return response
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/change-state', methods=['POST'])
def change_state():
    is_authenticated, user = authenticate()
    if not is_authenticated:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.json
    new_state = data.get('new_state')
    
    # Here you would update the state in your storage (e.g., a database)
    # For simplicity, we'll just return the current state with modifications
    if new_state is not None:
        authenticated_users[request.cookies.get('session')] = new_state
        return jsonify({'message': 'State updated', 'new_state': new_state})
    else:
        return jsonify({'error': 'Missing new state'}), 400

@app.route('/logout', methods=['POST'])
def logout():
    cookie = request.cookies.get('session')
    if cookie:
        del authenticated_users[cookie]
    response = make_response(jsonify({'message': 'Logout successful'}))
    response.set_cookie('session', '', expires=0)
    return response

@app.route('/status', methods=['GET'])
def status():
    is_authenticated, user = authenticate()
    if not is_authenticated:
        return jsonify({'authenticated': False}), 401
    else:
        return jsonify({'authenticated': True, 'user': user})

if __name__ == '__main__':
    app.run(debug=True)
bash
python app.py