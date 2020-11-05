
from services.reddit.reddit_service import RedditService
from services.files.filessystem_service import FileSystem

class RedditWrapper:
    def __init__(self):
        secret = FileSystem.read_json("secrets/reddit.json")
        reddit_id = secret['client_id']
        reddit_secret = secret['client_secret']
        self.reddit_service = RedditService(reddit_id, reddit_secret, "Memebot")
    
    # TODO: Implement the database
    def get_subreddit_list(self):
        pass
    
    # TODO: Implement get_subreddit_list()
    def get_random_subreddit(self):
        pass
    
    # TODO: Implement
    def add_subreddit(self, sub_name):
        pass

    # TODO: Implement
    def remove_subreddit(self, sub_name):
        pass