import datetime
import json
from pprint import pprint
import requests


class DailyScores:
    def __init__(self, date):
        web_source = requests.get(
            "http://data.nba.com/data/10s/prod/v1/{}{:02d}{:02d}/scoreboard.json".format(date.year, date.month,
                                                                                         date.day))
        data = json.loads(web_source.content)
        self.games = data['games']

    def get_scores(self):
        result = []
        for item in self.games:
            tmp = dict([('hTeamTriCode', item['hTeam']['triCode']), ('hTeamScore', item['hTeam']['score']),
                        ('vTeamTriCode', item['vTeam']['triCode']), ('vTeamScore', item['vTeam']['score'])])
            result.append(tmp)
        return result


date = datetime.date(2018, 1, 1)
a = DailyScores(date).get_scores()
pprint(a)
