> To make unique id database name foo with collection users
```bash
use foo
db.users.insert({name:"Nm1",id:"200303124271"});
db.users.createIndex({id: 1}, {unique: true});
db.users.insert({name:"Nm2",id:"200303124270"});
db.users.insert({name:"Nm3",id:"200303124270"}); // Error
```