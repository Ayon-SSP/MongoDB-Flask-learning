from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Set the MongoDB URI and database name
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
app.config['MONGO_DBNAME'] = 'mydatabase'

# Create a new PyMongo client and database instance
client = MongoClient(app.config['MONGO_URI'])
db = client[app.config['MONGO_DBNAME']]

# Define the User collection
users = db.users

# Define the REST API endpoints

# GET /users - Returns a list of all users
@app.route('/users', methods=['GET'])
def get_users():
    output = []
    for user in users.find():
        output.append({
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        })
    return jsonify({'result': output})

# GET /users/<id> - Returns the user with the specified ID
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = users.find_one({'_id': ObjectId(id)})
    if user:
        output = {
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        }
    else:
        output = {'result': 'User not found'}
    return jsonify(output)

# POST /users - Creates a new user with the specified data
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = {
        'name': data['name'],
        'email': data['email'],
        'password': data['password']
    }
    user_id = users.insert_one(user).inserted_id
    output = {'id': str(user_id)}
    return jsonify(output)

# PUT /users/<id> - Updates the user with the specified ID with the new data
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = {
        'name': data['name'],
        'email': data['email'],
        'password': data['password']
    }
    result = users.update_one({'_id': ObjectId(id)}, {'$set': user})
    if result.modified_count == 1:
        output = {'result': 'User updated successfully'}
    else:
        output = {'result': 'User not found'}
    return jsonify(output)

# DELETE /users
