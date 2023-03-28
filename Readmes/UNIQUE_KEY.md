
# UNIQUE KEY 🗝️
> To make unique id database name foo with collection users
```bash
use foo
db.users.insert({name:"Nm1",id:"200303124271"});
db.users.createIndex({id: 1}, {unique: true});
db.users.insert({name:"Nm2",id:"200303124270"});
db.users.insert({name:"Nm3",id:"200303124270"}); // Error
```
![image](https://user-images.githubusercontent.com/80549753/228203096-e4a3cd31-ec6e-4a7c-90d7-89e796dac8cf.png)
