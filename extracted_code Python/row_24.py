bash
pip install flask sqlalchemy flask-sqlalchemy
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)

# Configuration for SQLite database (in-memory for this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    city = db.Column(db.String(50))

# Helper function to concatenate user input into WHERE clauses
def build_where_clause(criteria):
    where_clauses = []
    if 'name' in criteria:
        where_clauses.append(User.name.like(f"%{criteria['name']}%"))
    if 'age' in criteria:
        where_clauses.append(User.age == int(criteria['age']))
    if 'city' in criteria:
        where_clauses.append(User.city.like(f"%{criteria['city']}%"))
    
    return or_(*where_clauses) if where_clauses else None

# Define the search endpoint
@app.route('/search', methods=['POST'])
def search():
    criteria = request.json.get('criteria')
    if not criteria:
        return jsonify({"error": "No criteria provided"}), 400
    
    where_clause = build_where_clause(criteria)
    if where_clause is None:
        users = User.query.all()
    else:
        users = User.query.filter(where_clause).all()
    
    result = [{'id': user.id, 'name': user.name, 'age': user.age, 'city': user.city} for user in users]
    return jsonify(result)

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create tables for our app
    app.run(debug=True)
bash
curl -X POST http://127.0.0.1:5000/search -H "Content-Type: application/json" -d '{"criteria": {"name": "John", "city": "New York"}}'