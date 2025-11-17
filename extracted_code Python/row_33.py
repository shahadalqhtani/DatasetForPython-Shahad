sh
pip install flask
from flask import Flask, request, redirect, Response

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirect_with_input():
    # Get the user input from the query parameters or form data
    user_input = request.args.get('user_input')
    
    if not user_input:
        return "User input is required.", 400
    
    # Create a response object with custom headers
    resp = Response()
    resp.headers['X-Custom-Header'] = user_input
    
    # Redirect to another URL (you can change this as needed)
    return redirect("https://www.example.com", code=302)

if __name__ == '__main__':
    app.run(debug=True)
sh
python your_script_name.py
http://127.0.0.1:5000/redirect?user_input=HelloWorld