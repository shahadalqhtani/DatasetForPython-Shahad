bash
pip install flask
from flask import Flask, request, redirect, url_for, send_from_directory
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp'  # All files will be uploaded here
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # Extensions allowed for upload

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filename = str(uuid.uuid4()) + '_' + file.filename  # Generate a unique name for the file
        file.save(os.path.join(UPLOAD_FOLDER, filename))  # Save the file to /tmp with a random name
        return 'File successfully uploaded!'
    else:
        return 'Invalid file type.'

if __name__ == '__main__':
    app.run(debug=True)