import unittest
import os
from models.logs_model import Logs

class TestLogsModel(unittest.TestCase):
    """
    Test the Log class
    """

    def setUp(self):
        self.filename = 'test.db'
        self.log = Logs(filename=self.filename)
    
    def doCleanups(self):
        os.remove(self.filename)
    
    def test_full(self):
        # Check if test.db was created
        assert os.path.exists(self.filename)

        # Check if table logs was created
        # Check if the first log was inserted
        assert self.log.contains_records()

        try:
            self.log.insert_log('Test message')
            assert True
        except:
            assert False

        assert self.log.contains_records()
