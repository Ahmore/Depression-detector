from tkinter import *
from gui.charts import charts

def open_overview_screen():
    global overview_screen
    overview_screen = Tk()
    overview_screen.title("Overview")
    overview_screen.geometry("300x250")

    Button(overview_screen, text="Charts", width=30, height=2, bg="white",
           command=charts).pack()


def call_charts():
    charts()

# overview()