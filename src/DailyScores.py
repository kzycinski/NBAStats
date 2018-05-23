import threading

import matplotlib.pyplot as plt

from IShow import IShow


class DailyScores(IShow):
    def __init__(self, server):
        self.games = server.get_daily_scores()
        self.date = server.get_date()

    def get_scores(self):
        result = []
        for item in self.games:
            tmp = dict([('hTeamTriCode', item['hTeam']['triCode']), ('hTeamScore', item['hTeam']['score']),
                        ('vTeamTriCode', item['vTeam']['triCode']), ('vTeamScore', item['vTeam']['score'])])
            result.append(tmp)
        return result

    def show(self, scores):
        names = []
        points = []
        for item in scores:
            names.append((item['hTeamTriCode'], item['vTeamTriCode']))
            points.append((int(item['hTeamScore']), int(item['vTeamScore'])))

        fig = plt.figure(1, figsize=(3 * len(names), len(names)))
        fig.suptitle('Daily scores - {}.{}.{}'.format(self.date.day, self.date.month, self.date.year),
                     fontsize=14, fontweight='bold')

        fig.text(0.5, 0.04, 'Teams', fontsize=14, ha='center', va='center')
        fig.text(0.06, 0.5, 'Points', fontsize=14, ha='center', va='center', rotation='vertical')

        for i in range(len(names)):
            ymin = min(points[i]) - 10
            ymax = max(points[i]) + 10

            subplot_a = 1 if len(names) < 10 else 2
            subplot_b = len(names) if len(names) < 10 else int(len(names) / 2)
            subplot_c = i + 1

            plt.subplot(subplot_a, subplot_b, subplot_c)

            plt.ylim(ymin, ymax)
            plt.yticks(points[i])

            plt.bar(names[i], points[i])

        plt.show()
