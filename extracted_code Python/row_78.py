bash
pip install flask flask-session
from flask import Flask, session, request
from flask_session import Session
import os

app = Flask(__name__)

# Set a secret key for signing the session cookies. This should be changed in a production environment!
app.config['SECRET_KEY'] = os.urandom(24)

# Configure session to use filesystem (or another backend) to store sessions
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    # Set a session variable
    session['value'] = request.host  # You can set any value you want in the session
    return f"Session value set to: {session['value']}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)