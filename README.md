# Learning MongoDB Flask

![image](https://user-images.githubusercontent.com/80549753/228181800-c402bc96-93dc-4f92-99d1-b00c327f9f55.png)

<!-- ![image](https://user-images.githubusercontent.com/80549753/228182747-ef0bcff4-89f4-479e-ab49-e96921a49e87.png) -->

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


> To make unique id database name foo with collection users
```bash
use foo
db.users.insert({name:"Nm1",id:"200303124271"});
db.users.createIndex({id: 1}, {unique: true});
db.users.insert({name:"Nm2",id:"200303124270"});
db.users.insert({name:"Nm3",id:"200303124270"}); // Error
```
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

### to show the collectiosn
show collections
```
=======
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
