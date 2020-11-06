# discord-bot
A discord bot that can fetch random image posts from specified subreddits.

## How to setup
1. Create a folder at the root of this project, called 'secrets' and open it
2. Create a file 'reddit.json' and follow this format with your own client id and client secret
```
{
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
}
```
3. Create a file 'discord.json' and follow the same procedure
```
{
    "token": "YOUR_TOKEN"
}
```
4. It's recommended you create a virtual environment with python before running, but if you want you can skip this step
    1. [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
5. In the root folder of this project, run `python -m pip install -r requirements.txt`
6. Run main.py and you're all setup

## How to use
Before subreddits can be suggested to the bot, you need to get it up and running. Follow the setup guide for that explaination. Commands that can be used in discord are:

**!addsub < subreddit name >**\
Adds a subreddit to the database of subreddits

**!removesub < subreddit name >**\
Removes a subreddit from the database

**!listsubs**\
Lists all of the subreddits in the database

**!meme < *subreddit name* >**\
Fetches an image post from the database of subreddits, parameter is optional but if it is specified then a random image post is fetched specifically from that subreddit
