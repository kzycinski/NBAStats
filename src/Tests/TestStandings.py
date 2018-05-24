import datetime
import unittest
from ServerConnection import ServerConnection
from NoDataFoundError import NoDataFoundError
from Standings import Standings

date = datetime.date(2017, 12, 12)
server = ServerConnection("http://data.nba.net/data/10s/prod/v1", date)


class TestStandings(unittest.TestCase):

    def test_init(self):
        self.assertIsNotNone(Standings(server))

    def test_get_standings_wrong_argument(self):
        try:
            Standings(server).get_standings(None)
        except TypeError:
            pass

    def test_get_standings_correct_argument(self):
        a = Standings(server)
        self.assertIsNotNone(a.get_standings(server.get_all_standings()))

    def test_get_all_standings(self):
        self.assertIsNotNone(Standings(server).get_all_standings())

    def test_get_western_standings(self):
        self.assertIsNotNone(Standings(server).get_western_standings())

    def test_get_eastern_standings(self):
        self.assertIsNotNone(Standings(server).get_eastern_standings())

    def test_show_wrong_arg(self):
        try:
            Standings(server).show(None)
        except TypeError:
            pass



if __name__ == '__main__':
    unittest.main()
