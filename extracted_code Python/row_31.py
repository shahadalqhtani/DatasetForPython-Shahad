from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/location', methods=['GET'])
def location():
    # Get the 'url' parameter from the query string
    url = request.args.get('url')
    
    if not url:
        return "Missing 'url' parameter", 400
    
    # Create a response with a Location header
    response = make_response("Redirecting to URL...", 302)
    response.headers['Location'] = url
    
    return response

if __name__ == '__main__':
    app.run(debug=True)