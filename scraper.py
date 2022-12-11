import requests

s = requests.Session()

create = s.post("https://www.goat.com/")


header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

products = requests.get("https://www.goat.com/search?query=HQ6448", headers=header)

print(products.headers)