# this program will function as a text editor where th euse can enter in text, save it , open other files etc
# author: jade higgins
# 09/02/2021

from tkinter import Tk, PhotoImage, Menu, Frame, Text, Scrollbar, Checkbutton, Button, END, Toplevel, Label, Entry, IntVar,BooleanVar,\
    StringVar
# from tkinter import *
from tkinter import Tk
# working with files
import tkinter.filedialog
import os# for  handling file operations
import tkinter.messagebox
# adding a const var
PROGRAM_NAME = 'Jades Text Editor'

# adding a global var to keep track of the filename of the opened file
# it is a global var because we want other methods to be able to access it
file_name = None

root = Tk()
# establishing the size of the window
root.geometry('500x500')
root.title(PROGRAM_NAME)

# this is called if the user unchecks highlight button
def undo_highlight(event=None):
    # removes the active_line tag from the entire text area
    content_text.tag_remove('active_line', 1.0, 'end')

# this called if the user presses the button to and it is checked
# after 100 milliseconds it calls the toggle_highlight function to check if it still should be highlighted
def highlight_line(interval=100):
    content_text.tag_remove('active_line', 1.0, 'end')
    content_text.tag_add('active_line', 'insert linestart', 'insert lineend+1c')
    content_text.after(interval, toggle_highlight)


# everytime the user checks highlight current line, this function is called
# this function checks whether the menu item is checked. if it is checked, it invokes
# the highlight_line function, otherwise if it unchecked it calls the undo_highlight
def toggle_highlight(event=None):
    if to_highlight_line.get():
        highlight_line()
    else:
        undo_highlight()



# adding message boxes for about function
def display_about_messagebox(event=None):
    tkinter.messagebox.showinfo("About", "{} {}".format(PROGRAM_NAME, "\nThis was programmed by \n Jade Higgins"))

# adding message box for the help function
def display_help_messagebox(event=None):
    tkinter.messagebox.showinfo("Help", "Help Book: what do you need help with??", icon='question')

# adding a message box for exiting the editor
def exit_editor(event=None):
    # prompts user an Ok-cancel dialog to confirm the quit action
    if tkinter.messagebox.askokcancel("Quit", "You Really Want to Quit?"):
        root.destroy()

# implementing the cut function
def cut():
    content_text.event_generate("<<Cut>>")
    # calling this function
    on_content_changed()
    return "break"

# implementing the copy function
def copy():
    content_text.event_generate("<<Copy>>")
    return "break"

#implementing the paste function
def paste():
    content_text.event_generate("<<Paste>>")
    # calling this function
    on_content_changed()
    return "break"

# implementing the Undo function
def undo():
    content_text.event_generate("<<Undo>>")
    # calling this function
    on_content_changed()
    return "break"

# implementing the redo function
# the event var prevents TKinter from pasting info when using ctrl+y and instead redos the action
def redo(event=None):
    content_text.event_generate("<<Redo>>")
    # calling this function
    on_content_changed()
    return 'break'

# implementing the select all feature
def select_all(event=None):
    # sel is used for selecting text. 1.0 and end means select beginning until the end
    content_text.tag_add('sel', 1.0, 'end')
    return "break"

