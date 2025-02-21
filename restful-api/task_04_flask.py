from flask import Flask, jsonify, request

# Initialiser l'application Flask
app = Flask(__name__)

# Stocker les utilisateurs en mémoire
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Endpoint racine
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Endpoint pour vérifier le statut
@app.route("/status")
def status():
    return "OK"

# Endpoint pour récupérer tous les noms d'utilisateur
@app.route("/data")
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)

# Endpoint pour récupérer un utilisateur spécifique
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint pour ajouter un nouvel utilisateur
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Ajouter l'utilisateur
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

# Lancer le serveur Flask
if __name__ == "__main__":
    app.run(debug=True)
