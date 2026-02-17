from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to Flask web server!"

# GET method endpoint
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})

# POST method endpoint
@app.route('/users', methods=['POST'])
def add_users():
    data = request.get_json()
    return jsonify({
        "message": "User created successfully",
        "user": data
    }), 201

# PUT request
@app.route('/users/<int:id>', methods=['PUT'])
def update_users(id):
    return jsonify({"message": f"User {id} updated successfully"})

# DELETE request
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    return jsonify({"message": f"User {id} deleted successfully"})

# PATCH request
@app.route('/users/<int:id>', methods=['PATCH'])
def patch_user(id):
    data = request.get_json()
    return jsonify({
        "message": "User updated partially",
        "user_id": id,
        "updated_fields": data
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
