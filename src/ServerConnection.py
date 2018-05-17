import datetime
import json
from pprint import pprint

import requests


class ServerConnection:
    def __init__(self, server_name, date):
        self.server_name = server_name
        self.date = date

    def get_teams(self):
        web_source = requests.get(
            self.server_name + "/{}/teams.json".format(self.date.year))

        try:
            data = json.loads(web_source.content)
            return data['league']['standard']
        except json.decoder.JSONDecodeError:
            return None

    def get_daily_scores(self):
        web_source = requests.get(
            self.server_name + "/{}{:02d}{:02d}/scoreboard.json".format(self.date.year, self.date.month,
                                                                        self.date.day))
        try:
            data = json.loads(web_source.content)
            return data['games']
        except json.decoder.JSONDecodeError:
            return None

    def get_all_standings(self):
        web_source = requests.get(
            self.server_name + "/{}{:02d}{:02d}/standings_all.json".format(self.date.year, self.date.month,
                                                                           self.date.day))
        try:
            data = json.loads(web_source.content)
            return data['league']['standard']['teams']
        except json.decoder.JSONDecodeError:
            return None

    def get_conference_standings(self):
        web_source = requests.get(
            self.server_name + "/{}{:02d}{:02d}/standings_conference.json".format(self.date.year, self.date.month,
                                                                                  self.date.day))
        try:
            data = json.loads(web_source.content)
            return data
        except json.decoder.JSONDecodeError:
            return None

    def get_western_standings(self):
        tmp = self.get_conference_standings()
        return tmp['league']['standard']['conference']['west'] if tmp else None

    def get_eastern_standings(self):
        tmp = self.get_conference_standings()
        return tmp['league']['standard']['conference']['east'] if tmp else None

    def get_players(self):
        web_source = requests.get(self.server_name + "/{}/players.json".format(self.date.year))

        try:
            data = json.loads(web_source.content)
            return data['league']['standard']
        except json.decoder.JSONDecodeError:
            return None
            #TODO
