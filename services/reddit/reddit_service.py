import praw

class RedditService:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=client_secret,
                                  user_agent=user_agent)
    
    def get_subreddits(self):
        pass

    def get_random_subreddit(self):
        pass

    def add_subreddit(self, subreddit_name):
        pass

    def remove_subreddit(self):
        pass
    
    """
    Helper function that fetches the post requested by user
    """
    def _fetch_post(self, subreddit, limit):
        if subreddit is None:
            return reddit.subreddit(self.get_random_subreddit()).random()
        if limit == -1:
            return reddit.subreddit(subreddit).random()
        else:
            if limit > 10:
                limit = 10
            return reddit.subreddit(subreddit).hot(limit=limit)

    
    """
    Fetches the post and validates that it is a image, and that the user
    is allowed to fetch
    """
    def fetch_post(self, subreddit=None, limit=-1):
        valid_post = False
        #while not valid_post:
        #    pass

    
    """
    Checks if post contains 'reddit.com', if it does then it is most likely a text post
    and returns False, else True
    """
    def is_valid_image_post(self, post):
        if submission is None:
            print("Submission was None")
            return False
    
        url = submission.url
        if submission.author is None:
            print("Submission did not have an author")
            return False
        if "https://www.reddit.com" in url:
            return False
        else:
            return True