import sqlite3
from models.logs_model import Logs

class Games:
    def __init__(self, filename="storage/games.db"):
        self.filename = filename
        self._create_default_table()
        self.logs = Logs()
    
    def _connect(self):
        """
        Returns the connection and cursor to the database file
        """
        conn = sqlite3.connect(self.filename)
        curs = conn.cursor()
        return conn, curs

    def _create_default_table(self):
        """
        Creates the table if it does not exists within the database file,
        also inserts the first log if the table was just created
        """
        conn, c = self._connect()

        create_log_table = ''' CREATE TABLE IF NOT EXISTS games
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                game TEXT NOT NULL)'''
        c.execute(create_log_table)
        conn.commit()
        conn.close()
    
    def insert_game(self, game: str):
        """
        Insert a game into the table from the given string parameter
        """
        conn, c = self._connect()

        args = (game,)

        create_game = '''INSERT INTO games(game)
                      VALUES(?)'''
        c.execute(create_game, args)
        conn.commit()
        conn.close()
    
    def contains_records(self):
        """
        Returns True or False if the table contains any entries
        False if entries dont exist, True otherwise
        """
        conn, c = self._connect()
        c.execute('''SELECT COUNT(*) FROM games''')
        result = c.fetchall()
        if result[0][0] == 0:
            return False
        else:
            return True
    
    def fetch_all(self):
        """
        Fetch all games from the database
        Returns a list of strings
        """
        conn, c = self._connect()

        query = '''SELECT * FROM games'''
        c.execute(query)
        result = c.fetchall()

        return_list = []
        for r in result:
            return_list.append(r[1])
        return return_list
