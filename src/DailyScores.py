import datetime
import json
from pprint import pprint
import requests
import matplotlib.pyplot as plt

from src.ServerConnection import ServerConnection


class DailyScores:
    def __init__(self, server_name, date):
        self.server = ServerConnection(server_name, date)
        self.games = self.server.get_daily_scores()

    def get_scores(self):
        result = []
        for item in self.games:
            tmp = dict([('hTeamTriCode', item['hTeam']['triCode']), ('hTeamScore', item['hTeam']['score']),
                        ('vTeamTriCode', item['vTeam']['triCode']), ('vTeamScore', item['vTeam']['score'])])
            result.append(tmp)
        return result

    def show_scores(self):
        scores = self.get_scores()
        names = []
        points = []
        for item in scores:
            names.append((item['hTeamTriCode'], item['vTeamTriCode']))
            points.append((int(item['hTeamScore']), int(item['vTeamScore'])))

        plt.figure(1, figsize=(3 * len(names), len(names)))
        plt.ylabel("Score")

        for i in range(len(names)):
            subplot = 100 + len(names) * 10 + i + 1

            ymin = min(points[i]) - 10
            ymax = max(points[i]) + 10

            plt.subplot(subplot)
            plt.ylim(ymin, ymax)
            plt.yticks(points[i])
            plt.bar(names[i], points[i])

        plt.show()
