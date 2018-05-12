import datetime
import json
import requests
from pprint import pprint
import matplotlib.pyplot as plt

from src.Standings import Standings
from src.DailyScores import DailyScores

server_name = "http://data.nba.net/data/10s/prod/v1"
date = datetime.date(2017, 1, 2)
a = DailyScores(server_name, date)
b = Standings(server_name, date)
a.show(a.get_scores())
b.show(b.get_all_standings())