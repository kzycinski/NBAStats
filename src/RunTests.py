import unittest
from Tests import *

tests = [TestDailyScores,
         TestNBATeams,
         TestPlayersManagement,
         TestServerConnection,
         TestStandings,
         TestPlayer]


def create_suite():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for test in tests:
        test_suite.addTest(loader.loadTestsFromModule(test))

    return test_suite


if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)
