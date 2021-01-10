from flask import render_template
from flask import Markup
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

    text1 = Markup("Like the rest of Canada, Vancouver saw a bout of cases early in the year that receded over the summer, before rebounding to much higher proportions in the fall up to today. Vancouver and most of BC have done fairly well, maintaining sub one-hundred cases for most of the year until about October/November, where cases began to grow greatly.")
    text2 = Markup("BC provincial health officer Dr. Bonnie Henry first recommended that the BC populace wear masks on <b>June 30th, 2020</b>. This came at a time when cases had already largely decreased in Vancouver, and as such it is difficult to evaluate the effectiveness of her recommendation.")
    text3 = Markup("Conversely, masks were legislated in public indoor spaces on <b>Nov 24th, 2020</b> through a ministerial order from the BC Minister of Public Safety. This came as cases were peaking in BC, and soon afterwards a noticeable decrease in new cases can be seen, which only began to rise again over the holiday season.")

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

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Vancouver', text1=text1, text2=text2, text3=text3)

@app.route('/montreal')
def montreal():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = Markup("Montréal and Quebec was notorious in the early days of the pandemic in Canada for having the greatest number of cases in any part of Canada. However, we see the same pattern here as pretty much everywhere else, an initial decrease in cases followed by a massive rise.")
    text2 = Markup("It was recommended to wear masks in Montréal and the rest of quebec by Premier François Legault on the <b>12th of May</b>. This corresponded with a massive decrease in cases in Montréal over the coming days, nearly to the point of elimination.")
    text3 = Markup("Masks were made mandatory in the city on <b>July 31st</b>. This was in the middle of the summer lull, however came at the tails of a small resurgence in cases. As can be seen, following this date, new cases once again decreased. However, it is difficult to evaluate the significance of this decrease.")

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

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Montréal', text1=text1, text2=text2, text3=text3)

@app.route('/toronto')
def toronto():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = Markup("Toronto, the biggest and most multicultural city in Canada, is perhaps  unsurprisingly also home to the greatest number of COVID-19 cases in Canada. Like the rest of Canada, Toronto saw a large number of cases in the spring that died down over the summer. However, as summer turned to fall and then winter, the new case count per day dontinuned to rise, nearing 1400 new cases on Jan 7, 2021.")
    text2 = Markup("The City of Toronto strongly recommended its populace to wear masks on <b>May 20th</b>, coinciding with Canadian federal recommendations. In the coming days, daily case counts would decrease a great deal.")
    text3 = Markup("Slightly over a month later, on <b>Jun 30th, 2021</b>, masks were made mandatory. Cases were already falling at this point, though this mandate may have sealed the deal for COVID-19 in the following months, until the fall resurgence.")

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

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Toronto', text1=text1, text2=text2, text3=text3)

@app.route('/ottawa')
def ottawa():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = Markup("Ottawa was notable regarding the pandemic in Canada as Sophie Gregoire Trudeau, wife of the Canadian Prime Minister, came down with COVID-19 following a rtip to the UK. Like the rest of Canada, the same spring wave can be seen, dying down over the summer, before re-emerging in the fall. Interestingly, case counts decreased once again as winter approached, before skyrocketing over the holiday season.")
    text2 = Markup("Ottawa's chief medical officer of health, Dr. Vera, stressed that people should wear masks on <b>May 16, 2020</b>. However, by this time, cases were already decreasing in the city.")
    text3 = Markup("Paradoxically, cases began to climb following Ottawa's mask order on <b>August 26</b>. It is likely that other factors played parts that overwhelmed masking's ability to prevent transmimssion, and/or the sites of transmission occured where no masking took place.")

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

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Ottawa', text1=text1, text2=text2, text3=text3)

