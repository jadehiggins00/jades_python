import numpy



from pprint import pprint



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



# this method is used to check if there is the same number in each
# row and column while also checking each 3x3 grid box
def possible(list_of_lists,num, row, col):
    #print('working')
    # checking the rows if there is the same number in each row
    for value in range(0,9):
        if list_of_lists[row][value] == num:
            return False

    # checking if the number is appearing in the given col
    for value in range(0,9):
        if list_of_lists[value][col] == num:
            return False

    # finding the top left row and col of the 3x3 box
    row_corner = row - row % 3
    col_corner = col - col % 3
    for i in range(3):
        for j in range(3):
            if list_of_lists[row_corner + i][col_corner + j] == num:
                return False
    return True

def check_cells(list_of_lists):
    # checking each row
    for i in range(9):
        # checking each column
        for j in range(9):
            # if the sudoku grid contains 0 in the row
            if list_of_lists == 0:
                return i,j
    # if all fields are filled with numbers between 1-9 return none none
    return None, None

# we will solve each sudoku puzzle using the backtracking
# algorithm. each puzzle contained inside a list of lists
def solve_sudoku(list_of_lists):
        # checking for the empty fields
        # for row in range(0,9):
        #     for col in range(0,9):
        #         if self.list_of_lists[row][col] == 0:
        #             for num in range(1,10):
        #                 if self.possible(row, col, num):
        #                     self.list_of_lists[row][col] = num
        #                     self.solve()
        #                     self.list_of_lists = 0
        #             return
        # print(self.list_of_lists)


    # Choosing somewhere on the sudoku board to make a guess
    row, col = check_cells(list_of_lists)

    # if all the fields are filled with numbers between 1-9
    # then the puzzle has been solved
    if row is None:
        return True

    # If there is a cell marked with 0, then we place a value between 1 and 9
    for value in range(1, 10): # 1 - 9
        # Now we check if this is a possible value
        if possible(list_of_lists,value, row, col):
            # if this is a valid value, then we place on the board
            list_of_lists[row][col] = value
            # then we recursively call the function
            if solve_sudoku(list_of_lists):
                return True

        # if nothing gets returned true or is not valid value
        # then we backtrack
        list_of_lists[row][col] = -1

    # if none of the numbers we tried work, then the sudoku is unsolvable
    return False

# this method is used to open the text file and put the contents into a list of lists
if __name__ == '__main__':
    #file = open("C:\\Users\jadeh\PycharmProjects\Sudoku\Assignment 2 sudoku.txt", "r")
    file = open("C:\\Users\jadeh\Documents\Python-Projects\jades_python\sudoku1.txt", "r")
    list_of_lists = []
    for line in file:
        stripped_line = line.splitlines()
        #file.split(",")
        list_of_lists.append(stripped_line)
       # list_of_lists.split(",")

    file.close()

    line = 0
    title = 'Grid'
    # while(True):
    #     while title not in list_of_lists and line and line<len(list_of_lists)-1:
    #         #increment to the next line
    #         line+=1
    #         if line == len(list_of_lists)-1:
    #             print(title+'')
    #             line+=1
        # converting the list to a numpy array
       # arr = numpy.array(list_of_lists)

    #print("array: ", arr)
    print(solve_sudoku(list_of_lists))
    pprint(list_of_lists)
#
#
#

# #s.is_valid()
#s.open_text_file()
