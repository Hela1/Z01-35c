import sqlite3

class DataBase():
    def __init__(self):
        self.conn = sqlite3.connect('serwerBD.db')
        self.c = self.conn.cursor()
        self.create_database()
        

    def create_database(self):
        sql = '''CREATE TABLE IF NOT EXISTS Users
             (login text UNIQUE, password text);'''
        self.c.execute(sql)
        self.conn.commit()
        sql = '''CREATE TABLE IF NOT EXISTS Msgs
             (user1 text, user2 text, msg text);'''
        self.c.execute(sql)

        self.conn.commit()

    def addUsr(self, login, password):
        sql = "INSERT INTO Users VALUES (?,?)"
        val = (login, password)
        self.c.execute(sql)
        self.conn.commit()

    def addMsg(self, user1, user2, text):
        sql = "INSERT INTO Msgs VALUES (?,?,?)"
        val = (user1, user2, text)
        self.c.execute(sql, val)
        self.conn.commit()
    
    def getMsg(self, user1, user2):
        sql = sql = "SELECT msg FROM Msgs WHERE user1 == ? AND user2 = ?"
        val = (user1, user2)
        self.c.execute(sql, val)
        self.conn.commit()
        return self.c.fetchall()

    def getUsr(self, login):
        tup = (login,)
        sql = "SELECT login, password FROM Users WHERE login == ?"
        self.c.execute(sql, tup)
        self.conn.commit()
        return self.c.fetchall()

if __name__ == "__main__":
    bd = DataBase()
    print(bd.getMsg("Jola", "Fasola"))

