import unittest
import os
from models.subreddit_model import Subreddits

class TestLogsModel(unittest.TestCase):
    """
    Test the Subreddit class
    """

    def setUp(self):
        self.filename = 'test_subreddits.db'
        self.subreddits = Subreddits(filename=self.filename)
    
    def doCleanups(self):
        os.remove(self.filename)
    
    def test_full(self):
        # Check if test_subreddits.db was created
        assert os.path.exists(self.filename)

        # Insert into the database
        try:
            self.subreddits.insert_subreddit('Test message')
            assert True
        except:
            assert False

        # Fetch the list and make sure it has one item
        try:
            sub_list = self.subreddits.fetch_all_subreddits()
            assert len(sub_list) == 1
        except:
            assert False

        # Remove from the database
        try:
            self.subreddits.remove_subreddit('Test message')
            assert True
        except:
            assert False
        
        # Fetch the list again and make sure it is empty
        try:
            sub_list = self.subreddits.fetch_all_subreddits()
            assert len(sub_list) == 0
        except:
            assert False