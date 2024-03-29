import sqlite3

if __name__ == "__main__":
    from logs_model import Logs
else:
    from models.logs_model import Logs


class Subreddits:
    def __init__(self, filename="storage/subreddits.db"):
        self.filename = filename
        self._create_default_table()

    def _connect(self):
        """
        Returns the connection and cursor to the database file
        """
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        return conn, curs

    def _create_default_table(self):
        """
        Creates the table if it does not exists within the database file
        """
        conn, c = self._connect()

        create_sub_table = ''' CREATE TABLE IF NOT EXISTS subreddits
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                               subreddit TEXT NOT NULL)'''
        c.execute(create_sub_table)
        conn.commit()
        conn.close()

    def insert_subreddit(self, subreddit: str):
        """
        Insert a subreddit into the table from the given string parameter
        """
        logs = Logs()
        conn, c = self._connect()
        argument = (subreddit,)

        insert_sub = '''INSERT INTO subreddits(subreddit)
                      VALUES(?)'''
        c.execute(insert_sub, argument)
        conn.commit()
        conn.close()
        logs.insert_log(str(subreddit) + " was added")

    def remove_subreddit(self, subreddit: str):
        """
        Remove a subreddit from the table from the given string parameter
        """
        logs = Logs()
        conn, c = self._connect()
        argument = (subreddit, )

        remove_sub = '''DELETE FROM subreddits WHERE subreddit=? '''
        c.execute(remove_sub, argument)
        conn.commit()
        conn.close()
        logs.insert_log(str(subreddit) + " was removed")

    def fetch_all_subreddits(self):
        """
        Fetches all of the stored subreddits and returns them in a list
        """
        conn, c = self._connect()
        c.execute('''SELECT * FROM subreddits''')
        sub_list = []
        results = c.fetchall()
        for result in results:
            sub_list.append(result[1])
        return sub_list


if __name__ == "__main__":
    subsreddits = Subreddits()
    # s.insert_subreddit('programmerhumor')
    print(subsreddits.fetch_all_subreddits())

    print("- LOGS -")
    logs = Logs()
    logs.print_all()
