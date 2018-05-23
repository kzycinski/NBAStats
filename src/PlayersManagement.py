import matplotlib.pyplot as plt
from NBATeams import NBATeams
from IShow import IShow
from Player import Player
from NoDataFoundError import NoDataFoundError


class PlayersManagement(IShow):
    def __init__(self, server):
        self.server = server
        self.players_list = server.get_players_list()

    def get_player(self, name, surname, mode):
        player_id = None
        for player in self.players_list:
            if player['firstName'] == name and player['lastName'] == surname:
                player_id = player['personId']
        if not player_id:
            raise NoDataFoundError
        player_info = self.server.get_player_stats(player_id)
        pi = player_info['stats'][mode]
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

        fig = plt.figure(4)
        fig.suptitle('Points per game', fontsize=14, fontweight='bold')
        y_min = 0
        y_max = max(ppg) + 10

        plt.ylim(y_min, y_max)
        plt.ylabel("PPG", fontsize=14,  ha='center')
        plt.xlabel("PLAYERS", fontsize=14,ha='center')
        for a, b in zip(names, ppg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, ppg)

        fig = plt.figure(5)
        fig.suptitle('Assists per game', fontsize=14, fontweight='bold')

        y_min = 0
        y_max = max(apg) + 5

        plt.ylim(y_min, y_max)
        plt.ylabel("APG", fontsize=14, ha='center')
        plt.xlabel("PLAYERS", fontsize=14,  ha='center')
        for a, b in zip(names, apg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, apg)

        fig = plt.figure(6)
        fig.suptitle('Rebounds per game', fontsize=14, fontweight='bold')

        y_min = 0
        y_max = max(rpg) + 5

        plt.ylim(y_min, y_max)
        plt.ylabel("RPG", fontsize=14, ha='center')
        plt.xlabel("PLAYERS", fontsize=14,  ha='center')
        for a, b in zip(names, rpg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, rpg)

        fig = plt.figure(7)
        fig.suptitle('Minutes per game', fontsize=14, fontweight='bold')

        y_min = 0
        y_max = max(mpg) + 10

        plt.ylim(y_min, y_max)
        plt.ylabel("MPG", fontsize=14,  ha='center')
        plt.xlabel("PLAYERS", fontsize=14,  ha='center')
        for a, b in zip(names, mpg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, mpg)

        fig = plt.figure(8)
        fig.suptitle('Steals per game', fontsize=14, fontweight='bold')

        y_min = 0
        y_max = max(spg) + 2

        plt.ylim(y_min, y_max)
        plt.ylabel("SPG", fontsize=14, ha='center')
        plt.xlabel("PLAYERS", fontsize=14,  ha='center')
        for a, b in zip(names, spg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, spg)

        fig = plt.figure(9)
        fig.suptitle('Blocks per game', fontsize=14, fontweight='bold')

        y_min = 0
        y_max = max(bpg) + 2

        plt.ylim(y_min, y_max)
        plt.ylabel("BPG", fontsize=14,  ha='center')
        plt.xlabel("PLAYERS", fontsize=14,  ha='center')
        for a, b in zip(names, bpg):
            plt.text(a, b, str(b), color='blue', fontweight='bold', ha='center')
        plt.bar(names, bpg)

        plt.show()
