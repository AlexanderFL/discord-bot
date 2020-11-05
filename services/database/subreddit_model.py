import sqlite3
from datetime import datetime

if __name__ == "__main__":
    from logs_model import Logs
else:
    from services.database.logs_model import Logs

class Subreddits:
    def __init__(self, filename="storage/subreddits.db"):
        self.filename = filename
        self._create_default_table()
    
    def connect(self):
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        return conn, curs

    def _create_default_table(self):
        conn, c = self.connect()

        create_sub_table = ''' CREATE TABLE IF NOT EXISTS subreddits
                               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                               subreddit TEXT NOT NULL)'''
        c.execute(create_sub_table)
        conn.commit()
        conn.close()
    
    def insert_subreddit(self, subreddit):
        logs = Logs()
        conn, c = self.connect()
        argument = (subreddit,)

        create_log = '''INSERT INTO subreddits(subreddit)
                      VALUES(?)'''
        c.execute(create_log, argument)
        conn.commit()
        conn.close()
        logs.insert_log(str(subreddit) + " was added")
    
    def remove_subreddit(self, subreddit):
        pass # TODO: Implement
    
    def print_all(self):
        conn, c = self.connect()
        c.execute('''SELECT * FROM subreddits''')
        result = c.fetchall()
        for r in result:
            print(r)

if __name__ == "__main__":
    s = Subreddits()
    s.print_all()