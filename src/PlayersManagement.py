import matplotlib.pyplot as plt
from NBATeams import NBATeams
from IShow import IShow
from Player import Player
from ServerConnection import ServerConnection


class PlayersManagement(IShow):
    def __init__(self, server):
        self.server = server
        self.players_list = server.get_players_list()

    def get_player(self, name, surname):
        player_id = None
        for player in self.players_list:
            if player['firstName'] == name and player['lastName'] == surname:
                player_id = player['personId']
        if not player_id:
            return None
            # todo
        player_info = self.server.get_player_stats(player_id)
        pi = player_info['stats']['latest']
        teams = NBATeams(self.server)
        return Player(name, surname, teams.get_team_tricode_from_id(int(player_info['teamId'])), pi['ppg'], pi['rpg'],
                      pi['apg'], pi['mpg'], pi['spg'], pi['bpg'])

    def show(self, players):
        names = []
        ppg = []
        apg = []
        rpg = []
        mpg = []
        spg = []
        bpg = []
        for item in players:
            tmp = '{}\n{}'.format(item['Name'], item['Team'])
            names.append(tmp)
            ppg.append(float(item['PPG']))
            rpg.append(float(item['RPG']))
            apg.append(float(item['APG']))
            mpg.append(float(item['MPG']))
            spg.append(float(item['SPG']))
            bpg.append(float(item['BPG']))

        plt.figure(1)

        y_min = 0
        y_max = max(ppg) + 10

        plt.ylim(y_min, y_max)
        for a, b in zip(names, ppg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, ppg)

        plt.figure(2)

        y_min = 0
        y_max = max(apg) + 5

        plt.ylim(y_min, y_max)
        for a, b in zip(names, apg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, apg)

        plt.figure(3)

        y_min = 0
        y_max = max(rpg) + 5

        plt.ylim(y_min, y_max)
        for a, b in zip(names, rpg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, rpg)

        plt.figure(4)

        y_min = 0
        y_max = max(mpg) + 10

        plt.ylim(y_min, y_max)
        for a, b in zip(names, mpg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, mpg)

        plt.figure(5)

        y_min = 0
        y_max = max(spg) + 2

        plt.ylim(y_min, y_max)
        for a, b in zip(names, spg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, spg)

        plt.figure(6)

        y_min = 0
        y_max = max(bpg) + 2

        plt.ylim(y_min, y_max)
        for a, b in zip(names, ppg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, bpg)

        plt.show()
