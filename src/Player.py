class Player:
    def __init__(self, fname, lname, team, ppg, rpg, apg, mpg, spg, bpg):
        self.first_name = fname
        self.last_name = lname
        self.team = team
        self.ppg = ppg
        self.rpg = rpg
        self.apg = apg
        self.mpg = mpg
        self.spg = spg
        self.bpg = bpg

    def get_stats(self):
        return [dict([('Name', self.first_name + " " + self.last_name), ('Team', self.team), ('PPG', self.ppg),
                      ('RPG', self.rpg),
                      ('APG', self.apg), ('MPG', self.mpg), ('SPG', self.spg),
                      ('BPG', self.bpg)])]

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_team(self):
        return self.team
