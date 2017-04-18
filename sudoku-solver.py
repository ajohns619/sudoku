from sys import argv

script, sudoku_name = argv

# Gets 9x9 sudoku with specified filename
def get_sudoku(name):
    sudoku = [];
    f = open(name, "r")
    while True:
        c = f.read(1)
        if not c:
            break
        elif c.isdigit():
            sudoku.append(int(c))

    f.close()
    return sudoku

# Checks that the digits are between and include 1 and 9
def check_min_max(s):
    if max(s) != 9 or min(s) != 1:
        return False
    return True

# Checks that the rows have no duplicates
def check_rows(s):
    for row in range(9):
        row_elems = [0 for i in range(10)]
        for col in range(9):
            elem = s[row * 9 + col]
            if row_elems[elem] == 0:
                row_elems[elem] = 1
            else:
                return False

    return True
           
# STUB
def check_cols(s):
    for col in range(9):
        col_elems = [0 for i in range(10)]
        for row in range(9):
            elem = s[col * 9 + row]
            if col_elems[elem] == 0:
                col_elems[elem] = 1
            else:
                return False

    return True

# Checks that all squares have only one instance of any digit
def check_squares(s):
    for first_row in range(3):
        for first_col in range(3):
            if not check_single_square(s, 3 * first_row, 3 * first_col):
                return False
    return True


# Checks that one specific square has only one instance of any digit
# first_row and first_col are the coordinares of the upper left element of the square
def check_single_square(s, first_row, first_col):
    square_elems = [0 for i in range(10)]
    for row in range(3):
        for col in range(3):
            elem = s[(first_row + row) * 9 + (first_col + col)]
            if square_elems[elem] == 0:
                square_elems[elem] = 1
            else:
                return False
    return True

# Calls all checks to validate sudoku
# And operators require all checks to be true
def validate_sudoku(s):
    result  = True
    result &= check_min_max(s)
    result &= check_rows(s)
    result &= check_cols(s)
    result &= check_squares(s)

    return result

def main():
    s = get_sudoku(sudoku_name)
    result = validate_sudoku(s)
    print result  

if __name__ == "__main__":
    main()