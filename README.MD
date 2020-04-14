# SQLITECLOSEDHELPER

Description: This library helps you to manage your sqlite database easily without any query

### How to install?

``pip install sqliteclosedhelper``



### How to use ?

#### Creating a database file 
```
from sqliteclosedhelper import *
db=DB("filename.db")
```

#### Creating a table
```
db.createTable(tablename="books",fields={"id":TEXT+PRIMARY,"name":TEXT,"price":INTEGER}) #creates a table if not created
```
#### Insert a field
```
db.insert(tablename="books",data={"id":"a1x","name":"Book1","price":100})
```

#### Updating a field
```
db.update(tablename="books",data={"price":120},where={"id":"a1x","name":"Book1"},whattype=AND)
```
#### Get a field
```
print(db.get(tablename="books",where={"name":"Book1","price":120},whattype=AND))
```
#### Delete a field
```
db.delete("books",where={"name":"Book1","price":120},whattype=AND)
```
#### Delete all field
```
db.deleteAll("books")
```
#### Get all field
```
print(db.getAll("books"))
```
