import sqlite3
from datetime import datetime

"""
TODO: Perhaps make this class static?
"""
class Logs:
    def __init__(self, filename="storage/subreddits.db"):
        self.filename = filename
        self._create_default_table()
    
    def connect(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        return conn, curs

    def _create_default_table(self):
        conn, c = self.connect()

        create_log_table = ''' CREATE TABLE IF NOT EXISTS logs
                               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                               message TEXT NOT NULL, 
                               date_added TEXT NOT NULL)'''
        c.execute(create_log_table)
        conn.commit()
        conn.close()

        if not self.contains_records():
            self.insert_log('Created log table')
    
    def get_date_now(self):
        return str(datetime.now())
    
    def insert_log(self, message):
        conn, c = self.connect()
        argument = (message, self.get_date_now())

        create_log = '''INSERT INTO logs(message, date_added)
                      VALUES(?, ?)'''
        c.execute(create_log, argument)
        conn.commit()
        conn.close()
    
    def contains_records(self):
        conn, c = self.connect()
        c.execute('''SELECT COUNT(*) FROM logs''')
        result = c.fetchall()
        if result[0][0] == 0:
            return False
        else:
            return True
    
    def print_all(self):
        conn, c = self.connect()
        c.execute('''SELECT * FROM logs''')
        result = c.fetchall()
        for r in result:
            print(r)

if __name__ == "__main__":
    l = Logs()
    l.print_all()