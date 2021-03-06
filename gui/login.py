from tkinter import *
from gui.overview import open_overview_screen
from services.api import login
from services.interval_job import start_interval_job
import gui.start

def open_login_screen():
    global login_screen
    login_screen = Toplevel(gui.start.start_screen)
    login_screen.title("Login")
    login_screen.geometry("200x250")
    Label(login_screen, text="").pack()
    gui.start.start_screen.withdraw()

    username = StringVar()
    password = StringVar()

    Label(login_screen, text="Username*").pack()
    username_login_entry = Entry(login_screen, textvariable=username)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password*").pack()
    password_login_entry = Entry(login_screen, textvariable=password,
                                 show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1,
           command=lambda: try_login(username.get(), password.get())).pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Back", width=10, height=1,
           command=go_to_start_screen).pack()


def go_to_start_screen():
    login_screen.withdraw()
    gui.start.start_screen.wm_deiconify()

def try_login(username, password):
    global token
    token = login(username, password)

    if token is not None:
        go_to_overview_screen()
        start_interval_job()
    else:
        open_login_result_screen()

def open_login_result_screen():
    global login_result_screen
    login_result_screen = Toplevel(login_screen)
    login_result_screen.title("Error")
    Label(login_result_screen, text="Login failed").pack()
    Button(login_result_screen, text="OK", width=10, height=1,
       command=close_login_result_screen).pack()

def close_login_result_screen():
    login_result_screen.withdraw()

def go_to_overview_screen():
    login_screen.withdraw()
    open_overview_screen()
