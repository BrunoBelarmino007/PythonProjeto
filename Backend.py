import sqlite3 as sql

class TransactionObject():
    database   = "clientes.db"
    conn       = None
    cur        = None
    connected  = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur  = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms=None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False
        
    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False
        
def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            sobrenome TEXT,
            email TEXT,
            cpf TEXT UNIQUE)
        """)
    trans.persist()
    trans.disconnect()

def cpf_exists(cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT COUNT(*) FROM clientes WHERE cpf = ?", (cpf,))
    count = trans.fetchall()[0][0]
    trans.disconnect()
    return count > 0

initDB()
