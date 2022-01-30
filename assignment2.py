# This class is responsibile for all the necessary attributes
# class sudoku:
#     def __init__(self):
#         self.attempts = 0 # counts the number of backtracking
#         self.cells # this will count the resolved cells of the sudoku grid
#         self.grid = [0]*81 # sudoku grid which is intialised to cells of 0
#
#         self.rowIndex = [] # this will contains 9 indexes of each row
#         self.colIndex = [] #this will contain 9 indexes of each col
#         self.sub_grid_Index = [] # contains indexes of each 3x3 sub-grid
#
#         for i in range(0, 81, 9):
#             self.rowIndex.append(range(i, i+9))

# reading the text file that contains 10 sudoku's

class sudoku:

    def __init__(self):
    


    def open_text_file(self):
        f = open("C:\\Users\jadeh\PycharmProjects\Sudoku\Assignment 2 sudoku.txt", "r")
        # print(f.read())
        list_of_lists = []
        for line in f:
            stripped_line = line.splitlines()
            #line_list = stripped_line
            list_of_lists.append(stripped_line)
        f.close()
        print(list_of_lists)


    def sudoku_board(self):

        nums = []
        for row in range(3):
            nums.append([])

            for col in range(1,4):
                #subgrid = []
                #for i in range(3):
                    #for j in range(3):
                        #subgrid.append([3*row+i][3*col+j])
                nums[row].append(col)

        print("3x3 grid with numbers")
       # print(subgrid)
        print(nums)

#sudoku_board()
s = sudoku()
s.sudoku_board()
#open_text_file()