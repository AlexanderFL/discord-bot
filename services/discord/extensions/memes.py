import discord
from discord.ext import commands
from services.reddit.reddit_wrapper import RedditWrapper
from services.reddit.reddit_service import SubredditDoesNotSupportRandom, NoImagePosts

class Memes(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.reddit = RedditWrapper()
    
    def create_discord_msg(self, post):
        subredditname = post.subreddit.display_name
        upvotes = post.score
        title = post.title
        url = post.url
        ratio = float(post.upvote_ratio) * 100
        msg = 'From /r/{0} with {1} upvotes: {2}\n{3}% upvote ratio\n{4}'.format(subredditname, upvotes, title, ratio, url)
        return msg
    
    @commands.command()
    async def meme(self, ctx, sub_name="None", limit=-1):
        try:
            if sub_name == "None":
                post = self.reddit.get_random_post(self.reddit.get_random_subreddit())
            else:
                post = self.reddit.get_random_post(sub_name)
            await ctx.send(self.create_discord_msg(post))
        except SubredditDoesNotSupportRandom:
            await ctx.send('This subreddit does not support fetching random posts')
        except NoImagePosts:
            await ctx.send('Didn\'t find any posts that contain images')
    
def setup(client):
    client.add_cog(Memes(client))