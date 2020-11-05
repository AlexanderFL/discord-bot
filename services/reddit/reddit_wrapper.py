from services.reddit.reddit_service import RedditService
from services.files.filessystem_service import FileSystem
from models.subreddit_model import Subreddits
from random import randint

class RedditWrapper:
    def __init__(self):
        secret = FileSystem.read_json("secrets/reddit.json")
        reddit_id = secret['client_id']
        reddit_secret = secret['client_secret']
        self.reddit_service = RedditService(reddit_id, reddit_secret, "Memebot")
        self.subreddit_models = Subreddits()
    
    def get_subreddit_list(self):
        return self.subreddit_models.fetch_all_subreddits()
    
    def get_random_subreddit(self):
        subs = self.get_subreddit_list()
        return subs[randint(0, len(subs) - 1)]
    
    # TODO: Implement
    def add_subreddit(self, sub_name):
        pass

    # TODO: Implement
    def remove_subreddit(self, sub_name):
        pass