bash
pip install flask
from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and file.filename.endswith('.xml'):
        try:
            # Parse the XML content
            tree = ET.fromstring(file.read())
            
            # You can now manipulate or extract data from the parsed XML
            root = tree.getroot()
            
            # Example: Extract all tags and their values
            xml_data = {}
            for elem in root.iter():
                if elem.tag not in xml_data:
                    xml_data[elem.tag] = []
                xml_data[elem.tag].append(elem.text)
            
            return jsonify({"parsed_xml": xml_data}), 200
        except ET.ParseError as e:
            return jsonify({"error": "XML parsing error", "details": str(e)}), 400
    else:
        return jsonify({"error": "Unsupported file type"}), 400

if __name__ == '__main__':
    app.run(debug=True)
bash
python app.py