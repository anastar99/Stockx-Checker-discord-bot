import requests
import payload
import json
import discord

class Shovel:

    def __init__(self, id):
        self.id = id

    def findItemData(self):

        url = f'https://stockx.com/api/browse?_search={self.id}'

        data = requests.get(url, headers=payload.generate_payload(), proxies={'http': payload.getProxy()}) # if you dont have proxies just remove ",proxies={'http': payload.getProxy()}"
        
        parsed_data = json.loads(data.text)
        #print(parsed_data)

        formatted = {}
        formatted['shoe'] = parsed_data['Products'][0]['shoe']
        formatted['full_name'] = parsed_data['Products'][0]['title']
        formatted['picture'] = parsed_data['Products'][0]['media']['thumbUrl']
        formatted['link_key'] = parsed_data['Products'][0]['urlKey']
        formatted['last_sale'] = parsed_data['Products'][0]['market']['lastSale']
        formatted['last_size'] = parsed_data['Products'][0]['market']['lastSaleSize']
        formatted['retail'] = parsed_data['Products'][0]['traits'][2]['value'] if parsed_data['Products'][0]['traits'][2]['value'] != False else 'N/A'
        formatted['low_bid'] = parsed_data['Products'][0]['market']['lowestAsk']
        formatted['low_bid_size'] = parsed_data['Products'][0]['market']['lowestAskSize']
        formatted['high_bid'] = parsed_data['Products'][0]['market']['highestBid']
        formatted['high_bid_size'] = parsed_data['Products'][0]['market']['highestBidSize']
        formatted['sale_num'] = parsed_data['Products'][0]['market']['deadstockSold']
        formatted['avg'] = parsed_data['Products'][0]['market']['averageDeadstockPrice']
        return formatted

    def shoeLink(self, key):
        url = f'https://stockx.com/{key}'

        return url

    def styleMessage(self, data):

        embed = discord.Embed(title=data['full_name'], description=f"Retail: ${data['retail']} ", color=discord.Color.blurple(), url=self.shoeLink(data['link_key']))
        embed.set_thumbnail(url=f"{data['picture']}")
        embed.add_field(name='Lowest Ask', value=f"${data['low_bid']}")
        embed.add_field(name='Highest Ask', value=f"${data['high_bid']}", inline=True)
        embed.add_field(name='Last Sale', value=f"{data['last_size']}: ${data['last_sale']}", inline=True)
        embed.add_field(name='Total # Of Sales', value=data['sale_num'], inline=True)
        embed.add_field(name='Avg Sale Price', value=f"${data['avg']}", inline=True)
        embed.set_footer(text='Github: anastar99')

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