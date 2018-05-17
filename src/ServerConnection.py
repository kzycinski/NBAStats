import datetime
import json
from pprint import pprint

import requests


class ServerConnection():
    def __init__(self, server_name, date):
        self.server_name = server_name
        self.date = date

    def get_teams(self):
        try:
            web_source = requests.get(
                self.server_name + "/{}/teams.json".format(self.date.year))
        except requests.exceptions.ConnectionError:
            print("Cannot connect to the server :(\n")
            return
        try:
            data = json.loads(web_source.content)
            return data['league']['standard']
        except json.decoder.JSONDecodeError:
            print("Given website has no data, perhaps check the date\n")
            return

    def get_daily_scores(self):
        try:
            web_source = requests.get(
                self.server_name + "/{}{:02d}{:02d}/scoreboard.json".format(self.date.year, self.date.month,
                                                                            self.date.day))
        except requests.exceptions.ConnectionError:
            print("Cannot connect to the server :(\n")
            return
        try:
            data = json.loads(web_source.content)
            return data['games']
        except json.decoder.JSONDecodeError:
            print("Given website has no data, perhaps check the date\n")
            return

    def get_all_standings(self):
        try:
            web_source = requests.get(
                self.server_name + "/{}{:02d}{:02d}/standings_all.json".format(self.date.year, self.date.month,
                                                                               self.date.day))
        except requests.exceptions.ConnectionError:
            print("Cannot connect to the server :(\n")
            return
        try:
            data = json.loads(web_source.content)
            return data['league']['standard']['teams']
        except json.decoder.JSONDecodeError:
            print("Given website has no data, perhaps check the date\n")
            return

    def get_conference_standings(self):
        try:
            web_source = requests.get(
                self.server_name + "/{}{:02d}{:02d}/standings_conference.json".format(self.date.year, self.date.month,
                                                                                      self.date.day))
        except requests.exceptions.ConnectionError:
            print("Cannot connect to the server :(\n")
            return
        try:
            data = json.loads(web_source.content)
            return data
        except json.decoder.JSONDecodeError:
            print("Given website has no data, perhaps check the date\n")
            return

    def get_western_standings(self):
        tmp = self.get_conference_standings()
        return tmp['league']['standard']['conference']['west'] if tmp else None

    def get_eastern_standings(self):
        tmp = self.get_conference_standings()
        return tmp['league']['standard']['conference']['east'] if tmp else None

    def get_players_list(self):
        try:
            web_source = requests.get(self.server_name + "/{}/players.json".format(self.date.year))
        except requests.exceptions.ConnectionError:
            print("Cannot connect to the server :(\n")
            return
        try:
            data = json.loads(web_source.content)
            return data['league']['standard']
        except json.decoder.JSONDecodeError:
            print("Given website has no data, perhaps check the date\n")
            return

    def get_player_stats(self, id):
        try:
            web_source = requests.get(self.server_name + "{}/players/{}_profile.json".format(self.date.year, id))
        except requests.exceptions.ConnectionError:
            print("Cannot connect to the server :(\n")
            return
        try:
            data = json.loads(web_source.content)
            return data['league']['standard']
        except json.decoder.JSONDecodeError:
            print("Given website has no data, perhaps check the date\n")
            return
