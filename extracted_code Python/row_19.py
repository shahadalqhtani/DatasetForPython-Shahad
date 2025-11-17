bash
pip install flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/comment', methods=['GET'])
def return_comment():
    user_comment = request.args.get('user_comment', 'No comment provided')
    return f'<p>{user_comment}</p>'

if __name__ == '__main__':
    app.run(debug=True)
http://127.0.0.1:5000/comment?user_comment=Hello%20World