#implementing the find all function
def find_text(event=None):
    # creating a new top level window to search for words
    search_toplevel = Toplevel(root)
    # giving the window a title
    search_toplevel.title('Find Text')
    # setting the window as a transient window so it can lie on top of the parent window
    search_toplevel.transient(root)
    # adding a label for the window
    Label(search_toplevel, text="Find Text:").grid(row=0, column=0, sticky='e')
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
    Button(search_toplevel, text='Find Text', underline=0,
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

# this returns the opened file object
# file_object = tkinter.filedialog.askopenfile(mode='r')

# implementing the open file function
def open_file(event=None):
    # we use askopenfilename to fetch the file name of the opened file.
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension='.txt',
        filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if input_file_name:
        global file_name
        file_name = input_file_name
        # here we isolate the os module and add it as the title of the root window
        # changes the name of the top bar to be the file name
        root.title('{} - {}'.format(os.path.basename(file_name),  PROGRAM_NAME))
        # we open the given file in read mode and insert its content into the content widget
        with open(file_name) as _file:
            # we use the context manager ( the with command) which takes care of closing
            # the file properly for us, even in the case of an exception
            content_text.insert(1.0, _file.read())
    # calling this function
    on_content_changed()

# implementing the save function
# this function checks whether a file is open
def save(event=None):
    global file_name
    # if the file is not open, it passes the work to the save_as function
    if not file_name:
        save_as()
    # if a file is open it will overwrite the the contents of a file with the current contents of the text area
    else:
        write_to_file(file_name)
    return 'break'

# implementing the save_as() function
def save_as(event=None):
    # this function uses a dialog by using asksaveasfilename and tires to get the filename
    # provided by the user for the given filename
    input_file_name = tkinter.filedialog.asksaveasfile(defaultextension='.txt',
            filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if input_file_name:
        global file_name
        file_name = input_file_name
        # opens new file in write mode and writes the contents of the new text under this new filename
        write_to_file(file_name)
        # after writing, it closes the current file object and changes the title of the window
        # to reflect the file name
        root.title('{} - {}'.format(os.path.basename(file_name),PROGRAM_NAME))
    return 'break'

# implementing the write_to_file
# this actually writes to the file
def write_to_file(file_name):
    # try get the contents of the text area and write the new content and save the file
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass

# implementing the new_file function
def new_file(event=None):
    # changing the title of the root window to untitled
    root.title('Untitled')
    global file_name
    # sets the value of the global var to be none
    file_name = None
    # delete all the content in the text area and creates a fresh document
    content_text.delete(1.0, END)
    # calling this function
    on_content_changed()

# function to check whether lines have been added or removed from the text area
# and accordingly update line numbers
def on_content_changed(event=None):
    # calling the function
    update_line_numbers()

# implementing the function update_line_numbers
def update_line_numbers(event=None):
    # updates the text widget that displays the line using the string
    # output from the previous function
    line_numbers = get_line_numbers()
    # string added to the left label by using config
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')

# implementing get_line_numbers which returns a string containing all the numbers
# until the last row, separated by line breaks
def get_line_numbers():
    output = ''
    # previously we set show_line_no to be 1
    # if show_line_no is set to 1 then we calculate the last line
    if show_line_no.get():
        # here we create a text string consisting of numbers from 1 to the number
        # of the last line
        row, col = content_text.index("end").split('.')
        # each number is seperated by a line break
        for i in range(1, int(row)):
            output += str(i)+ '\n'
    # if show_line_number is unchecked in the menu, the varibale text remains blank
    # thereby displaying no numbers
    return output



# images from icons folder for shortcut bar
new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')
find_icon = PhotoImage(file='icons/find_text.gif')

# adding the menu bar
# my_menu = Menu(parent, **options)
#adding menu bar in the widget
menu_bar = Menu(root)
# adding the file label to the menu
file_menu = Menu(menu_bar, tearoff=0)
# all file menu items will be added here next
menu_bar.add_cascade(label="File", menu=file_menu)
# adding menu items
file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', image=new_file_icon, underline=1, command=new_file)
# adding a line as a seperator between options
file_menu.add_separator()
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', image=open_file_icon, underline=1, command=open_file)
file_menu.add_command(label='Save', accelerator='Ctrl+S', compound='left',image=save_file_icon, underline=1, command=save)
file_menu.add_command(label='Save as', accelerator='Shift + Ctrl+S', compound='left', underline=1, command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt+F4', compound='left', underline=1, command=exit_editor)

# adding edit label to the menu bar
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
# adding menu items
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', compound='left', image=undo_icon, command=undo)
edit_menu.add_separator()
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', image=redo_icon, underline=1, command=redo)
edit_menu.add_separator()

# calls the function cut() using command to use this function
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', image=cut_icon, underline=1, command=cut)

# calls the function copy() using the command to use this function
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', image=cut_icon, underline=1, command=copy)

# calls the function paste() using the command to use this function
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', image=paste_icon, underline=1, command=paste)

edit_menu.add_separator()
# adding a callback to the find_text function
edit_menu.add_command(label='Find', accelerator='Ctrl+F', compound='left', image=find_icon, underline=1, command=find_text)
edit_menu.add_separator()
# adding a callback to the select function
edit_menu.add_command(label='Select All', accelerator='Ctrl+A', compound='left', underline=1, command=select_all)

# adding view label to the menu bar
view_menu = Menu(menu_bar, tearoff=0)

# show the line numbers
show_line_no = IntVar()
show_line_no.set(1)
view_menu.add_checkbutton(label='Show Line Numbers', variable=show_line_no)
# adding a button to give the user the option to higlight a line
# adding a callback to the button
to_highlight_line = BooleanVar()
view_menu.add_checkbutton(label='Highlight Current Line', onvalue=1, offvalue=0, variable=to_highlight_line, command=toggle_highlight)

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
about_menu.add_command(label='About', compound='left', underline=1, command=display_about_messagebox)
about_menu.add_separator()
about_menu.add_command(label='Help', compound='left', underline=1, command=display_help_messagebox)
# configuring the menu bar
root.config(menu=menu_bar)

# adding a frame widget to hold the shortcut icons
shortcut_bar = Frame(root, height=27)
shortcut_bar.pack(expand='no', fill='x')

# adding shortcut icons
# creating a tuple of icons
icons = ('new_file', 'open_file', 'save', 'cut', 'copy', 'paste', 'undo',
         'redo', 'find_text')
# loop through the list by creating a button widget, adding an image to the button
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon))
    # before adding callback command, we have to convert the string to an equivalent expression
    # using the eval command
    cmd = eval(icon)
    tool_bar = Button(shortcut_bar, image=tool_bar_icon, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side='left')


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

# binding the function to the ctrl-f quirk for find text function
content_text.bind('<Control-f>', find_text) # handling lowercase
content_text.bind('<Control-F>', find_text) # handling uppercase

# binding the function to the ctrl-N shortcut
content_text.bind('<Control-n>', new_file)# handling lowercase
content_text.bind('<Control-N>', new_file)# handling uppercase

# binding the function to the ctrl-O shortcut
content_text.bind('<Control-o>', open_file)# handling lowercase
content_text.bind('<Control-O>', open_file)# handling uppercase

# binding the function to the ctrl-s shortcut
content_text.bind('<Control-s>', save)
content_text.bind('<Control-S>', save)

# binding the function to the KeyPress-F1 shortcut
content_text.bind('<KeyPress-F1>', display_help_messagebox)

# binding the function to any keypress so it can update the function
content_text.bind('<Any-KeyPress>', on_content_changed)
# configuring the tag named active_line to have a different background colour
content_text.tag_configure('active_line', background='ivory2')

# all our code goes here

# overriding the the close button and redirecting it to the exit_editor()
root.protocol('WM_DELETE_WINDOW', exit_editor)
root.mainloop()


