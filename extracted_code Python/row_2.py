from flask import Flask, jsonify
import platform

app = Flask(__name__)

@app.route('/admin/system-info', methods=['GET'])
def get_system_info():
    sys_info = {
        'platform': platform.platform(),
        'python_version': platform.python_version(),
        'system': platform.system(),
        'release': platform.release(),
        'machine': platform.machine()
    }
    return jsonify(sys_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)