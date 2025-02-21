# type: ignore
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}

# Route racine
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Route pour obtenir le statut
@app.route('/status')
def status():
    return "OK"

# Route pour obtenir la liste des utilisateurs
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

# Route pour obtenir les détails d'un utilisateur spécifique
@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

# Route pour ajouter un nouvel utilisateur
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    
    # Vérifie si username est présent dans les données
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
