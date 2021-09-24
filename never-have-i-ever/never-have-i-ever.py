# this is my version of the " Never Have I Ever " Drinking game.
# Date:  24/09/2021 - Sweden
# Author: Jade Higgins

from tkinter import Tk, PhotoImage, Menu, Frame, Text, Scrollbar, Checkbutton, Button, END, Toplevel, Label, Entry, IntVar, INSERT,  BooleanVar,\
    StringVar, Canvas
# from tkinter import *
from tkinter import Tk
# working with files
import tkinter.filedialog
import os# for  handling file operations
import tkinter.messagebox

# symbollic name
PROGRAM_NAME = 'Never Have I Ever..'


root = Tk()
# establishing the size of the window
root.geometry('500x500')
root.title(PROGRAM_NAME)

# Adding the menu part to the widget
menu_bar = Menu(root)
# adding the about menu widget
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)
about_menu.add_separator()

# creating a canvas to hold the textboxes and buttons etc.
canvas1 = Canvas(root, width=400, height=400)
canvas1.pack()



# creating text box one
textbox1 = Entry(root)
canvas1.create_window(200, 140, window=textbox1)


#display the  menu bar
root.config(menu=menu_bar)
root.mainloop()