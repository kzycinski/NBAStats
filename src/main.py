"""import requests
from bs4 import BeautifulSoup

websource = requests.get("http://data.nba.net/data/10s/prod/v1/20180509/scoreboard.json")
soup = BeautifulSoup(websource.content, "html.parser")
print(soup.prettify())
"""
import json
import requests
from pprint import pprint

websource = requests.get("http://data.nba.net/data/10s/prod/v1/20180509/scoreboard.json")
data = json.loads(websource.content)

#Data is array that holds dictionaries

a = data["games"]
pprint(a[0])



