from datetime import datetime

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

    def azureAddData(self):
        currenttime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.curosr.execute(f"INSERT into guestbook(name,text,date) values('Mateusz','Świetna stronka','{currenttime}')")
        self.conn.commit()



