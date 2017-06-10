# sudoky-checker-numpy.py
# Author: Alex Johnson
#
# Date: 5/21/2017


from sys import argv
import numpy as np

# Reads in 9x9 sudoku with specified filename and stores it in list
def get_sudoku(name):
    sudoku = [];
    file = open(name, "r")

    while True:
        c = file.read(1)
        if not c:
            break
        elif c.isdigit():
            sudoku.append(int(c))
    file.close()

    return sudoku

# Checks that the digits are between and include 1 and 9
def check_min_max(sudoku):
    # Returns true if the min is 1 and the max is 9
    return (np.amax(sudoku) == 9 and np.amin(sudoku) == 1)

# Checks that the rows have no duplicates
def check_rows(sudoku):
    for row in range(9):
        # row_elems is a usual python array, since it is one-dimensional
        row_elems = [0 for i in range(10)]

        for col in range(9):
            elem = sudoku[row][col]
            if row_elems[elem] == 0:
                row_elems[elem] = 1
            else:
                return False
    return True
           
# Checks that the columns have no duplicates
def check_cols(sudoku):
    # Checking the rows is the same as checking columns of the transpose
    return check_rows(np.transpose(sudoku))

# Checks that all squares have only one instance of any digit
def check_squares(sudoku):
    for row in range(3):
        for col in range(3):
            if not three_by_three_square(sudoku, 3 * row, 3 * col):
                return False
    return True

# Checks that one specific square has only one instance of any digit
# first_row and first_col are the coordinares of the upper left element of the square
def three_by_three_square(sudoku, first_row, first_col):
    square_elems = [0 for i in range(10)]
    for row in range(3):
        for col in range(3):
            elem = sudoku[(first_row + row)][(first_col + col)]
            if square_elems[elem] == 0:
                square_elems[elem] = 1
            else:
                return False
    return True

# Calls all checks to validate sudoku; &-operators require all checks to be true
def validate_sudoku(sudoku):
    if (len(sudoku) != 81):
        return False

    # Create a numpy element: 9 dimensional array with 9 elements
    np_sudoku = np.array(sudoku).reshape(9, 9)

    result  = True
    result &= check_min_max(np_sudoku)
    result &= check_rows(np_sudoku)
    result &= check_cols(np_sudoku)
    result &= check_squares(np_sudoku)

    return result

def main():
    sudoku = get_sudoku(argv[1])
    result = validate_sudoku(sudoku)
    print(result)  

if __name__ == "__main__":
    main()
