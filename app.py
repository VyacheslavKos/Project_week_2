import random

from flask import Flask
from flask import render_template

from data.data import *


app = Flask(__name__)


@app.route('/')
def main():
    # Выбираем произвольные 6 отелей
    id_tours = []
    tours_random = {}
    for tour_id in tours:
        id_tours.append(tour_id)
    random.shuffle(id_tours)
    for i in range(6):
        tours_random[id_tours[i]] = tours[id_tours[i]]
    return render_template('index.html', title=title, tours_random=tours_random, subtitle=subtitle,
                           description=description, departures=departures)


@app.route('/departures/<departure>/')
def re_departures(departure):
    # Фильтруем отели по привязке к месту вылета
    tours_dep = {}
    for key, value in tours.items():
        if departure == value['departure']:
            tours_dep[key] = value
    return render_template('departure.html', title=title, departure=departure, departures=departures,
                           tours_dep=tours_dep)


@app.route('/tours/<int:ide>/')
def re_tours(ide):
    return render_template('tour.html', title=title, tour=tours[ide], departures=departures)


if __name__ == '__main__':
    app.run()
