import sqlite3

class LeagueDBCommandBase:
        
    def __init__(self, sqliteConnection:sqlite3.Connection):
        self.sqliteConnection:sqlite3.Connection = sqliteConnection

    def sendVoidCommand(self, query:str, args:tuple=()):
        cursor = self.sqliteConnection.cursor()
        cursor.execute(query,args)
        cursor.close()
        self.sqliteConnection.commit()

    def sendQueryCommand(self, query:str, args:tuple=()):
        cursor = self.sqliteConnection.cursor()
        cursor.execute(query,args)
        result = cursor.fetchall()
        cursor.close()
        self.sqliteConnection.commit()
        return result

    def sendScalarCommand(self, query:str, args:tuple=()):
        cursor = self.sqliteConnection.cursor()
        cursor.execute(query,args)
        result = cursor.fetchone()
        cursor.close()
        self.sqliteConnection.commit()
        return result