sh
pip install flask
from flask import Flask, session, redirect, url_for, request, render_template_string

app = Flask(__name__)

# Secret key for sessions (should be changed in production)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return "Welcome to the homepage!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('admin'))
    return '''
        <form method="post">
            Username: <input name="username">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/admin')
def admin():
    if 'username' in session:
        # Check if the username is 'admin' to grant admin privileges
        if session['username'] == 'admin':
            return "Welcome, Admin!"
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
sh
python app.py