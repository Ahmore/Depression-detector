from services.api import get_measurements
import gui.start
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


def emotions_chart(dateFrom, dateTo):
    x, y1, y2, y3 = get_chart_data(dateFrom, dateTo)
    print(x, y1, y2, y3)
    fig = plt.figure('EMOTIONS CHART')

    x = [datetime.strptime(d, '%Y-%m-%d').date() for d in x]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())

    plt.stackplot(x, y3, y2, y1, labels=['Sadness', 'Neutral', 'Happiness'])
    plt.legend(loc='upper left')

    fig.autofmt_xdate()
    plt.show()


def calc(emotion, elem):
    emotions = elem['value']['hidden_photo']

    neutral = emotions['neutral'] / 10
    happiness = emotions['happiness']
    sadness = emotions['sadness']
    total = neutral + happiness + sadness

    emotion_map = {'neutral': neutral, 'happiness': happiness,
                   'sadness': sadness}
    return emotion_map[emotion] / total


def get_chart_data(dateFrom, dateTo):
    raw_data = get_measurements(gui.login.token)
    data = [elem for elem in raw_data if
            elem['date'] >= dateFrom and elem['date'] <= dateTo]
    sorted_data = sorted(data, key=lambda item: item['date'])

    date = [elem['date'] for elem in sorted_data]
    happiness = [calc('happiness', elem) for elem in sorted_data]
    neutral = [calc('neutral', elem) for elem in sorted_data]
    sadness = [calc('sadness', elem) for elem in sorted_data]
    return date, happiness, neutral, sadness
