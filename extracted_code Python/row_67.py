sh
pip install flask
from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/unpickle', methods=['POST'])
def unpickle_data():
    try:
        # Load data from the POST request
        data = request.data
        if not data:
            return "No data received", 400
        
        # Unpickle the data
        loaded_data = pickle.loads(data)
        
        # Return the unpickled data
        return f"Unpickled Data: {loaded_data}", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
sh
curl -X POST -d "H4sIAAAAAAAAA..." http://127.0.0.1:5000/unpickle