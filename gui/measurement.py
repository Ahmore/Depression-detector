from tkinter import *
import gui.start
from services.api import get_azure_data
from services.api import get_azure_token
from services.api import send_measurement
from services.camera import make_photo
import datetime

def open_measurement_screen():
    global measurement_screen
    measurement_screen = Toplevel(gui.start.start_screen)
    measurement_screen.title("Add measurement")
    measurement_screen.geometry("300x250")

    Label(measurement_screen, text="Please enter your feeling [1-4]").pack()

    # gui.start.start_screen.withdraw()
    gui.overview.overview_screen.withdraw()

    feeling = StringVar()

    Label(measurement_screen, text="Feeling * ").pack()
    feelings_entry = Entry(measurement_screen, textvariable=feeling)
    feelings_entry.pack()

    Label(measurement_screen, text="").pack()
    Button(measurement_screen, text="Add", width=10, height=1,
           command=lambda: try_add_measurement(feeling.get())).pack()
    Button(measurement_screen, text="Back", width=10, height=1,
           command=go_to_overview_screen).pack()

def try_add_measurement(feelings):
    as_int = int(feelings)

    if as_int >= 1 and as_int <= 4:
        open_photo_screen(as_int)

def open_photo_screen(feeling):
    measurement_screen.withdraw()

    token = get_azure_token(gui.login.token)
    initial_photo = make_photo()
    initial_photo_data = get_azure_data(token,  initial_photo)

    global photo_screen
    photo_screen = Toplevel(gui.start.start_screen)
    photo_screen.title("Photo")
    photo_screen.geometry("300x250")

    Label(photo_screen, text="Make photo").pack()
    Button(photo_screen, text="Make", width=10, height=1,
           command=lambda: try_make_photo(feeling, initial_photo_data)).pack()
    Button(photo_screen, text="Back", width=10, height=1,
           command=go_to_overview_screen2).pack()

def try_make_photo(feeling, initial_photo_data):
    photo_screen.withdraw()

    token = get_azure_token(gui.login.token)
    second_photo = make_photo()
    second_photo_data = get_azure_data(token,  second_photo)

    now = str(datetime.datetime.now())
    data = {
        'hidden_photo': initial_photo_data,
        'unhidden_photo': initial_photo_data,
        'feeling': feeling 
    }

    open_measurement_result_screen(send_measurement(gui.login.token, now, data))

def go_to_overview_screen():
    measurement_screen.withdraw()
    gui.overview.overview_screen.wm_deiconify()

def go_to_overview_screen2():
    photo_screen.withdraw()
    gui.overview.overview_screen.wm_deiconify()

def go_to_overview_screen3():
    measurement_result_screen.withdraw()
    gui.overview.overview_screen.wm_deiconify()

def open_measurement_result_screen(is_success):
    global measurement_result_screen
    measurement_result_screen = Toplevel(gui.start.start_screen)
    measurement_result_screen.title("Success" if is_success is True else "Fail")
    measurement_result_screen.geometry("150x100")
    Label(measurement_result_screen, text="Measurement success" if is_success is True else "Measurement fail").pack()

    Button(measurement_result_screen, text="OK",
           command=go_to_overview_screen3).pack()
