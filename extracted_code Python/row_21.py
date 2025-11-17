bash
pip install flask jinja2
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# In-memory storage for demonstration purposes
bio_store = {}

@app.route('/')
def home():
    return "Welcome to the Bio Storage API!"

@app.route('/store_bio', methods=['POST'])
def store_bio():
    data = request.get_json()  # Assuming JSON is used for payload
    bio = data.get('bio')
    if bio:
        bio_id = str(len(bio_store) + 1)
        bio_store[bio_id] = bio
        return f"Bio stored with ID {bio_id}"
    else:
        return "No bio provided", 400

@app.route('/profile/<bio_id>')
def profile(bio_id):
    bio = bio_store.get(bio_id)
    if bio is None:
        return "Bio not found", 404
    else:
        html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bio Profile</title>
</head>
<body>
    <h1>Biographical Information</h1>
    <p>{bio}</p>
</body>
</html>
"""
        return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
bash
python app.py
bash
curl -X POST -H "Content-Type: application/json" -d '{"bio": "This is a sample bio."}' http://127.0.0.1:5000/store_bio