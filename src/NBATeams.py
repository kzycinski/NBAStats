import json
import requests
from pprint import pprint


class NBATeams:
    def __init__(self, year):
        web_source = requests.get("http://data.nba.net/data/10s/prod/v1/{}/teams.json".format(year))
        data = json.loads(web_source.content)
        self.teams = data['league']['standard']

    def get_team(self, name):
        if len(name) == 3:
            for item in self.teams:
                if item['tricode'] == name:
                    return item
            else:
                raise NameError("Wrong team Tricode")
        else:
            for item in self.teams:
                if item['fullName'] == name:
                    return item
            else:
                raise NameError("Wrong team FullName")



