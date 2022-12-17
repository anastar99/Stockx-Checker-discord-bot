import discord
from scraper import Shovel
from shhhh import TOKEN, CHANNEL


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# ?check <id>
@client.event

async def on_message(message):

    user_message = str(message.content)
    channel = client.get_channel(CHANNEL)

    if message.author == client.user:
        return

    #print(user_message[0:6], user_message[7::])
    if user_message[0:6] == '?check':

        await channel.send(embed=Shovel(user_message[7::]).gogo())
client.run(TOKEN)