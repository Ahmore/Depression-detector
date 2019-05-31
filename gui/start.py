from tkinter import *
from gui.login import open_login_screen
from gui.register import open_register_screen

def open_start_screen():
    global start_screen
    start_screen = Tk()
    start_screen.geometry("300x250")
    start_screen.title("Account Login")
    
    Label(text="Select Your Choice", bg="blue", width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=open_login_screen).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=open_register_screen).pack()

    start_screen.mainloop()