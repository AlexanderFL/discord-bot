import unittest
from services.reddit.reddit_service import (RedditService, SubredditDoesNotSupportRandom,
                                            NoImagePosts)
from services.files.filessystem_service import FileSystem
from unittest.mock import Mock


# TODO: Create a service stub that would fake a connection to reddit.com
class TestRedditService(unittest.TestCase):
    def setUp(self):
        info = FileSystem.read_json('secrets/reddit.json')
        self.reddit = RedditService(info['client_id'], info['client_secret'], 'Memebot v0.1.2 by u/thealexknows')

    def test_fetch_valid_post(self):
        post = self.reddit.fetch_random_post('pics')
        self.assertIsInstance(post.url, str)

    def test_fetch_invalid_post_no_random(self):
        with self.assertRaises(SubredditDoesNotSupportRandom):
            self.reddit.fetch_random_post('wallpapers')
    
    def test_fetch_invalid_post_no_pics(self):
        # This test takes some time to execute
        with self.assertRaises(NoImagePosts):
            self.reddit.fetch_random_post('nosleep')
    
    def test_is_invalid_subreddit(self):
        self.assertFalse(self.reddit.is_valid_subreddit('1'))
    
    def test_is_valid_subreddit(self):
        self.assertTrue(self.reddit.is_valid_subreddit('pics'))
    
    def test_is_valid_image_post_valid(self):
        setup_obj = Post()
        self.assertTrue(self.reddit.is_valid_image_post(setup_obj))