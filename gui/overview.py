from tkinter import *
from gui.charts import charts
from gui.measurement import open_measurement_screen
import sys

def open_overview_screen():
    global overview_screen
    overview_screen = Tk()
    overview_screen.title("Menu")
    overview_screen.geometry("300x220")

    Label(overview_screen, text="").pack()
    Button(overview_screen, text="Add measurement", width=30, height=2, bg="white",
           command=open_measurement_screen).pack()

    Label(overview_screen, text="").pack()
    Button(overview_screen, text="Statistics", width=30, height=2, bg="white",
           command=charts).pack()

    Label(overview_screen, text="").pack()
    Button(overview_screen, text="Exit", width=30, height=2, bg="white",
           command=exit).pack()

    Label(overview_screen, text="").pack()

def exit():
    sys.exit()
