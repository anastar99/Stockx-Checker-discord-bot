from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, Popularity
import random

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value]
popular = [Popularity.COMMON.value, Popularity.POPULAR.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, popularity=popular, limit=100)


def get_agent():

    return user_agent_rotator.get_random_user_agent()


def generate_payload():

    agent = get_agent()

    headers = {
        'accept': 'application/json',
        'app-platform': 'Iron',
        'referer': 'https://stockx.com/en-gb',
        'user-agent': agent,
        'x-requested-with': 'XMLHttpRequest'

    }

    return headers

def getProxy():
    proxyList = ["188.132.222.2:8080", "190.158.69.120:8080",
            "152.204.128.46:33047","118.27.113.167:8080",
            "8.210.83.33:80","43.227.129.65:83",
            "1.162.35.88:80","5.187.2.186:8089",
            "139.99.237.62:80","181.78.67.109:999"]

    get_random = random.randint(0, len(proxyList) - 1)
    return proxyList[get_random]
if __name__ == "__main__":
    pass