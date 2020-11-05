import sqlite3

class Database:
    def __init__(self, filename="storage/subreddits.db"):
        self.filename = filename
        self.conn = sqlite3.connect(self.filename)

    def _create_default_tables(self):
        c = self.conn.cursor()

        create_log_table = ''' CREATE TABLE IF NOT EXISTS logs
                               (message text, date_added text)'''

        create_sub_table = ''' CREATE TABLE IF NOT EXISTS subreddits
                           (subreddit text, date_added text) '''