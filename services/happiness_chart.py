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


def get_chart_data(dateFrom, dateTo):
    raw_data = get_measurements(gui.login.token)
    data = [elem for elem in raw_data if
            elem['date'] >= dateFrom and elem['date'] <= dateTo]
    sorted_data = sorted(data, key=lambda item: item['date'])

    date = [elem['date'] for elem in sorted_data]
    self_assesment = [elem['value']['feeling'] for elem in sorted_data]
    calculated = [depression_calculator(elem['value']['hidden_photo']) for elem
                  in sorted_data]
    return date, self_assesment, calculated
