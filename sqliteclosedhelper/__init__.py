import sqlite3

PRIMARY = " PRIMARY KEY "
TEXT = " TEXT "
INTEGER = " INTEGER "
REAL = " REAL "
INTEGER_NOT_NULL = " INTEGER NOT NULL "
INTEGER_NOT_NULL_AUTOINCREMENT = " INTEGER NOT NULL AUTOINCREMENT "
INTEGER_UNIQUE = " INTEGER UNIQUE "
TEXT_UNIQUE = " TEXT UNIQUE "
TEXT_NOT_NULL = " TEXT NOT NULL "
TEXT_PRIMARY = " TEXT PRIMARY "
INTEGER_PRIMARY = " INTEGER PRIMARY "
INTEGER_PRIMARY_AUTOINCREMENT = " INTEGER PRIMARY AUTOINCREMENT "
AND=" AND "
OR=" OR "

class DB:
    def __init__(self, dbpath):
        self.conn = sqlite3.connect(dbpath)

    def __generateValues(self,data):
        _values=[]
        for x in data:
            _values.append("'"+data[x].replace("'","''")+"'" if type(data[x]) is str else str(data[x]))
        return ",".join(_values)

    def createTable(self, tablename, fields):
        fieldtype = ""
        for x in fields:
            fieldtype += x + " " + fields[x] + ","
        fieldtype = fieldtype[:-1]
        self.conn.execute("CREATE  TABLE if not exists  " + tablename + " (" + fieldtype + ")")
        self.conn.commit()

    def insert(self, tablename, data):
        fieldnames = ",".join(data)
        values=self.__generateValues(data)
        self.conn.execute("INSERT INTO " + tablename + " (" + fieldnames + ") VALUES (" + values + ");")
        self.conn.commit()

    def update(self, tablename, data, where,whattype):
        fieldnames = ",".join([x+"="+("'"+data[x]+"'" if type(data[x]) is str else str(data[x])) for x in data])
        where =  whattype.join([x+"="+("'"+where[x]+"'" if type(where[x]) is str else str(where[x])) for x in where])
        # print("UPDATE " + tablename + " SET " + fieldnames + " WHERE " + where)
        self.conn.execute("UPDATE " + tablename + " SET " + fieldnames + " WHERE " + where)
        self.conn.commit()

    def deleteAll(self, tablename):
        self.conn.execute("delete from " + tablename)
        self.conn.commit()

    def parseData(self,tablename,data):
        fields = [x[1] for x in tuple(self.conn.execute("PRAGMA table_info(" + tablename + ")").fetchall())]
        newData=[]
        for x in data:
            _data={}
            for i,y in enumerate(fields):
                _data[y]=x[i]
            newData.append(_data)
        return newData
    
    def getAll(self, tablename):
        return self.parseData(tablename,self.conn.execute("select * from " + tablename).fetchall())

    def get(self, tablename, where, **params):
        orand = " " + params['whattype'] + " " if 'what' in params else " AND "
        where1 = ""
        for x in where:
            where[x] = "'" + where[x] + "'" if type(where[x]) is str else where[x]
            where1 += str(x) + " = " + str(where[x]) + orand
        where1 = where1[:-3] if orand is " OR " else where1[:-4]
        return self.parseData(tablename,self.conn.execute("SELECT * FROM " + tablename + " WHERE " + where1).fetchall())

    def delete(self, tablename, where, **params):
        orand = " " + params['whattype'] + " " if 'what' in params else " AND "
        where1 = ""
        for x in where:
            where[x] = "'" + where[x] + "'" if type(where[x]) is str else where[x]
            where1 += str(x) + " = " + str(where[x]) + orand
        where1 = where1[:-3] if orand is " OR " else where1[:-4]
        self.conn.execute("DELETE FROM " + tablename + " WHERE " + where1).fetchall()
        self.conn.commit()

    def execute(self, query):
        result = self.conn.execute(query)
        self.conn.commit()
        return result

