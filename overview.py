from tkinter import *
from charts import charts

def overview():
    global overview_screen
    overview_screen = Tk()
    overview_screen.title("Overview")
    overview_screen.geometry("300x250")

    Button(overview_screen, text="Charts", width=30, height=2, bg="white",
           command=charts).pack()


def call_charts():
    charts()

# overview()