import datetime
import unittest
from ServerConnection import ServerConnection
from NoDataFoundError import NoDataFoundError
from NBATeams import NBATeams

date = datetime.date(2017, 12, 12)
server = ServerConnection("http://data.nba.net/data/10s/prod/v1", date)

class TestNBATeams(unittest.TestCase):

    def test_init_correct_server(self):
        self.assertIsNotNone(NBATeams(server))

    def test_get_team_wrong_name(self):
        try:
            NBATeams(server).get_team("Team")
        except NameError:
            pass

    def test_get_team_wrong_id(self):
        try:
            NBATeams(server).get_team(1)
        except NameError:
            pass

    def test_get_team_wrong_tricode(self):
        try:
            NBATeams(server).get_team("ABC")
        except NameError:
            pass

    def test_get_team_tricode_from_id_wrong_id(self):
        try:
            NBATeams(server).get_team_tricode_from_id(1)
        except NameError:
            pass

    def test_get_team_tricode_from_id_wrong_id_type(self):
        try:
            NBATeams(server).get_team_tricode_from_id("Type")
        except AttributeError:
            pass

    def test_get_team_corect_name(self):
        self.assertIsNotNone(NBATeams(server).get_team("Chicago Bulls"))

    def test_get_team_correct_id(self):
        self.assertIsNotNone(NBATeams(server).get_team(1610612760))

    def test_get_team_correct_tricode(self):
        self.assertIsNotNone(NBATeams(server).get_team("OKC"))

    def test_get_team_tricode_from_id_correct_id(self):
        if NBATeams(server).get_team_tricode_from_id(1610612760) == 'OKC':
            pass


if __name__ == '__main__':
        unittest.main()
