from tkinter import *
from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta
from services.emotion_chart import emotions_chart
from services.happiness_chart import happiness_chart


def charts():
    global charts_screen
    charts_screen = Tk()
    charts_screen.title("CHARTS")
    charts_screen.geometry("745x370")
    now = datetime.now()
    two_weeks_ago = now - timedelta(days=14)
    Label(charts_screen, text="Date from:", height=2, font='Arial 14').grid(
        row=0, column=0)
    cal1 = Calendar(charts_screen, font="Arial 14", selectmode='day',
                    locale='en_US',
                    cursor="hand1", year=two_weeks_ago.year,
                    month=two_weeks_ago.month, day=two_weeks_ago.day)
    cal1.grid(row=1, column=0)
    Label(charts_screen, text="Date to:", height=2, font='Arial 14').grid(
        row=0, column=1)
    cal2 = Calendar(charts_screen, font="Arial 14", selectmode='day',
                    locale='en_US',
                    cursor="hand1", year=now.year, month=now.month,
                    day=now.day)
    cal2.grid(row=1, column=1)
    Button(charts_screen, text="EMOTIONS PLOT",
           command=lambda: emotions_plot(cal1.selection_get(),
                                         cal2.selection_get()), height=2,
           font='Arial 14').grid(row=2,
                                 column=0)

    Button(charts_screen, text="HAPPINESS PLOT",
           command=lambda: happiness_plot(cal1.selection_get(),
                                          cal2.selection_get()), height=2,
           font='Arial 14').grid(row=2,
                                 column=1)


def emotions_plot(dateFrom, dateTo):
    emotions_chart(str(dateFrom), str(dateTo))


def happiness_plot(dateFrom, dateTo):
    happiness_chart(str(dateFrom), str(dateTo))
