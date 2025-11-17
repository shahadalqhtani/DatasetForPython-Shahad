from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)

# Define the directory where your files are stored
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = request.form['filename']  # Assuming the form contains a field named 'filename'
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        return f"File {filename} uploaded successfully."
    else:
        return "Failed to upload file."

@app.route('/download')
def download_file():
    user_filename = request.args.get('filename', '')  # Get filename from query parameters
    if not user_filename:
        return "No filename provided"
    file_path = os.path.join(UPLOAD_FOLDER, user_filename)
    if not os.path.exists(file_path):
        return f"File {user_filename} does not exist."
    return send_from_directory(UPLOAD_FOLDER, user_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
html
  <form action="http://localhost:5000/upload" method="post" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="text" name="filename" placeholder="Enter filename">
      <input type="submit" value="Upload">
  </form>