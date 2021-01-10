from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def hello():

    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

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
        width=1300,
        style=NeonStyle,
        legend_at_bottom=True, legend_at_bottom_columns=9)

    for city in cities:
        datetimeline.add(cities[city][0], cities[city][1],dots_size=0.5)

    chart = datetimeline.render_data_uri()

    Rcities = {}
    with open('masks-recommended-zeroed.csv', newline='') as source:
        reader = csv.reader(source)
        line = next(reader)
        for n in range(1, len(line)):
            Rcities[n] = [line[n],[]]
        for row in reader:
            for n in range(1, len(row)):
                if row[n] == '':
                    Rcities[n][1].append(None)
                else:
                    Rcities[n][1].append(int(row[n]))
    Rchart = pygal.Line(
        truncate_label=-1,
        x_title='Date pre/post mask recommendation',
        y_title='Cases',
        width=600,
        style=NeonStyle,
        show_minor_x_labels=False,
        legend_at_bottom=True, legend_at_bottom_columns=3)
    Rchart.title = 'Days from mask recommendation'
    Rchart.x_labels = map(str, range(-30, 30))
    Rchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']
    for city in Rcities:
        Rchart.add(Rcities[city][0], Rcities[city][1],dots_size=0.5)

    recchart = Rchart.render_data_uri()

    Mcities = {}
    with open('masks-mandatory-zeroed.csv', newline='') as source:
        reader = csv.reader(source)
        line = next(reader)
        for n in range(1, len(line)):
            Mcities[n] = [line[n],[]]
        for row in reader:
            for n in range(1, len(row)):
                if row[n] == '':
                    Mcities[n][1].append(None)
                else:
                    Mcities[n][1].append(int(row[n]))
    Mchart = pygal.Line(
        truncate_label=-1,
        x_title='Date pre/post mask bylaw',
        y_title='Cases',
        width=600,
        style=NeonStyle,
        show_minor_x_labels=False,
        legend_at_bottom=True, legend_at_bottom_columns=3)
    Mchart.title = 'Days from mask bylaw'
    Mchart.x_labels = map(str, range(-30, 30))
    Mchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']
    for city in Mcities:
        Mchart.add(Mcities[city][0], Mcities[city][1],dots_size=0.5)

    manchart = Mchart.render_data_uri()

    return render_template('index.html', chart = chart, recchart = recchart, manchart = manchart)

@app.route('/edmonton')
def edmonton():
    return render_template('city.html', city='Edmonton')
