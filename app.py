from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app =  Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users-db'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def retrieveAll():
    holder = []
    currentCollection = mongo.db.users
    for user in currentCollection.find():
        holder.append({'id': user['id'], 'name': user['name'], 'email': user['email'], 'password': user['password']})
        # holder.append({'1':'1'})
        # print(user)
    return jsonify(holder)




@app.route('/<id>', methods=['GET'])
def retrieveFromId(id):
    currentCollection = mongo.db.users
    data = currentCollection.find_one({"id": id})
    if data:
        return jsonify({'id': data['id'], 'name': data['name'], 'email': data['email'], 'password': data['password']})
    else:
        return jsonify({'message': 'User not found'})



@app.route('/postData', methods = ['POST'])
def postData():
    currentCollection = mongo.db.users
    id = request.json['id']
    name = request.json['name']
    mail = request.json['email']
    password = request.json['password']

    if request.method == 'POST':
        currentCollection.insert_one({'id': id, 'name': name, 'email': mail, 'password': password})
        return jsonify({'message': 'User created successfully', 'id': id, 'name': name, 'email': mail, 'password': password})
    else:
        return jsonify({'message': 'Error'})











if __name__ == '__main__':
    app.run(debug=True)