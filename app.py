from sqliteclosedhelper import *
db=DB("filename.db")

db.createTable(tablename="books",fields={"id":TEXT+PRIMARY,"name":TEXT,"price":INTEGER}) #creates a table if not created

db.insert(tablename="books",data={"id":"a1x","name":"Book1","price":100})

db.update(tablename="books",data={"price":120},where={"id":"a1x","name":"Book1"},whattype=AND)

print(db.get(tablename="books",where={"name":"Book1","price":120},whattype=AND))

db.delete("books",where={"name":"Book1","price":120},whattype=AND)

db.deleteAll("books")

print(db.getAll("books"))

