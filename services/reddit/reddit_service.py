import praw
from prawcore.exceptions import NotFound, Redirect, Forbidden, BadRequest, RequestException


class RedditService:
    """
    This class handles all of the requests out to reddit through praw, 
    fetching posts, and checking if they're valid for the context they're used in.

    Only the wrapper should talk to this class.
    """
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=client_secret,
                                  user_agent=user_agent)

    def fetch_random_post(self, subreddit, counter=1):
        """
        Returns a random post from the given subreddit
        """
        try:
            post = self.reddit.subreddit(subreddit).random()
            if post is None:
                raise SubredditDoesNotSupportRandom()

            if self.is_valid_image_post(post):
                return post
            else:
                # Counter gets incremented each pass, if it has reached
                # 20, raise exception to avoid infinite recursive calls
                if counter == 20:
                    raise NoImagePosts()
                return self.fetch_random_post(subreddit, counter+1)
        except RequestException:
            raise RequestException

    def _fetch_many_posts(self, subreddit, limit):
        """
        Returns a generator of posts from a given subreddit
        """
        if limit > 10:
            limit = 10
        return self.reddit.subreddit(subreddit).hot(limit=limit)

    def is_valid_image_post(self, post):
        """
        Checks if post contains 'reddit.com', if it does then it is most likely a text post
        and returns False, else True
        """
        url = post.url
        if post.author is None:
            print("Submission did not have an author")
            return False
        if "https://www.reddit.com" in url:
            return False
        else:
            return True

    def is_valid_subreddit(self, sub_name):
        """
        Returns True if subreddit is valid, False otherwise
        """
        try:
            self.reddit.subreddit(sub_name).id
        except NotFound:
            return False
        except Redirect:
            return False
        except Forbidden:
            return False
        except BadRequest:
            return False
        return True


class SubredditDoesNotSupportRandom(Exception):
    pass


class NoImagePosts(Exception):
    pass
