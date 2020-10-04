from flask import Flask, render_template
from static.data import title, subtitle, description, departures, tours


app = Flask(__name__)


@app.route('/')
def re_main():
    return render_template('index.html', title=title, tours=tours, subtitle=subtitle, description=description,
                           departures=departures)


@app.route('/departures/<departure>/')
def re_departure(departure):
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
