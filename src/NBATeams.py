import json
import requests
from pprint import pprint

from src.ServerConnection import ServerConnection


class NBATeams:
    def __init__(self, server):
        self.teams = server.get_teams()


    def get_team(self, name):
        if type(name) is int:
            for item in self.teams:
                if item['teamId'] == name:
                    return item
            else:
                raise NameError("Wrong team ID\n")
        if len(name) == 3:
            for item in self.teams:
                if item['tricode'] == name:
                    return item
            else:
                raise NameError("Wrong team Tricode\n")
        else:
            for item in self.teams:
                if item['fullName'] == name:
                    return item
            else:
                raise NameError("Wrong team FullName\n")

    def get_team_tricode_from_id(self, id):
        if type(id) is int:
            for item in self.teams:
                if int(item['teamId']) == id:
                    return item['tricode']
            else:
                raise NameError("Wrong team ID\n")
        else:
            raise AttributeError("ID has to be int\n")
