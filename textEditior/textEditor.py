# this program will function as a text editor where th euse can enter in text, save it , open other files etc
# author: jade higgins
# 09/02/2021

from tkinter import Tk, PhotoImage, Menu, Frame, Text, Scrollbar, Checkbutton, Button, END ,Toplevel, Label, Entry, IntVar, \
    StringVar
# from tkinter import *
from tkinter import Tk

# adding a const var
PROGRAM_NAME = 'Jades Text Editor'

root = Tk()
# establishing the size of the window
root.geometry('500x500')
root.title(PROGRAM_NAME)


# implementing the cut function
def cut():
    content_text.event_generate("<<Cut>>")
    return "break"

# implementing the copy function
def copy():
    content_text.event_generate("<<Copy>>")
    return "break"

#implementing the paste function
def paste():
    content_text.event_generate("<<Paste>>")
    return "break"

# implementing the Undo function
def undo():
    content_text.event_generate("<<Undo>>")
    return "break"

# implementing the redo function
# the event var prevents TKinter from pasting info when using ctrl+y and instead redos the action
def redo(event=None):
    content_text.event_generate("<<Redo>>")
    return 'break'

# implementing the select all feature
def select_all(event=None):
    # sel is used for selecting text. 1.0 and end means select beginning until the end
    content_text.tag_add('sel', 1.0, 'end');
    return "break"

#implementing the find all function
def find_all(event=None):
    # creating a new top level window to search for words
    search_toplevel = Toplevel(root)
    # giving the window a title
    search_toplevel.title('Find Text')
    # setting the window as a transient window so it can lie on top of the parent window
    search_toplevel.transient(root)
    # adding a label for the window
    Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
    # adding an entry field
    search_entry_widget = Entry(search_toplevel, width=25)
    # positioning the entry field
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    # focus_set is used to set focus on a widget
    search_entry_widget.focus_set()
    # this var is used to track what the user enters
    ignore_case_value = IntVar()
    # adding a check button for ignore case feature
    Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(row=1,column=1, sticky='e', padx=2,pady=2)
    # adding a button for find all - lambda can take a number of arguments ( like a small function
    # calls search_output
    Button(search_toplevel, text='Find All', underline=0,
           command=lambda: search_output(search_entry_widget.get(), ignore_case_value.get(),
                                          content_text, search_toplevel, search_entry_widget)
           ).grid(row=0,column=2, sticky='e' + 'w', padx=2, pady=2)
    # adding the function close_search_window which takes care of removing the match tag that
    # was added during the search. used to override the close button
    def close_search_window():
        # removing the match tag
        content_text.tag_remove('match', '1.0', END)
        # destroying the toplevel window
        search_toplevel.destroy()

    # used to close the window and calling the function close_search_window()
    search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
    return "break"

# defining the search function which performs the search
# and adds the match tag to the matching text
def search_output(needle, if_ignore_case, content_text, search_toplevel, search_box):
    # removes previous search related match tags, if there are any
    content_text.tag_remove('match', '1.0', END)
    # intialising this to be 0
    matches_found = 0
    if needle:
        # storing the first position of the first match in this var
        start_pos = '1.0'
        # we can search through the entire document using a while True loop
        # the loop keeps track of matches using the count var
        while True:
            # uses a search function and calculates the position of the last character in the matched word
            # and stores it in the end_pos var
            start_pos = content_text.search(needle, start_pos, nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            # for every match found it adds the match tag to the text ranging from
            # the first position to the last position
            content_text.tag_add('match', start_pos, end_pos)
            # after every match we set the value to the start pos to be the end pos
            matches_found += 1
            start_pos = end_pos
        # tag match configured to have a red font and yellow background
        content_text.tag_config('match', foreground='red', background='yellow')

    # updating the title of the find window to show the number of matches
    # sets focus on search box element
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))

# adding the menu bar
# my_menu = Menu(parent, **options)
#adding menu bar in the widget
menu_bar = Menu(root)
# adding the file label to the menu
file_menu = Menu(menu_bar, tearoff=0)
# all file menu items will be added here next
menu_bar.add_cascade(label="File", menu=file_menu)
# adding menu items
file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', underline=1)
# adding a line as a seperator between options
file_menu.add_separator()
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', underline=1)
file_menu.add_command(label='Save', accelerator='Ctrl+S', compound='left', underline=1)
file_menu.add_command(label='Save as', accelerator='Shift + Ctrl+S', compound='left', underline=1)
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt+F4', compound='left', underline=1)

# adding edit label to the menu bar
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
# adding menu items
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', compound='left', command=undo)
edit_menu.add_separator()
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', underline=1, command=redo)
edit_menu.add_separator()

# calls the function cut() using command to use this function
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', underline=1, command=cut)

# calls the function copy() using the command to use this function
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', underline=1, command=copy)

# calls the function paste() using the command to use this function
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', underline=1, command=paste)

edit_menu.add_separator()
# adding a callback to the find_text function
edit_menu.add_command(label='Find', accelerator='Ctrl+F', compound='left', underline=1, command=find_all)
edit_menu.add_separator()
# adding a callback to the select function
edit_menu.add_command(label='Select All', accelerator='Ctrl+A', compound='left', underline=1, command=select_all)

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
content_text = Text(root, wrap='word', undo=1)
content_text.pack(expand='yes', fill='both')


# adding in the scroll bar for the content_text
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

# handling redo quirk
content_text.bind('<Control-y>', redo) # handling lowercase
content_text.bind('Control-Y', redo) # handling Uppercase

# binding the function to the ctrl-a quirk for select all
content_text.bind('<Control-a>', select_all) # handling lowercase
content_text.bind('<Control-A>', select_all)

# binding the function to the ctrl-f quirk for find all function
content_text.bind('<Control-f>', find_all) # handling lowercase
content_text.bind('<Control-F>', find_all) # handling uppercase


# all our code goes here

root.mainloop()


