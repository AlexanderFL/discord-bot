import os
import discord
import discord.abc as abc
from discord.ext import commands
from services.reddit.reddit_wrapper import RedditWrapper

class DiscordService(commands.Cog):
    def __init__(self):
        self.client = discord.Client()
        self.bot = commands.Bot(command_prefix='!')
        self.reddit = RedditWrapper()
    
    def load(self):
        """
        Load the extensions located in the extensions/ folder
        """
        for filename in os.listdir('./services/discord/extensions'):
            if filename.endswith('.py'):
                self.bot.load_extension(f'services.discord.extensions.{filename[:-3]}')
                print("Loaded extension: {0}".format(filename[:-3]))
        
    def run_bot(self, token):
        """
        Gets the discord bot running
        """
        print("Starting the discord bot...")
        self.load()
        self.bot.run(token)