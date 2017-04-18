from sys import argv

script, sudoku_name = argv

# Gets 9x9 sudoku with specified filename and stores it in list
def get_sudoku(name):
    sudoku = [];
    file = open(name, "r")

    while True:
        # Read a single character at a time
        c = file.read(1)
        if not c:
            break
        elif c.isdigit():
            sudoku.append(int(c))
    file.close()
    return sudoku

# Checks that the digits are between and include 1 and 9
def check_min_max(sudoku):
    if max(sudoku) != 9 or min(sudoku) != 1:
        return False
    return True

# Checks that the rows have no duplicates
def check_rows(sudoku):
    for row in range(9):
        row_elems = [0 for i in range(10)]
        for col in range(9):
            elem = sudoku[row * 9 + col]
            if row_elems[elem] == 0:
                row_elems[elem] = 1
            else:
                return False
    return True
           
# Checks that the columns have no duplicates
def check_cols(sudoku):
    for col in range(9):
        col_elems = [0 for i in range(10)]
        for row in range(9):
            elem = sudoku[col * 9 + row]
            if col_elems[elem] == 0:
                col_elems[elem] = 1
            else:
                return False

    return True

# Checks that all squares have only one instance of any digit
def check_squares(sudoku):
    for first_row in range(3):
        for first_col in range(3):
            if not check_single_square(sudoku, 3 * first_row, 3 * first_col):
                return False
    return True


# Checks that one specific square has only one instance of any digit
# first_row and first_col are the coordinares of the upper left element of the square
def check_single_square(sudoku, first_row, first_col):
    square_elems = [0 for i in range(10)]
    for row in range(3):
        for col in range(3):
            elem = sudoku[(first_row + row) * 9 + (first_col + col)]
            if square_elems[elem] == 0:
                square_elems[elem] = 1
            else:
                return False
    return True

# Calls all checks to validate sudoku; &-operators require all checks to be true
def validate_sudoku(sudoku):
    if (len(sudoku) != 81):
        return False

    result  = True
    result &= check_min_max(sudoku)
    result &= check_rows(sudoku)
    result &= check_cols(sudoku)
    result &= check_squares(sudoku)

    return result

def main():
    sudoku = get_sudoku(sudoku_name)
    result = validate_sudoku(sudoku)
    print result  

if __name__ == "__main__":
    main()