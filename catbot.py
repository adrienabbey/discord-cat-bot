# https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'cat':
        await message.channel.send('Hello!')
        print(message.content)

client.run(os.getenv('TOKEN'))
