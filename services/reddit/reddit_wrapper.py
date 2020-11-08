from services.reddit.reddit_service import RedditService
from services.files.filessystem_service import FileSystem
from prawcore.exceptions import RequestException
from models.subreddit_model import Subreddits
from random import randint

class RedditWrapper:
    def __init__(self):
        secret = FileSystem.read_json("secrets/reddit.json")
        reddit_id = secret['client_id']
        reddit_secret = secret['client_secret']
        self.reddit_service = RedditService(reddit_id, reddit_secret, "Memebot")
        self.subreddit_models = Subreddits()
    
    def _subreddit_in_list(self, sub_name):
        """
        Returns True if subreddit is in database, False otherwise
        """
        subs = self.get_subreddit_list()
        if sub_name in subs:
            return True
        else:
            return False
    
    def get_subreddit_list(self):
        """
        Returns a list of all the subreddits in the database
        """
        return self.subreddit_models.fetch_all_subreddits()
    
    def get_random_subreddit(self):
        """
        Returns a random subreddit from the database
        """
        subs = self.get_subreddit_list()
        return subs[randint(0, len(subs) - 1)]
    
    def add_subreddit(self, sub_name):
        """
        Verify that the sub does not already exist in the database and it's a valid
        subreddit, then add it to the database
        """
        if not self.reddit_service.is_valid_subreddit(sub_name):
            raise InvalidSubredditName()
        
        if self._subreddit_in_list(sub_name):
            raise SubredditAlreadyExists()

        self.subreddit_models.insert_subreddit(sub_name)

    def remove_subreddit(self, sub_name):
        """
        Verify that the sub already exists in the database, then remove it
        """
        if self._subreddit_in_list(sub_name):
            self.subreddit_models.remove_subreddit(sub_name)
        else:
            raise SubredditNotInList()
    
    def get_random_post(self, subreddit):
        """
        Return a random post from a random subreddit
        """
        try:
            if self.reddit_service.is_valid_subreddit(subreddit):
                return self.reddit_service.fetch_random_post(subreddit)
            else:
                raise InvalidSubredditName()
        except RequestException:
            # If the bot has been inactive for a long time, reddit can throw
            # an RequestException: Read timed out
            secret = FileSystem.read_json("secrets/reddit.json")
            reddit_id = secret['client_id']
            reddit_secret = secret['client_secret']
            self.reddit_service = RedditService(reddit_id, reddit_secret, "Memebot")
        finally:
            self.get_random_post(subreddit)

class InvalidSubredditName(Exception):
    pass

class SubredditNotInList(Exception):
    pass

class SubredditAlreadyExists(Exception):
    pass