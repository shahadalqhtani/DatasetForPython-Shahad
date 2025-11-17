sh
pip install flask
from flask import Flask, request, send_from_directory, abort
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'

# Ensure the uploads directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return abort(400, "No file part")
    
    file = request.files['file']
    
    if file.filename == '':
        return abort(400, "No selected file")
    
    if file:
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return f"File {filename} has been uploaded successfully."

@app.route('/files/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
sh
python app.py
sh
curl -X POST -F "file=@path/to/your/local/file" http://127.0.0.1:5000/upload