# this program will function as a text editor where th euse can enter in text, save it , open other files etc
# author: jade higgins
# 09/02/2021

from tkinter import *
from tkinter import Tk
# adding a const var
PROGRAM_NAME = 'Jades Text Editor'

root = Tk()
# adding the menu bar
# my_menu = Menu(parent, **options)

#adding menu bar in the widget
menu_bar = Menu(root)
# adding the file label to the menu
file_menu = Menu(menu_bar, tearoff=0)
# all file menu items will be added here next
menu_bar.add_cascade(label="File", menu=file_menu)
# adding menu items
file_menu.add_command(label='New', accelerator='Ctrl + N', compound='left', underline=1)
# adding a line as a seperator between options
file_menu.add_separator()
file_menu.add_command(label='Open', accelerator='Ctrl + O', compound='left', underline=1)
file_menu.add_command(label='Save', accelerator='Ctrl + S', compound='left', underline=1)
file_menu.add_command(label='Save as', accelerator='Shift + Ctrl + S', compound='left', underline=1)
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt + F4', compound='left', underline=1)

# adding edit label to the menu bar
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
# adding menu items
edit_menu.add_command(label='Undo', accelerator='Ctrl + Z', compound='left')
edit_menu.add_separator()
edit_menu.add_command(label='Redo', accelerator='Ctrl + Y', compound='left', underline=1)
edit_menu.add_separator()


# implementing the cut function
def cut():
    content_text.event_generate("<<Cut>>")
    return "break"
# calls the function cut() using command to use this function
edit_menu.add_command(label='Cut', accelerator='Ctrl + X', compound='left', underline=1, command=cut)

edit_menu.add_command(label='Copy', accelerator='Ctrl + C', compound='left', underline=1)

edit_menu.add_command(label='Paste', accelerator='Ctrl + V', compound='left', underline=1)
edit_menu.add_separator()
edit_menu.add_command(label='Find', accelerator='Ctrl + F', compound='left', underline=1)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', accelerator='Ctrl + A', compound='left', underline=1)

# adding view label to the menu bar
view_menu = Menu(menu_bar, tearoff=0)

# show the line numbers
show_line_no = IntVar()
show_line_no.set(1)
view_menu.add_checkbutton(label='Show Line Numbers', variable=show_line_no)

# adding a themes menu
themes_menu = Menu(menu_bar, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu)

# colour scheme is defined with dictionary elements
color_schemes = {
    'Default': '#000000.#FFFFFF',
    'Greygarious': '#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue': '#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
}

# theme choice is set to a string
theme_choice = StringVar()
# sets the default colour to be black and white
theme_choice.set('Default')
# for loop to through dictionary
for k in sorted(color_schemes):
    # adding a radio button
    themes_menu.add_radiobutton(label=k, variable=theme_choice)
menu_bar.add_cascade(label='View', menu=view_menu)

# add about label to the menu bar
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label='About', compound='left', underline=1)
about_menu.add_separator()
about_menu.add_command(label='Help', compound='left', underline=1)
# configuring the menu bar
root.config(menu=menu_bar)

# adding a frame widget to hold the shortcut icons
shortcut_bar = Frame(root, height=25, background='light sea green')
shortcut_bar.pack(expand='no', fill='x')

# adding a text widget for the line number bar
line_number_bar = Text(root, width=4, padx=3, takefocus=0, border=0, background='khaki', state='disabled', wrap='none')
line_number_bar.pack(side='left', fill='y')

# adding the main text widget
content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')


# adding in the scroll bar for the content_text
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')




# all our code goes here
root.title(PROGRAM_NAME)
root.mainloop()


