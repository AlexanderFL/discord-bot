from services.discord.discord_service import DiscordService
from services.files.filessystem_service import FileSystem

if __name__ == "__main__":
    d = DiscordService()
    d.load()
    token = FileSystem.read_json('secrets/discord.json')['token']
    d.run_bot(token)