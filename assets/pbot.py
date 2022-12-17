import discord
from scraper import Shovel
from shhhh import TOKEN, CHANNEL


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL)
    boot_msg = discord.Embed(title='Connected', description='command:\ncheck <kw/id/sku>', color=discord.Color.green())
    boot_msg.set_footer(text='Github: anastar99')
    await channel.send(embed=boot_msg)
# ?check <id>
@client.event
async def on_message(message):
    channel = client.get_channel(CHANNEL)

    user_message = str(message.content)

    if message.author == client.user:
        return

    #print(user_message[0:6], user_message[7::])
    if user_message[0:6] == '?check':

        await channel.send(embed=Shovel(user_message[7::]).gogo())
client.run(TOKEN)