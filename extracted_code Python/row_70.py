bash
pip install flask
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/redirect')
def redirect_to_next():
    next_param = request.args.get('next', None)
    if next_param:
        return redirect(url_for('.redirect_to_next', next=request.args.get('next')))
    else:
        return "No next parameter provided."

if __name__ == '__main__':
    app.run(debug=True)
bash
   python redirect_endpoint.py