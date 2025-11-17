bash
pip install flask
from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)

# Hardcoded credentials for demonstration purposes only!
VALID_USERS = {
    "user1": "pass1",
    "user2": "pass2"
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in VALID_USERS and VALID_USERS[username] == password:
        return redirect(url_for('user'))
    else:
        return "Invalid credentials", 401

@app.route('/user')
def user():
    return "Welcome, logged-in user!"

if __name__ == '__main__':
    app.run(debug=True)
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h1>Please Log In</h1>
    <form action="/login" method="post">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>