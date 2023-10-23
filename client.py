# os allows us to interact with underlying operating system
import os
# discord.py is an api wrapper for discord written in python
import discord
import discord.utils
# dotenv is responsible for keeping passwords, API keys, and senstive data safe and secure
from dotenv import load_dotenv

from discord.ext import commands
from discord import File

from PIL import Image, ImageDraw, ImageFont
import io

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

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)


@bot.command(name='canvas')
async def canvas(ctx, text=None):

    width = 500
    height = 200

    # create empty image 600x300 
    image = Image.new('RGB', (width, height))

    # create object for drawing
    draw = ImageDraw.Draw(image)

    # draw red rectangle with green outline from point 
    draw.rectangle([50, 50, width-50, height-50], fill=(255,0,0), outline=(0,255,0))

    # draw text in center
    text = f'Hello {ctx.author.name}'

    text_width, text_height = draw.textsize(text)
    x = (width - text_width)//2
    y = (height - text_height)//2

    draw.text( (x, y), text, fill=(0,0,255))

    # create buffer
    buffer = io.BytesIO()

    # save PNG in buffer
    image.save(buffer, format='PNG')    

    # move to beginning of buffer so `send()` it will read from beginning
    buffer.seek(0) 

    # send image
    await ctx.send(file=File(buffer, 'myimage.png'))

# run bot with login token
client.run(DISCORD_TOKEN)