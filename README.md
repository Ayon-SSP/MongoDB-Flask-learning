# Learning MongoDB Flask

![image](https://user-images.githubusercontent.com/80549753/228181800-c402bc96-93dc-4f92-99d1-b00c327f9f55.png)

<!-- ![image](https://user-images.githubusercontent.com/80549753/228182747-ef0bcff4-89f4-479e-ab49-e96921a49e87.png) -->

# DataBase -> Collection -> Document

### MongoDB on  Ubuntu
```bash
sudo apt-get install mongodb
```
### To start Service
```bash
sudo service mongodb start
```
### To stop Service
```bash
sudo service mongodb stop
```
### To restart Service
```bash
sudo service mongodb restart
```
### To check status of Service
```bash
sudo service mongodb status
```

## MongoDB shell
```bash
mongo
```
```bash
### To show all databases
show dbs

### to show curr the databases
db
### To create a database or use a database
use <database_name>
### To create a collection
db.createCollection("<collection_name>")

### delete a collection
db.<collection_name>.drop()

### To insert a document
db.<collection_name>.insertOne({<key>:<value>})

### To insert multiple documents
db.<collection_name>.insertMany([{<key>:<value>},{<key>:<value>},{<key>:<value>}])

### To find a document
db.<collection_name>.find({<key>:<value>})

### To find all documents
db.<collection_name>.find()

### To find a document with a specific key
db.<collection_name>.find({<key>:{$exists:true}})

### To find a document with a specific key and value
db.<collection_name>.find({<key>:{$exists:true},<key>:<value>})

### To find a document with a specific key and value
db.<collection_name>.find({<key>:{$exists:true},<key>:<value>})


### To find a document with a specific key and value
db.<collection_name>.find({<key>:{$exists:true},<key>:<value>})

### To find a document with a specific key and value
db.<collection_name>.find({<key>:{$exists:true},<key>:<value>})

### To find a document with a specific key and value
db.<collection_name>.find({<key>:{$exists:true},<key>:<value>})

### To find a document with a specific key and value
db.<collection_name>.find({<key>:{$exists:true},<key>:<value>})

### To find a document with a specific key and value
db.<collection_name>.find({<key>:{$exists:true},<key>:<value>})
```

Eg:
```bash
use test
db.createCollection("users")
db.users.insertOne({"name":"John","age":20})
db.users.insertMany([{"name":"John","age":20},{"name":"John","age":20},{"name":"John","age":20}])
db.users.find({"name":"John"})
db.users.find()
db.users.find({"name":{$exists:true}})
db.users.find({"name":{$exists:true},"age":20})
db.mycollection.remove({age: {$gt: 30}})

db.users.insertMany([{"name":"John","age":20},{"name":"John","age":20},{"name":"John","age":20}])
db.users.fine().limit(2);
db.users.fine().sort({name:-1}).limit(3);
db.users.fine().sort({age: 1, name:-1 }).limit(3).skip(1);

db.users.find({name: /^J/}) // starts with J
db.users.find({name: /n$/}) // ends with n
db.users.find({name: "AYON"}, {name: 1, age: 1, _id: 0}) // only name and age & don't give me id


db.users.remove({"id": {$eq: "200303124271"}}) // to remove a document
### to show the collections
show collections
### delete a collection
db.<collection_name>.drop()
```
```
sudo apt-get install mongodb
```
### To start Service
```
sudo service mongodb start
```
![image](https://user-images.githubusercontent.com/80549753/228185731-b8774702-5ad9-4c74-91f1-3877944623fc.png)
![image](https://user-images.githubusercontent.com/80549753/228186313-bde7f4de-0884-45f2-8752-f5a35c82e86b.png)

![image](https://user-images.githubusercontent.com/80549753/228191657-300c6fad-d484-44ae-af2c-e90da6d6ba30.png)


### To Make a Unique ID [Link](https://github.com/Ayon-SSP/MongoDB-Flask/blob/master/Readmes/UNIQUE_KEY.md)

# UNIQUE KEY 🗝️
> To make unique id database name foo with collection users
> To Make a Unique ID [Link](https://github.com/Ayon-SSP/MongoDB-Flask/blob/master/Readmes/UNIQUE_KEY.md)
```bash
use foo
db.users.insert({name:"Nm1",id:"200303124271"});
db.users.createIndex({id: 1}, {unique: true});
db.users.insert({name:"Nm2",id:"200303124270"});
db.users.insert({name:"Nm3",id:"200303124270"}); // Error

db.users.getIndexes() // to check existing Keys
```
![image](https://user-images.githubusercontent.com/80549753/228203096-e4a3cd31-ec6e-4a7c-90d7-89e796dac8cf.png)


## Cors Error 💀
```python
from flask_cors import CORS, cross_origin
cors = CORS(app)

app.config['CORS_Headers'] = 'Content-Type'
# GET /users/<id> - Returns the user with the specified ID.
@app.route('/<id>', methods=['GET'])
@cross_origin()
def retrieveFromId(id):
    currentCollection = mongo.db.users
    data = currentCollection.find_one({"id": id})
    if data:
        return jsonify({'id': data['id'], 'name': data['name'], 'email': data['email'], 'password': data['password']})
    else:
        return jsonify({'message': 'User not found'})
```
## if error
```
❯ mongo
MongoDB shell version v3.6.8
connecting to: mongodb://127.0.0.1:27017
2023-03-30T08:32:06.732+0530 W NETWORK  [thread1] Failed to connect to 127.0.0.1:27017, in(checking socket for error after poll), reason: Connection refused
2023-03-30T08:32:06.733+0530 E QUERY    [thread1] Error: couldn't connect to server 127.0.0.1:27017, connection attempt failed :
connect@src/mongo/shell/mongo.js:257:13
@(connect):1:6
exception: connect failed
```
> Restart the mongodb or maybe your window mongodb is using 27017. change the port
```bash
sudo service mongodb restart
mongo --port <port_number>
```
