import pygal
import csv
from datetime import datetime, date

dates = []
dates_major = []
cities = {}

with open('cities.csv', newline='') as source:
    reader = csv.reader(source)

    line = next(reader)
    for n in range(1, len(line)):
        cities[n] = [line[n],[]]

    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d'))
        if dates[-1].day == 1:
            dates_major.append(dates[-1])
        for n in range(1, len(row)):
            if row[n] == '':
                cities[n][1].append((dates[-1], None))
            else:
                cities[n][1].append((dates[-1], int(row[n])))

from datetime import datetime
datetimeline = pygal.DateTimeLine(
    x_label_rotation=35, truncate_label=-1,
    x_value_formatter=lambda dt: dt.strftime('%B %d %Y'),
    x_title='Date',
    y_title='Cases',
    width=1300)

for city in cities:
    datetimeline.add(cities[city][0], cities[city][1],dots_size=0.5)

datetimeline.render_to_file('timeline5.svg')
