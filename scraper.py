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

    def webhook(self):
        pass


if __name__ == "__main__":
    Shovel('FZ5897')