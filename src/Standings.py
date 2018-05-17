import datetime
from pprint import pprint

from src.IShow import IShow
from src.NBATeams import NBATeams
from src.ServerConnection import ServerConnection
import matplotlib.pyplot as plt


class Standings(IShow):
    def __init__(self, server):
        self.server = server


    def get_standings(self, standings):
        result = []
        teams = NBATeams(self.server)
        for item in standings:
            tmp = dict([('win', item['win']), ('tricode', teams.get_team_tricode_from_id(int(item['teamId']))),
                        ('loss', item['loss'])])
            result.append(tmp)
        return result

    def get_all_standings(self):
        return self.get_standings(self.server.get_all_standings())

    def get_eastern_standings(self):
        return self.get_standings(self.server.get_eastern_standings())

    def get_western_standings(self):
        return self.get_standings(self.server.get_western_standings())

    def show(self, standings):
        names = []
        wins = []
        loses = []
        pprint(standings)
        for item in standings:
            tmp = '{}\n{}-{}'.format(item['tricode'], item['win'], item['loss'])
            names.append(tmp)
            wins.append(int(item['win']))
            loses.append(int(item['loss']))

        plt.figure(1)

        y_min = 0
        y_max = 82

        plt.ylim(y_min, y_max)
        for a, b in zip(names, wins):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha = 'center')
        plt.bar(names, wins)

        plt.figure(2)

        plt.ylim(y_min, y_max)
        for a, b in zip(names, loses):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha = 'center')
        plt.bar(names, loses)

        plt.show()
