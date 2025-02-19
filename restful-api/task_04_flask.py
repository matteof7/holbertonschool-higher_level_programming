from flask import Flask, jsonify,  request
app = Flask(__name__)

users = {
"jane": {"username": "Jane", "age": 28, "city": "Los Angeles"},
"john", {"username": "John", "age": 30, "city": "New York"}

}

@app.route("/")