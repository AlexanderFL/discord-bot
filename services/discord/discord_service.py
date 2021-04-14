import os
import discord
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

        dir_name = os.path.join(os.curdir, "services/discord/extensions")
        nr_of_extensions = 0
        # Get all subdirectories of extensions
        subdirectories = filter(os.path.isdir, [os.path.join(dir_name,x) for x in os.listdir(dir_name)])
        for dirname in subdirectories:
            dirname_lastpart = os.path.basename(os.path.normpath(dirname))
            # Get all files inside the subdirectory
            for filename in os.listdir(dirname):
                if filename == "main.py":
                    print("Loading extension '{0}'".format(dirname_lastpart))
                    self.bot.load_extension(f'services.discord.extensions.{dirname_lastpart}.{filename[:-3]}')
                    nr_of_extensions += 1
        # Show how many extensisons were loaded
        print("Loaded {0} extensions".format(nr_of_extensions))

    def run_bot(self, token):
        """
        Gets the discord bot running
        """
        print("Starting the discord bot...")
        self.load()
        self.bot.run(token)
