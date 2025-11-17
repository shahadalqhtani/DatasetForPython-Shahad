bash
pip install flask
from flask import Flask, send_file, request, abort
import os

app = Flask(__name__)

# Define a base path where your files are stored. This should be an absolute or relative path to your file directory.
BASE_PATH = '/path/to/your/files/'  # Update this with the actual path on your system

@app.route('/download')
def download():
    file_name = request.args.get('file')
    if not file_name:
        abort(400, "File name is required")
    
    full_path = os.path.join(BASE_PATH, file_name)
    
    # Check if the file exists in the specified path
    if not os.path.isfile(full_path):
        abort(404, "File not found")
    
    try:
        return send_file(full_path, as_attachment=True)
    except FileNotFoundError:
        abort(404, "File could not be read")

if __name__ == '__main__':
    app.run(debug=True)