# thi9s program is an example of using tkinter and possibly a rock paper scissors game could be created
# 19/01/2021
# author: jade higgins
#  version 2

# import the library
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import random
import tkinter as tk

# randomised list
options = random.choice(['rock', 'paper', 'scissors'])


class Rock_paper_scissors:

    def __init__(self, options):
        self.options = options

        self.init_window()

    def init_window(self):

        # creating the main window of the application
        # the main object is called root
        root = Tk()

        # setting the dimension of the window to be 300x300
        root.geometry('300x300')
        # giving a title to the main window
        root.title('Rock, Paper, Scissors')
        # this label is what output will show on the window
        self.label = Label(root, text="Rock, Paper, Scissors!").pack()

        # creating a style object for rock, paper and scissor buttons
        self.RPSstyle = Style()
        self.RPSstyle.configure('TButton', font=
        ("calibri", 10, 'bold',),
                                foreground='red', background='#99c94b')

        # creating a button for rock
        self.rock = Button(root, text="Rock", style='TButton', command=self.rock_button)
        # setting the position of the button
        self.rock.pack(side='top')

        # creating a button for paper
        self.paper = Button(root, text="Paper", command=self.paper_button)

        # setting the positon for paper button
        self.paper.pack(side='top')

        # creating a button for scissors
        self.scissors = Button(root, text="Scissors", command=self.scissors_button)
        # setting the positon of scissors button
        self.scissors.pack(side='top')

        # creating a button for the score message
        self.message = Button(root, text="Score", command=root.destroy)
        # setting the position of the button
        self.message.pack(side="bottom")

        # # COMPUTER CHOICE BUTTON
        self.computer_choice = Button(root)
        self.computer_choice.pack(side="left")

        # the label for user_password
        self.computer_label = Label(root,
                                    text="Computers Choice").place(x=5,
                                                                   y=150)

        # calling mainloop method which is use when your application
        # is ready to run and it tells the code to keep displaying
        root.mainloop()

    def rock_button(self):

        user_choice = self.rock
        if user_choice == self.rock:
            if self.options == "rock":
                # updating the message button
                self.message.config(text="draw")
                self.message.update_idletasks()
                # updating the computers choice button
                self.computer_choice.config(text="ROCK")
                self.computer_choice.update_idletasks()
                print('draw')

            elif self.options == "paper":
                self.message.config(text="you loser")
                self.message.update_idletasks()
                # updating the computers choice button
                self.computer_choice.config(text="PAPER")
                self.computer_choice.update_idletasks()
                print('loser')

            elif self.options == "scissors":
                self.message.config(text="you win")
                self.message.update_idletasks()
                # updating the computers choice button
                self.computer_choice.config(text="SCISSORS")
                self.computer_choice.update_idletasks()
                print('winner')

            else:
                print('fail')

    def paper_button(self):

        user_choice = self.paper
        if user_choice == self.paper:
            if self.options == "rock":
                self.message.config(text="Winner")
                self.message.update_idletasks()
                # updating the computers choice button
                self.computer_choice.config(text="ROCK")
                self.computer_choice.update_idletasks()

            elif self.options == "paper":
                self.message.config(text="Draw")
                self.message.update_idletasks()
                # updating the computers choice button
                self.computer_choice.config(text="PAPER")
                self.computer_choice.update_idletasks()

            elif self.options == "scissors":
                self.message.config(text="you loser")
                self.message.update_idletasks()
                # updating the computers choice button
                self.computer_choice.config(text="SCISSORS")
                self.computer_choice.update_idletasks()

    def scissors_button(self):

        user_choice = self.scissors
        if user_choice == self.scissors:
            if self.options == "rock":
                self.message.config(text="You Loser")
                self.message.update_idletasks()
                # updating the computers choice button
                self.computer_choice.config(text="ROCK")
                self.computer_choice.update_idletasks()

            elif self.options == "paper":
                self.message.config(text="Winner")
                self.message.update_idletasks()
                # updating the computers choice button
                self.computer_choice.config(text="PAPER")
                self.computer_choice.update_idletasks()

            elif self.options == "scissors":
                self.message.config(text="Draw!")
                self.message.update_idletasks()
                # updating the computers choice button
                self.computer_choice.config(text="SCISSORS")
                self.computer_choice.update_idletasks()
    # def computerProgam(self):
    #     options = ['rock', 'paper', 'scissors']
    #
    #     random.choice(options)
    #     self.rockButton(options)


rps = Rock_paper_scissors(options)
# rps.rock_button()
# rps.paper_button()
# rps.scissors_button()
