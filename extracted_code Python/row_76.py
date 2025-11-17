from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # In a real application, you would validate the username and password here
    username = request.form['username']
    password = request.form['password']
    
    if username == "valid_user" and password == "valid_password":
        # Create a response with a session cookie
        response = make_response("Login successful!")
        response.set_cookie('session_token', 'your_secret_token', secure=False, httponly=False)
        return response
    else:
        return "Invalid login credentials", 401

if __name__ == '__main__':
    app.run(debug=True)
sh
python app.py