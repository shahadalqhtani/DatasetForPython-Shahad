bash
pip install flask pyjwt
from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

# Secret key for JWT encoding and decoding
SECRET_KEY = 'your-256-bit-secret'

# Endpoint to authenticate and get a JWT token
@app.route('/auth', methods=['POST'])
def create_token():
    username = request.json.get('username')
    password = request.json.get('password')

    # Here you would typically validate the username and password against some backend storage
    if username == 'admin' and password == 'secret':
        payload = {
            'sub': username,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Middleware to authenticate JWT tokens
def jwt_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing'}), 403
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            # You can add more validation here if needed
        except (jwt.InvalidTokenError, jwt.ExpiredSignatureError):
            return jsonify({'error': 'Invalid token'}), 403
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

# Protected endpoint that requires authentication
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    user = jwt.decode(request.headers['Authorization'], SECRET_KEY, algorithms=['HS256'])
    return jsonify({'user': user}), 200

if __name__ == '__main__':
    app.run(debug=True)
bash
python your_script_name.py
bash
curl -X POST http://127.0.0.1:5000/auth -H "Content-Type: application/json" -d '{"username": "admin", "password": "secret"}'
bash
curl http://127.0.0.1:5000/protected -H "Authorization: Bearer YOUR_JWT_TOKEN"