# https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

global catCount
catCount = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global catCount

    if message.author == client.user:
        return

    if (('cat' in message.content) or ('kitty' in message.content)) and ('tenor.com' in message.content):
        # await message.channel.send('cat')
        await message.add_reaction("😸")
        catCount += 1

    if message.content == '!count':
        response = 'I have counted '
        response += str(catCount)
        response += ' cats so far.'
        await message.channel.send(response)

client.run(os.getenv('TOKEN'))
