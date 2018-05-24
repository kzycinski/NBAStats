import datetime
import unittest
from ServerConnection import *
from NoDataFoundError import *
from DailyScores import *

date = datetime.date(2017, 12, 12)
server = ServerConnection("http://data.nba.net/data/10s/prod/v1", date)


class TestDailyScores(unittest.TestCase):

    def test_init_correct(self):
        self.assertIsNotNone(DailyScores(" ", " "))

    def test_get_scores_correct(self):
        self.assertIsNotNone(DailyScores(server.get_daily_scores(), server.get_date()).get_scores())

    def test_get_scores_wrong_scores(self):
        try:
            DailyScores(" ", server.get_date()).get_scores()
        except TypeError:
            pass

    def test_show_wrong_date(self):
        try:
            a = DailyScores(server.get_daily_scores(), 21)
            a.show(a.get_scores())
        except AttributeError:
            pass

    def test_show_wrong_scores(self):
        try:
            a = DailyScores(" ", date)
            a.show(a.get_scores())
        except TypeError:
            pass


if __name__ == '__main__':
    unittest.main()
