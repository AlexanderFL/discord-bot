import discord
from discord.ext import commands
from services.reddit.reddit_wrapper import RedditWrapper, SubredditNotInList, SubredditAlreadyExists, InvalidSubredditName

class Subreddits(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.reddit = RedditWrapper()
    
    @commands.command()
    async def addsub(self, ctx, sub_name: str = None):
        if sub_name is None:
            await ctx.send('You need to specify a subreddit to add')
            return
        
        try:
            self.reddit.add_subreddit(sub_name)
            await ctx.send('Subreddit {0} was added'.format(sub_name))
        except SubredditAlreadyExists:
            await ctx.send('{0} is already in the list of subreddits'.format(sub_name))
        except InvalidSubredditName:
            await ctx.send('{0} does not exist on reddit.com'.format(sub_name))
    
    @commands.command()
    async def listsubs(self, ctx):
        subs = self.reddit.get_subreddit_list()
        builder = "({0}): ".format(len(subs))
        for sub in subs:
            builder += sub + ", "
        await ctx.send(builder)
    
    @commands.command()
    async def removesub(self, ctx, sub_name: str = None):
        if sub_name is None:
            await ctx.send('You need to specify a subreddit to remove')
            return
        
        try:
            self.reddit.remove_subreddit(sub_name)
            await ctx.send('{0} was removed from the list of subreddits'.format(sub_name))
        except SubredditNotInList:
            await ctx.send('"{0}" not in the list of subreddits'.format(sub_name))
        

def setup(client):
    client.add_cog(Subreddits(client))