@app.route('/calgary')
def calgary():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = Markup("Calgary saw some amount of cases in the early days of the pandemic, however these also slowed to a trickle as the spring and summer months passed. In late August, the cases began to rise, spiking at around 1000 cases in november and December before once again declining.")
    text2 = Markup("Contrary to what one would imagine, the recommendation on <b>May 20</b> that Canadians wear masks by the federal chief medical officer, Dr. Theresa Tam, was not associated with any decrease in cases. Instead, if anything, an increase in cases was seen. However, in the coming months, the rate of new cases remained largely steady.")
    text3 = Markup("On <b>August 1st</b>, Calgarians had to wear masks in indoors public spaces. However, this too wasnt associated with a decrease in cases, and the following days actually saw an increase. However, the case rate would still remain relatively constant in the coming weeks, before exponentially growing over the fall.")

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

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Calgary', text1=text1, text2=text2, text3=text3)

@app.route('/edmonton')
def edmonton():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = Markup("Edmonton reflects the common pattern accross Canada, with an initial spring wave that petered out over the summer, before climbing Once again in the fall. Edmonton was initially harder hit compared to her neighbour in Calgary, but was much better off in the later fall wave.")
    text2 = Markup("Masking recommendations came with Dr. Tam's <b>May 20th</b> federal recommendation for all Canadians. However, this came after the spring wave had largely died down in Edmonton.")
    text3 = Markup("Masking legislation came into effect on <b>August 1st</b> in Edmontion. However, this was not associated with a decrease in cases. Instead, it might have stabilized cases that were rising at the time, until the later fall wave.")

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

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Edmonton', text1=text1, text2=text2, text3=text3)

@app.route('/regina')
def regina():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = Markup("Regina saw only a few cases in the spring, and practically none over the summer, however their case count rose greatly over the course of the fall. As winter began, Regina didn't see the same large numbers they saw months earlier, but it was still a far cry from the peace the saw earlier in 2020.")
    text2 = Markup("The City of Regina recommended that citizens wear masks on <b>Aug 13</b>, right as case numbers reaches the same values as in spring. Consequently, Regina saw no new cases for a month until the fall wave that effected all Canada.")
    text3 = Markup("Saskatchewan imposed mandatory masking laws on <b>November 6</b>, after cases resurged and greatly exceeded spring levels in the province. The coming weeks saw Regina's case count peak, before decreasing in the winter.")

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

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Regina', text1=text1, text2=text2, text3=text3)

@app.route('/winnipeg')
def winnipeg():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = Markup("Winnipeg saw a modest amount of cases in the spring, and more or less no clases over the course of the summer. However, the fall saw cases in Winnipeg increase far beyond their spring case load. This reflects case incidence patterns accross the rest of Canada.")
    text2 = Markup("Winnipeg introduced masking recommendations on <b>April 6th</b>, coinciding with the end of the spring wave in the city.")
    text3 = Markup("On <b>September 25th</b>, Manitoba made masking mandatory accross the province, including in Winnipeg. This came as cases rose above spring levels for the first time. However, this was not effective as in the coming months, Winnipeg's case levels would reach their peak, dwarfing the number of cases in the spring.")

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

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Winnipeg', text1=text1, text2=text2, text3=text3)

@app.route('/saskatoon')
def saskatoon():
    import pygal
    import csv
    from datetime import datetime, date
    from pygal.style import NeonStyle

    text1 = Markup("Saskatoon's case incidence pattern resembles the rest of Canada, with an initial spring wave followed by a tranquil summer, before a fall/winter period where there was a massive resurgence of cases.")
    text2 = Markup("It was recommended to wear masks in Saskatoon on <b>August 13th</b>. This came as cases began to climb once again in the city. As a result, cases returned to earlier summer levels, before the fall wave ultimately hit.")
    text3 = Markup("As the fall wave descended on Saskatoon, the province was forced to introduce masking legislation on <b>November 6th</b>. However, many new chains of transmission were already operating and the legislation did little to halt the fall wave.")

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

    return render_template('city.html', chart = chart, recchart = recchart, manchart = manchart, city='Saskatoon', text1=text1, text2=text2, text3=text3)
