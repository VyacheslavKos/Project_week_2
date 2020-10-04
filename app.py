from flask import Flask
from flask import render_template
from static.data import title
from static.data import subtitle
from static.data import description
from static.data import departures
from static.data import tours
from random import randint


app = Flask(__name__)


@app.route('/')
def re_main():
    # Выбираем произвольные 6 отелей
    tours_random = {}
    while len(tours_random) < 6:
        random_tour = randint(1, len(tours))
        if random_tour not in tours_random.keys():
            tours_random[random_tour] = tours[random_tour]
    return render_template('index.html', title=title, tours_random=tours_random, subtitle=subtitle,
                           description=description, departures=departures)


@app.route('/departures/<departure>/')
def re_departure(departure):
    # Фильтруем отели по привязке к месту вылета
    tours_dep = {}
    tours_dep_str = []
    for key, value in tours.items():
        for value1 in value.values():
            if value1 == departure:
                tours_dep[key] = value
                tours_dep_str.append(value)
    return render_template('departure.html', title=title, departure=departure, departures=departures,
                           tours_dep=tours_dep, tours_dep_str=tours_dep_str)


@app.route('/tours/<int:id>/')
def render_tours(id):
    return render_template('tour.html', title=title, tour=tours[id], departures=departures)


def base():
    return render_template('base.html', title=title, departures=departures)


if __name__ == '__main__':
    app.run()
