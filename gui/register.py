from tkinter import *
from gui.login import open_login_screen
from services.api import register
import gui.start

def open_register_screen():
    global register_screen

    register_screen = Toplevel(gui.start.start_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    gui.start.start_screen.withdraw()

    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue",
           command=lambda: try_register(username.get(), password.get())).pack()
    Button(register_screen, text="Back", width=10, height=1,
           command=go_to_start_screen).pack()

def try_register(username, password):
    open_register_result_screen(register(username, password))

def go_to_start_screen():
    register_screen.withdraw()
    gui.start.start_screen.wm_deiconify()

def open_register_result_screen(is_success):
    global register_result_screen
    register_result_screen = Toplevel(register_screen)
    register_result_screen.title("Success" if is_success is True else "Fail")
    register_result_screen.geometry("150x100")
    Label(register_result_screen, text="Register success" if is_success is True else "Register fail").pack()

    if is_success is True:
        register_screen.withdraw()

        Button(register_result_screen, text="OK",
               command=go_to_login_screen).pack()
    else:
        Button(register_result_screen, text="OK",
               command=close_register_result_screen).pack()

def close_register_result_screen():
    register_result_screen.withdraw()

def go_to_login_screen():
    register_result_screen.withdraw()
    open_login_screen()