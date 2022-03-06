import numpy

class Sudoku:



    # def __init__(self):
    #     # we will now create the board
    #     self.row = [] # will contain 9 rows
    #     self.col = [] # will contain 9 columns
#
#
#     def is_valid(self, list_of_lists, row, col, num):
#         # checking the rows if there is the same number in each row
#         for value in range(9):
#             if list_of_lists[row][value] == num:
#                 return False
#
#         #checking the columns if there is the same number in each col
#         for value in range(9):
#             if list_of_lists[value][col] == num:
#                 return False
#
#         # finding the top left row and col of the 3x3 box
#         row_corner = row - row % 3
#         col_corner = col - col % 3
#         for i in range(3):
#             for j in range(3):
#                 if list_of_lists[row_corner + i][col_corner + j] == num:
#                     return False
#
#         return True
#
#     def sudoku_board(self):
#         pass
#

    def open_text_file(self):
        file = open("C:\\Users\jadeh\PycharmProjects\Sudoku\Assignment 2 sudoku.txt", "r")
        self.list_of_lists = []
        for line in file:
            stripped_line = line.splitlines()
            self.list_of_lists.append(stripped_line)
        file.close()

        # converting the list to a numpy array
        #arr = numpy.array(list_of_lists)

        #print("array: ", arr)
        print(self.list_of_lists)
        self.possible(self.list_of_lists)

    def possible(self, row, col, num):
        print('working')
       # checking the rows if there is the same number in each row
        for value in range(0,9):
            if self.list_of_lists[row][value] == num:
                return False

        # checking if the number is appearing in the given col
        for value in range(0,9):
            if self.list_of_lists[value][col] == num:
                return False

        # finding the top left row and col of the 3x3 box
        row_corner = row - row % 3
        col_corner = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.list_of_lists[row_corner + i][col_corner + j] == num:
                    return False
        return True


    def solve(self,):
        

#
#
#
s = Sudoku()
s.open_text_file()
# #s.is_valid()
# s.open_text_file()
