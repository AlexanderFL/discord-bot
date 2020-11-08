from services.discord.discord_service import DiscordService
from services.files.filessystem_service import FileSystem

class Bot:
    def __init__(self):
        self.d = DiscordService()
        self.token = FileSystem.read_json('secrets/discord.json')['token']
    
    def run(self):
        self.d.run_bot(self.token)
    

if __name__ == "__main__":
    b = Bot()
    b.run()