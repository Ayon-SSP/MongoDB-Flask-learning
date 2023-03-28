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



if __name__ == '__main__':
    app.run(debug=True)