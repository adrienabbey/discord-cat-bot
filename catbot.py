# https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

catCount = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'cat' in message.content:
        # await message.channel.send('cat')
        await message.add_reaction("😸")
        catCount += 1

    if 'Count cats' in message.content:
        await message.channel.send('I have counted ' + catCount + ' cats so far.')

client.run(os.getenv('TOKEN'))
