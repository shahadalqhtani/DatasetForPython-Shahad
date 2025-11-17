bash
   pip install Flask requests
from flask import Flask, request, redirect, url_for, render_template_string
import requests
import os

app = Flask(__name__)

# Client ID and client secret for demonstration purposes only
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
AUTH_URL = 'https://accounts.example.com/oauth/authorize'  # Replace with actual authorization URL
TOKEN_URL = 'https://accounts.example.com/oauth/token'     # Replace with actual token URL
REDIRECT_URI = 'http://localhost:5000/callback'            # This should match what the client provides

# In-memory storage for tokens (for demonstration purposes only)
tokens = {}

@app.route('/')
def index():
    return render_template_string('''
        <a href="{{ url_for("authorize") }}">Authorize</a>
    ''')

@app.route('/authorize')
def authorize():
    # Generate the authorization URL and redirect to it
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'scope': 'read write'
    }
    return redirect(f"{AUTH_URL}?{requests.compat.urlencode(params)}")

@app.route('/callback')
def callback():
    # Extract the authorization code from the query parameters
    auth_code = request.args.get('code')
    if not auth_code:
        return "Authorization failed.", 400

    # Exchange the authorization code for a token
    response = requests.post(TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'code': auth_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    })

    if response.status_code != 200:
        return f"Error fetching token: {response.json()}", response.status_code

    # Store the token (for demonstration purposes only)
    tokens['user'] = response.json()
    return "Authorization successful! Token stored.", 200

if __name__ == '__main__':
    app.run(port=5000)