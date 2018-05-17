class Players:
    def __init__(self, server):
        self.players = server.get_players()

    def get_player(self, name, surname):
        for player in self.players:
            if self.players['firstName'] == name and self.players['lastName'] == surname:
                return player
        return None

