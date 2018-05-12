import datetime
import json
import requests
from pprint import pprint
import matplotlib.pyplot as plt

from src.DailyScores import DailyScores

date = datetime.date(2018, 1, 2)
a = DailyScores(date).get_scores()
pprint(a)
names = []
scores = []
for item in a:
    names.append((item['hTeamTriCode'], item['vTeamTriCode']))
    scores.append((int(item['hTeamScore']), int(item['vTeamScore'])))

plt.figure(1, figsize=(3 * len(names), len(names)))
plt.ylabel("Score")

for i in range(len(names)):
    xd = 100 + len(names)*10 + i + 1
    print(xd)
    ymin = min(scores[i])-10
    ymax = max(scores[i])+10

    print(ymin,ymax)

    plt.subplot(100 + len(names)*10 + i + 1)
    plt.ylim(ymin, ymax)
    plt.yticks(scores[i])
    plt.bar(names[i], scores[i])


plt.show()


