from flask import Flask, request, abort
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json  # Assuming the incoming payload is in JSON format

    if 'action' not in data:
        return abort(400, "Missing action field")

    action = data['action']

    try:
        execute_command(action)
        return "Action processed successfully", 200
    except Exception as e:
        return str(e), 500

def execute_command(action):
    if action == 'start':
        subprocess.run(['echo', 'Starting process'], check=True)
    elif action == 'stop':
        subprocess.run(['echo', 'Stopping process'], check=True)
    elif action == 'restart':
        subprocess.run(['echo', 'Restarting process'], check=True)
    else:
        raise ValueError(f"Unknown action: {action}")

if __name__ == '__main__':
    app.run(port=5000)  # Run the Flask application on port 5000
bash
curl -X POST http://localhost:5000/webhook -H "Content-Type: application/json" -d '{"action": "start"}'