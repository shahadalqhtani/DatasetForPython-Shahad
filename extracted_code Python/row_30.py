bash
pip install flask
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ensure uploads directory exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        
        # Read the contents of the uploaded file
        with open(filename, 'r') as f:
            code = f.read()
        
        try:
            # Execute the plugin code
            exec(code)
            return jsonify({"status": "success", "message": "Plugin executed successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "File type not allowed"}), 400

def allowed_file(filename):
    # Allow only certain file extensions, you can customize this as needed
    ALLOWED_EXTENSIONS = {'txt'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)