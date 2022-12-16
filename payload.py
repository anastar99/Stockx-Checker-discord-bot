from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, Popularity

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
    proxyList = []

    # get random proxy from list 
    return # return that random proxy
if __name__ == "__main__":
    pass