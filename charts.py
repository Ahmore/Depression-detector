from tkinter import *
from tkcalendar import Calendar, DateEntry


def charts():
    global charts_screen
    charts_screen = Tk()
    charts_screen.title("CHARTS")
    charts_screen.geometry("745x370")
    Label(charts_screen, text="Date from:", height=2, font='Arial 14').grid(
        row=0, column=0)
    cal1 = Calendar(charts_screen, font="Arial 14", selectmode='day',
                    locale='en_US',
                    cursor="hand1", year=2018, month=2, day=5)
    cal1.grid(row=1, column=0)
    Label(charts_screen, text="Date to:", height=2, font='Arial 14').grid(
        row=0, column=1)
    cal2 = Calendar(charts_screen, font="Arial 14", selectmode='day',
                    locale='en_US',
                    cursor="hand1", year=2018, month=2, day=5)
    cal2.grid(row=1, column=1)
    Button(charts_screen, text="EMOTIONS PLOT",
           command=emotions_plot, height=2, font='Arial 14').grid(row=2,
                                                                  column=0)

    Button(charts_screen, text="HAPPINESS PLOT",
           command=happiness_plot, height=2, font='Arial 14').grid(row=2,
                                                                   column=1)


def emotions_plot():
    pass


def happiness_plot():
    pass

# charts()
