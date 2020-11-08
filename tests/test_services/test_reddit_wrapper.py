import unittest
from services.reddit.reddit_wrapper import (RedditWrapper, InvalidSubredditName)

class TestRedditWrapper(unittest.TestCase):
    def setUp(self):
        self.redditWrapper = RedditWrapper()
    
    def test_get_random_post_invalid(self):
        with self.assertRaises(InvalidSubredditName):
            self.redditWrapper.get_random_post("1")
    