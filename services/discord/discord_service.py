import discord
import discord.abc as abc
from discord.ext import commands
import random
from services.reddit.reddit_wrapper import RedditWrapper
import os

class DiscordService(commands.Cog):
    def __init__(self):
        self.bot = commands.Bot(command_prefix='!')
        self.reddit = RedditWrapper()
    
    def load(self):
        """
        Load the extensions located in the extensions/ folder
        """
        for filename in os.listdir('./services/discord/extensions'):
            if filename.endswith('.py'):
                self.bot.load_extension(f'services.discord.extensions.{filename[:-3]}')

    def run_bot(self, token):
        """
        Gets the discord bot running
        """
        self.bot.run(token)

    @commands.command()
    async def ping(self, ctx):
        """
        Example on implementing commands
        """
        await ctx.send('Pong!')
