import datetime
import unittest
from Player import Player

date = datetime.date(2017, 12, 12)


class TestPlayer(unittest.TestCase):

    def test_init(self):
        Player("", "", "", "", "", "", "", "", "")

    def test_get_stats_wrong(self):
        a = Player("", "", "", "", "", "", "", "", "")
        a.get_stats()

    def test_get_name_none(self):
        a = Player(None, None, "", "", "", "", "", "", "")
        try:
            a.get_name()
        except TypeError:
            pass

    def test_get_team_none(self):
        a = Player(None, None, None, "", "", "", "", "", "")
        self.assertIsNone(a.get_team())

    def test_get_team_correct(self):
        a = Player(None, None, "OKC", "", "", "", "", "", "")
        if a.get_team() == "OKC":
            pass

    def test_get_name_correct(self):
        a = Player("ABC", "CDE", "", "", "", "", "", "", "")
        if a.get_name() == "ABC CDE":
            pass


if __name__ == '__main__':
    unittest.main()
