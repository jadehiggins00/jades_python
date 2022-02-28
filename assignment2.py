import numpy

class Sudoku:

    def __init__(self):
        # we will now create the board
        self.row = [] # will contain 9 rows
        self.col = [] # will contain 9 columns


    def open_text_file(self):
        file = open("C:\\Users\jadeh\PycharmProjects\Sudoku\Assignment 2 sudoku.txt", "r")
        list_of_lists = []
        for line in file:
            stripped_line = line.splitlines()
            list_of_lists.append(stripped_line)
        file.close()

        # converting the list to a numpy array
        arr = numpy.array(list_of_lists)
        print("array: ", arr)

s = Sudoku()
s.open_text_file()