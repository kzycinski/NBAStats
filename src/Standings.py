from IShow import IShow
from NBATeams import NBATeams
import matplotlib.pyplot as plt


class Standings(IShow):
    def __init__(self, server):
        self.server = server
        self.date = server.get_date()

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
        for item in standings:
            tmp = '{}\n{}-{}'.format(item['tricode'], item['win'], item['loss'])
            names.append(tmp)
            wins.append(int(item['win']))
            loses.append(int(item['loss']))

        fig = plt.figure(2)

        y_min = 0
        y_max = 82
        fig.suptitle('Wins - {}.{}.{}'.format(self.date.day, self.date.month, self.date.year),
                     fontsize=14, fontweight='bold')
        plt.ylim(y_min, y_max)
        plt.ylabel("WINS", fontsize=14, ha='center')
        plt.xlabel("TEAMS", fontsize=14, ha='center')
        for a, b in zip(names, wins):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, wins)

        fig = plt.figure(3)
        fig.suptitle('Loses - {}.{}.{}'.format(self.date.day, self.date.month, self.date.year),
                     fontsize=14, fontweight='bold')
        plt.ylim(y_min, y_max)
        plt.ylabel("LOSES", fontsize=14, ha='center')
        plt.xlabel("TEAMS", fontsize=14, ha='center')
        for a, b in zip(names, loses):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, loses)

        plt.show()
