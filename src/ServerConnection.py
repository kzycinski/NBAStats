import datetime
import json
import requests


class ServerConnection:
    def __init__(self, server_name, date):
        self.server_name = server_name
        self.date = date

    def get_daily_scores(self):
        web_source = requests.get(
            self.server_name + "/{}{:02d}{:02d}/scoreboard.json".format(self.date.year, self.date.month,
                                                                        self.date.day))
        try:
            data = json.loads(web_source.content)
            return data['games']
        except json.decoder.JSONDecodeError:
            return None
