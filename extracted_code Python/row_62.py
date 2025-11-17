from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user store
users = {
    '1': {'email': 'user@example.com'}
}

@app.route('/change_email', methods=['GET'])
def change_email():
    user_id = request.args.get('user_id')
    new_email = request.args.get('new_email')
    
    if not user_id or not new_email:
        return jsonify({'error': 'Missing user_id or new_email'}), 400
    
    if user_id in users:
        users[user_id]['email'] = new_email
        return jsonify({'message': 'Email changed successfully', 'new_email': new_email}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)