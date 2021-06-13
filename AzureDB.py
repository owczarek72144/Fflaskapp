

import pypyodbc
import azurecred


class AzureDB:
    dsn = 'DRIVER=' + azurecred.AZDBDRIVER + ';SERVER=' + azurecred.AZDBSERVER + ';PORT=1433;DATABASE=' + azurecred.AZDBNAME + ';UID=' + azurecred.AZDBUSER + ';PWD=' + azurecred.AZDBPW

    def __init__(self):
        self.conn = pypyodbc.connect(self.dsn)
        self.curosr = self.conn.cursor()

    def finalize(self):
        if self.conn:
            self.conn.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finalize()

    def __enter__(self):
        return self

    def azureGetAllData(self):
        try:
            self.curosr.execute("SELECT * from guestbook")
            allEntry = self.curosr.fetchall()
            return allEntry
        except pypyodbc.DatabaseError as exception:
            print('Failed to execute query')
            print(exception)
            exit(1)

    def azureAddData(self, name, message,currenttime):
        self.curosr.execute(f"INSERT into guestbook(name,text,date) values('{name}','{message}','{currenttime}')")
        self.conn.commit()

    def azureDeleteEntry(self, id):
        self.curosr.execute(f"DELETE FROM guestbook WHERE entryid ='{id}'")
        self.conn.commit()

    def auzreUpdateEntry(self,id, name,message):
        self.curosr.execute(f"UPDATE guestbook SET name='{name}',text='{message}' WHERE entryid='{id}'")
        self.conn.commit()

    def azureGetRecord(self,id):
        try:
            self.curosr.execute(f"SELECT * from guestbook WHERE entryid = {id}")
            entry = self.curosr.fetchall()
            return entry
        except pypyodbc.DatabaseError as exception:
            print('Failed to execute query')
            print(exception)
            exit(1)
