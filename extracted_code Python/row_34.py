bash
pip install flask
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/put-in-header', methods=['POST'])
def put_in_header():
    # Get user input from the POST request
    data = request.data
    
    # Create a Content-Disposition header with the received data
    content_disposition = f'attachment; filename="{data.decode("utf-8")}"'
    
    # Create a Flask Response object and set its headers
    response = Response(data)
    response.headers['Content-Disposition'] = content_disposition
    
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)