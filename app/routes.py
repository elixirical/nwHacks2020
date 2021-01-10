from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():

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

@app.route('/vancouver')
def vancouver():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = ""
    text2 = ""
    text3 = ""

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
        show_legend=False)

    datetimeline.add(cities[2][0], cities[2][1],dots_size=0.5)

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
        show_legend=False)
    Rchart.title = 'Days from mask recommendation'
    Rchart.x_labels = map(str, range(-30, 30))
    Rchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Rchart.add(Rcities[2][0], Rcities[2][1],dots_size=0.5)

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
        show_legend=False)
    Mchart.title = 'Days from mask bylaw'
    Mchart.x_labels = map(str, range(-30, 30))
    Mchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Mchart.add(Mcities[2][0], Mcities[2][1],dots_size=0.5)

    manchart = Mchart.render_data_uri()

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Vancouver')

@app.route('/montreal')
def montreal():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = ""
    text2 = ""
    text3 = ""

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
        show_legend=False)

    datetimeline.add(cities[1][0], cities[1][1],dots_size=0.5)

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
        show_legend=False)
    Rchart.title = 'Days from mask recommendation'
    Rchart.x_labels = map(str, range(-30, 30))
    Rchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Rchart.add(Rcities[1][0], Rcities[1][1],dots_size=0.5)

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
        show_legend=False)
    Mchart.title = 'Days from mask bylaw'
    Mchart.x_labels = map(str, range(-30, 30))
    Mchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Mchart.add(Mcities[1][0], Mcities[1][1],dots_size=0.5)

    manchart = Mchart.render_data_uri()

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Montreal')

@app.route('/toronto')
def toronto():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = ""
    text2 = ""
    text3 = ""

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
        show_legend=False)

    datetimeline.add(cities[3][0], cities[3][1],dots_size=0.5)

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
        show_legend=False)
    Rchart.title = 'Days from mask recommendation'
    Rchart.x_labels = map(str, range(-30, 30))
    Rchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Rchart.add(Rcities[3][0], Rcities[3][1],dots_size=0.5)

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
        show_legend=False)
    Mchart.title = 'Days from mask bylaw'
    Mchart.x_labels = map(str, range(-30, 30))
    Mchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Mchart.add(Mcities[3][0], Mcities[3][1],dots_size=0.5)

    manchart = Mchart.render_data_uri()

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Toronto')

@app.route('/ottawa')
def ottawa():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = ""
    text2 = ""
    text3 = ""

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
        show_legend=False)

    datetimeline.add(cities[6][0], cities[6][1],dots_size=0.5)

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
        show_legend=False)
    Rchart.title = 'Days from mask recommendation'
    Rchart.x_labels = map(str, range(-30, 30))
    Rchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Rchart.add(Rcities[6][0], Rcities[6][1],dots_size=0.5)

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
        show_legend=False)
    Mchart.title = 'Days from mask bylaw'
    Mchart.x_labels = map(str, range(-30, 30))
    Mchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Mchart.add(Mcities[6][0], Mcities[6][1],dots_size=0.5)

    manchart = Mchart.render_data_uri()

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Ottawa')

@app.route('/calgary')
def calgary():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = ""
    text2 = ""
    text3 = ""

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
        show_legend=False)

    datetimeline.add(cities[8][0], cities[8][1],dots_size=0.5)

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
        show_legend=False)
    Rchart.title = 'Days from mask recommendation'
    Rchart.x_labels = map(str, range(-30, 30))
    Rchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Rchart.add(Rcities[8][0], Rcities[8][1],dots_size=0.5)

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
        show_legend=False)
    Mchart.title = 'Days from mask bylaw'
    Mchart.x_labels = map(str, range(-30, 30))
    Mchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Mchart.add(Mcities[8][0], Mcities[8][1],dots_size=0.5)

    manchart = Mchart.render_data_uri()

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Calgary')

@app.route('/edmonton')
def edmonton():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = ""
    text2 = ""
    text3 = ""

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
        show_legend=False)

    datetimeline.add(cities[9][0], cities[9][1],dots_size=0.5)

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
        show_legend=False)
    Rchart.title = 'Days from mask recommendation'
    Rchart.x_labels = map(str, range(-30, 30))
    Rchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Rchart.add(Rcities[9][0], Rcities[9][1],dots_size=0.5)

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
        show_legend=False)
    Mchart.title = 'Days from mask bylaw'
    Mchart.x_labels = map(str, range(-30, 30))
    Mchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Mchart.add(Mcities[9][0], Mcities[9][1],dots_size=0.5)

    manchart = Mchart.render_data_uri()

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Edmonton')

@app.route('/regina')
def regina():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = ""
    text2 = ""
    text3 = ""

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
        show_legend=False)

    datetimeline.add(cities[4][0], cities[4][1],dots_size=0.5)

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
        show_legend=False)
    Rchart.title = 'Days from mask recommendation'
    Rchart.x_labels = map(str, range(-30, 30))
    Rchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Rchart.add(Rcities[4][0], Rcities[4][1],dots_size=0.5)

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
        show_legend=False)
    Mchart.title = 'Days from mask bylaw'
    Mchart.x_labels = map(str, range(-30, 30))
    Mchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Mchart.add(Mcities[4][0], Mcities[4][1],dots_size=0.5)

    manchart = Mchart.render_data_uri()

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Regina')

@app.route('/winnipeg')
def winnipeg():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = ""
    text2 = ""
    text3 = ""

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
        show_legend=False)

    datetimeline.add(cities[7][0], cities[7][1],dots_size=0.5)

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
        show_legend=False)
    Rchart.title = 'Days from mask recommendation'
    Rchart.x_labels = map(str, range(-30, 30))
    Rchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Rchart.add(Rcities[7][0], Rcities[7][1],dots_size=0.5)

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
        show_legend=False)
    Mchart.title = 'Days from mask bylaw'
    Mchart.x_labels = map(str, range(-30, 30))
    Mchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Mchart.add(Mcities[7][0], Mcities[7][1],dots_size=0.5)

    manchart = Mchart.render_data_uri()

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Winnipeg')

@app.route('/saskatoon')
def saskatoon():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = ""
    text2 = ""
    text3 = ""

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
        show_legend=False)

    datetimeline.add(cities[5][0], cities[5][1],dots_size=0.5)

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
        show_legend=False)
    Rchart.title = 'Days from mask recommendation'
    Rchart.x_labels = map(str, range(-30, 30))
    Rchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Rchart.add(Rcities[5][0], Rcities[5][1],dots_size=0.5)

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
        show_legend=False)
    Mchart.title = 'Days from mask bylaw'
    Mchart.x_labels = map(str, range(-30, 30))
    Mchart.x_labels_major = ['-30','-25','-20','-15','-10','-5','0','5','10','15','20','25','30']

    Mchart.add(Mcities[5][0], Mcities[5][1],dots_size=0.5)

    manchart = Mchart.render_data_uri()

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Saskatoon')
