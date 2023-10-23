# os allows us to interact with underlying operating system
import os
# discord.py is an api wrapper for discord written in python
import discord
import discord.utils
# dotenv is responsible for keeping passwords, API keys, and senstive data safe and secure
from dotenv import load_dotenv

# loads variables from env file into actual environment
load_dotenv()
# hide discord token in env file away from users
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# create an instance of Client()
# a client represents a connection to discord and interacts w/ discord api
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# register an event
@client.event
# on_ready() is called when bot has finished login and setup
async def on_ready():
    print("{client.user} has connected to Ananya's Discord server!")

# register an event
@client.event
# on_ready() is called when new member joins server
async def on_member_join(member):
    # create a direct message to send the user
    await member.create_dm()
    # send this message to the user
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to my Discord server!"
    )

# run bot with login token
client.run(DISCORD_TOKEN)