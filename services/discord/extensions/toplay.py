from discord.ext import commands
from models.games_model import Games
from random import randint

class WhatToPlay(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    def _fetch_all_games(self):
        games_model = Games()
        return games_model.fetch_all()
    
    def _insert_game(self, game):
        games_model = Games()
        games_model.insert_game(game)
        return True
    
    def get_random_game(self):
        all_games = self._fetch_all_games()
        rand_index = randint(-1, len(all_games)-1)
        return all_games[rand_index]
    
    def create_discord_msg(self):
        games = self._fetch_all_games()
        msg = ""
        for x in range(0, len(games)):
            if x == len(games) - 1:
                msg += games[x]
            else:
                msg += games[x] + ", "
        return msg
    
    @commands.command()
    async def showgames(self, ctx):
        await ctx.send(self.create_discord_msg())

    @commands.command()
    async def insertgame(self, ctx, message=".none"):
        if message == ".none":
            await ctx.send('Please enter a game to insert into the list of games')
        else:
            self._insert_game(message)
            await ctx.send('Added {0} to list'.format(message))
    
    @commands.command()
    async def whattoplay(self, ctx):
        await ctx.send('Maybe try {0}'.format(self.get_random_game()))

    
def setup(client):
    client.add_cog(WhatToPlay(client))