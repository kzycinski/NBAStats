import unittest
from ServerConnection import ServerConnection
import datetime
from NoDataFoundError import NoDataFoundError

date = datetime.date(2017, 12, 12)
server = ServerConnection("http://data.nba.net/data/10s/prod/v1", date)


class TestServerConnection(unittest.TestCase):

    def test_empty_server_get_data(self):
        try:
            ServerConnection.get_data("http://data.nba.net/data/10s/prod/v")
        except NoDataFoundError:
            pass

    def test_wrong_server_get_data(self):
        try:
            ServerConnection.get_data("http://2017/teams.json")
        except ConnectionError:
            pass

    def test_get_teams(self):
        return self.assertIsNotNone(server.get_teams())

    def test_get_daily_scores(self):
        return self.assertIsNotNone(server.get_daily_scores())

    def test_get_all_standings(self):
        return self.assertIsNotNone(server.get_all_standings())

    def test_get_western_standings(self):
        return self.assertIsNotNone(server.get_western_standings())

    def test_get_eastern_standings(self):
        return self.assertIsNotNone(server.get_eastern_standings())

    def test_get_players_list(self):
        return self.assertIsNotNone(server.get_players_list())

    def test_get_player_stats(self):
        return self.assertIsNotNone(server.get_player_stats(201566))

    def test_get_player_stats_wrong_id(self):
        try:
            return self.assertIsNotNone(server.get_player_stats(000000))
        except NoDataFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
