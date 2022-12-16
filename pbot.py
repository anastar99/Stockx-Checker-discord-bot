import discord
from scraper import Shovel
from shhhh import TOKEN, CHANNEL


client = discord.Client()


@client.event

async def on_message(message):

    pass
client.run(TOKEN)