import datetime
import unittest
from ServerConnection import ServerConnection
from NoDataFoundError import NoDataFoundError
from PlayersManagement import PlayersManagement

date = datetime.date(2017, 12, 12)
server = ServerConnection("http://data.nba.net/data/10s/prod/v1", date)


class TestPlayersManagement(unittest.TestCase):

    def test_init(self):
        self.assertIsNotNone(PlayersManagement(server))

    def test_get_player_wrong_firstname(self):
        try:
            PlayersManagement(server).get_player("Name", "Durant", 'mode')
        except NoDataFoundError:
            pass

    def test_get_player_wrong_lastname(self):
        try:
            PlayersManagement(server).get_player("Kevin", "Name", 'mode')
        except NoDataFoundError:
            pass

    def test_get_player_wrong_mode(self):
        try:
            PlayersManagement(server).get_player("Kevin", "Durant", 'mode')
        except KeyError:
            pass

    def test_get_player_correct_data(self):
        return self.assertIsNotNone(PlayersManagement(server).get_player("Kevin", "Durant", 'latest'))

    def test_show_wrong_arg(self):
        try:
            PlayersManagement(server).show(None)
        except NoDataFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
