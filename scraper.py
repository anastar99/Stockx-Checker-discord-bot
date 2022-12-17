import requests
import payload
import json
import discord

class Shovel:

    def __init__(self, id):
        self.id = id

    def findItemData(self):

        url = f'https://stockx.com/api/browse?_search={self.id}'

        data = requests.get(url, headers=payload.generate_payload())
        
        parsed_data = json.loads(data.text)
        print(parsed_data)

        formatted = {}
        formatted['shoe'] = parsed_data['Products'][0]['shoe']
        formatted['full_name'] = parsed_data['Products'][0]['shortDescription']
        formatted['picture'] = parsed_data['Products'][0]['media']['thumbUrl']
        formatted['link_key'] = parsed_data['Products'][0]['urlKey']
        # lowest, highest asks
        # lowest, highest, latest sale and size
        return formatted

    def shoeLink(self, key):
        url = f'https://stockx.com/{key}'

        return url

    def graph(self):
        pass

    def styleMessage(self, data):

        embed = discord.Embed(title=data['full_name'], description='retail price', color=discord.Color.blurple(), url=self.shoeLink(data['link_key']))
        embed.set_thumbnail(url=f"{data['picture']}")
        embed.add_field(name='Lowest Ask', value='lowest value')
        embed.add_field(name='Highest Ask', value='highest value', inline=True)
        embed.add_field(name='Last Sale', value='Size: price', inline=False)
        embed.set_footer(text='anastar99')

        return embed

    def error(self):

        embed = discord.Embed(title=f'Could Not Find {self.id}', description='Please Try Again...\n\nIf it does exist message pistachio', color=discord.Color.red())
        return embed
    def gogo(self):

        try:

            d = self.findItemData()
            return self.styleMessage(d)
        except IndexError:
            return self.error()

if __name__ == "__main__":
    Shovel('FZ5897').gogo()