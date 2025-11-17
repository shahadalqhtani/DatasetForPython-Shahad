sh
pip install flask
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/set-cookie')
def set_cookie():
    # Create a response object with a Set-Cookie header
    resp = make_response("Hello, World!")
    
    # Set the insecure domain and path values for the cookie
    resp.set_cookie('example_cookie', 'insecure_value', domain='localhost', path='/')
    
    return resp

if __name__ == '__main__':
    app.run(debug=True)