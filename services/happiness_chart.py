from services.api import get_measurements
import gui.start
from services.deprcalc import depression_calculator
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


def happiness_chart(dateFrom, dateTo):
    x, y1, y2 = get_chart_data(dateFrom, dateTo)
    print(x, y1, y2)
    fig = plt.figure('HAPPINESS CHART')

    x = [datetime.strptime(d, '%Y-%m-%d').date() for d in x]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.yticks([1.0, 2.0, 3.0, 4.0],
               ['Deep depression', 'Strong depression', 'Mild depression',
                'Normal'])
    plt.plot(x, y1, 'b', label='Self-assessment')
    plt.plot(x, y2, 'r', label='Actual')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.gcf().subplots_adjust(left=0.22)
    fig.autofmt_xdate()
    plt.show()


def weighted_photos(photos):
    hidden = depression_calculator(photos['hidden_photo'])
    unhidden = depression_calculator(
        photos['unhidden_photo']) if 'unhidden_photo' in photos else 2
    return round((hidden * 3 + unhidden) / 4.0)


def get_chart_data(dateFrom, dateTo):
    raw_data = get_measurements(gui.login.token)
    data = [elem for elem in raw_data if
            elem['date'] >= dateFrom and elem['date'] <= dateTo]

    date_feeling_map = {}
    for elem in data:

        if elem['date'] in date_feeling_map:
            existing = date_feeling_map[elem['date']]['value']['hidden_photo']
            existing['sadness'] += elem['value']['hidden_photo']['sadness']
            existing['neutral'] += elem['value']['hidden_photo']['neutral']
            existing['happiness'] += elem['value']['hidden_photo']['happiness']
            existing['anger'] += elem['value']['hidden_photo']['anger']
            existing['contempt'] += elem['value']['hidden_photo']['contempt']
            existing['disgust'] += elem['value']['hidden_photo']['disgust']
            existing['surprise'] += elem['value']['hidden_photo']['surprise']
            if 'feeling' in elem['value']:
                date_feeling_map[elem['date']]['value']['feeling'] = \
                    elem['value']['feeling']
            if 'unhidden_photo' in elem['value']:
                date_feeling_map[elem['date']]['value']['unhidden_photo'] = \
                    elem['value']['unhidden_photo']
        else:
            date_feeling_map[elem['date']] = elem

    data = [elem for elem in date_feeling_map.values()]

    sorted_data = sorted(data, key=lambda item: item['date'])

    date = [elem['date'] for elem in sorted_data]
    self_assesment = [
        (elem['value']['feeling'] if ('feeling' in elem['value']) else 2) for elem
        in sorted_data]
    calculated = [weighted_photos(elem['value']) for elem
                  in sorted_data]
    return date, self_assesment, calculated
