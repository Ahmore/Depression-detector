from tkinter import *
from gui.charts import charts
from gui.measurement import open_measurement_screen
import sys

def open_overview_screen():
    global overview_screen
    overview_screen = Tk()
    overview_screen.title("Overview")
    overview_screen.geometry("300x250")

    Button(overview_screen, text="Add measurement", width=30, height=2, bg="white",
           command=open_measurement_screen).pack()

    Button(overview_screen, text="Charts", width=30, height=2, bg="white",
           command=charts).pack()

    Button(overview_screen, text="Exit", width=30, height=2, bg="white",
           command=exit).pack()

def exit():
    sys.exit()
