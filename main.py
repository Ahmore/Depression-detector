from tkinter import *
import requests
import os
from overview import overview

BACKEND_URL = "https://depression-detector-backend.herokuapp.com/api/"


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    main_screen.withdraw()
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
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
           command=register_user).pack()
    Button(register_screen, text="Back", width=10, height=1,
           command=call_register_main_screen).pack()


def call_register_main_screen():
    register_screen.withdraw()
    main_screen.wm_deiconify()


# Designing window for login

def login():
    global login_screen
    main_screen.withdraw()
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify,
                                 show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1,
           command=login_verify).pack()
    Button(login_screen, text="Back", width=10, height=1,
           command=call_login_main_screen).pack()


def call_login_main_screen():
    login_screen.withdraw()
    main_screen.wm_deiconify()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()
    print(username_info)
    print(password_info)
    dict = {
        "username": username_info,
        "password": password_info
    }
    err = requests.post(BACKEND_URL+'registration', json=dict)
    if err.status_code == 200:
        Label(register_screen, text="Registration Success", fg="green",
              font=("calibri", 11)).pack()
    else:
        Label(register_screen, text="Registration Failed", fg="red",
              font=("calibri", 11)).pack()



# Implementing event on login button

def login_verify():
    dict = {
        "username": username_verify.get(),
        "password": password_verify.get()
    }
    err = requests.get(BACKEND_URL + 'measurement', headers=dict)
    if err.status_code == 200:
        login_sucess()
    else:
        password_not_recognised()

# Designing popup for login success
def register_sucess():
    register_screen.withdraw()
    global register_success_screen
    register_success_screen = Toplevel(login_screen)
    register_success_screen.title("Success")
    register_success_screen.geometry("150x100")
    Label(register_success_screen, text="Register Success").pack()
    Button(register_success_screen, text="OK",
           command=call_register_overview).pack()


def login_sucess():
    login_screen.withdraw()
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",
           command=call_login_overview).pack()


def call_login_overview():
    login_success_screen.withdraw()
    overview()


def call_register_overview():
    register_success_screen.withdraw()
    overview()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()


# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
