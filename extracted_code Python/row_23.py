bash
pip install flask
bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
bash
   pip install flask
from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

# Function to get the database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route('/', methods=['GET'])
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

# Login route
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    conn = get_db_connection()
    user = conn.execute("SELECT id FROM users WHERE email=? AND pass=?", (email, password)).fetchone()
    conn.close()
    
    if user:
        session['user_id'] = user['id']
        return redirect(url_for('dashboard'))
    else:
        return "Invalid credentials"

# Dashboard route
@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user_id' in session:
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE id=?", (session['user_id'],)).fetchone()
        conn.close()
        return f"Welcome, {user['username']}!"
    else:
        return redirect(url_for('home'))

# Logout route
@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Set up the database (this is a simple example, not for production use)
    conn = get_db_connection()
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    
    app.run(debug=True)
sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    pass TEXT NOT NULL
);
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h1>Please login</h1>
    <form action="/login" method="post">
        Email: <input type="email" name="email"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>