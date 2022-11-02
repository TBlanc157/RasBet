import mysql.connector
from DBConstants import DBConstants

class Database:
    def __init__(self):
        self._conn = mysql.connector.connect(host = DBConstants.host, 
                                             port = DBConstants.port, 
                                             user = DBConstants.username, 
                                             password = DBConstants.password, 
                                             database = DBConstants.database) 
        self._cursor = self._conn.cursor(buffered=True,named_tuple=True)

    def __enter__(self):
        return self

    def __exit__(self):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def lastrowid(self):
        return self.cursor.lastrowid

    def close(self, commit=True):
        if commit:
            self.commit()
        self.cursor.close()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.fetchall()
