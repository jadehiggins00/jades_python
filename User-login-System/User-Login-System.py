# this is my version of a user login system where the user can
# register for an account then login
# Date:  25/09/2021 - Sweden
# Author: Jade Higgins

from tkinter import Tk, PhotoImage, Menu, Frame, Text, Scrollbar, Checkbutton, Button, END, Toplevel, Label, Entry, \
    IntVar, INSERT, BooleanVar, \
    StringVar, Canvas
# from tkinter import *
from tkinter import Tk
# working with files
import tkinter.filedialog
import os  # for  handling file operations
import tkinter.messagebox

# symbollic name
PROGRAM_NAME = 'Jades User Login'


def main_account_screen():

    # global var
    global main_screen

    # creating the gui window
    main_screen = Tk()
    # setting the configuration of the gui window
    main_screen.geometry("300x250")
    # setting the title of the gui window
    main_screen.title(PROGRAM_NAME)



    # Creating the form label
    Label(text="Choose Login or Register", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    # creating the Login Button
    Button(text='Login', bg='yellow', height='2', width='30', command=login).pack()
    # this is used to leave a space inbetween the buttons
    Label(text='').pack()

    # creating the register button
    Button(text='Register', bg='yellow', height='2', width='30', command=register).pack()


    # this starts the gui
    main_screen.mainloop()

# creating a login window using a top level widget
def login():

    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry('300x250')

    # label at the top of the window
    Label(login_screen, text='Please Enter your Details Below to Login').pack()
    Label(login_screen,text='').pack()

    global username_verify
    global password_verify

    # setting these vars to text vars
    username_verify = StringVar()
    password_verify = StringVar()

    # label for username
    Label(login_screen, text='Username * ').pack()
    # creating username entry widget
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text='').pack()

    # label and entry for password
    Label(login_screen, text='Password * ').pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text='').pack()

    # login button
    Button(login_screen, text='Login', width=10, height=1, command=login_verification).pack()

# login verification
def login_verification():
    print('working..')


def register():
    # here we are creating a toplevel widget
    # when register is clicked, a top-level window is displayed
    # in the arguement we have to pass the global screen variable

    # setting global variables
    # this allows the variables to be accessible
    global username
    global password
    global username_entry
    global password_entry
    global register_screen

    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry('300x250')

    # setting the text variables
    username = StringVar()
    password = StringVar()

    # set label for users instruction
    Label(register_screen, text='Please enter details below', bg='blue').pack()
    # creating space between the labels
    Label(register_screen, text='').pack()

    # setting the label for the username label
    username_label = Label(register_screen, text='Username * ')
    username_label.pack()

    # setting the username entry
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    # creating the password label
    password_label = Label(register_screen, text='Password * ')
    password_label.pack()

    # creating the password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    # creating space between the entry box and button
    Label(register_screen, text='').pack()

    # creating the register button
    Button(register_screen, text='Register', width=10, height=1, bg='yellow', command=register_user).pack()


# Implementing an event on the register button.
# Essentially, after filling in the entries and the register button is pressed
# The entries are saved in file.
def register_user():

    # getting the username and password
    username_info = username.get()
    password_info = password.get()

    # opening the file in write mode
    file = open(username_info, 'w')

    # writing the username and password information into the file
    file.write(username_info + '\n')
    file.write(password_info)
    file.close()

    # this clears the entry widget
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    # creating a label to inform the user of success
    Label(register_screen,text='Registeration Success', fg='green', font=('Calibri',11)).pack()

# calling the main_account_screen function
main_account_screen()