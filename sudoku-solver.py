def new_sudoku():
    sudoku = [];
    f = open("sudoku.txt", "r")
    while True:
        c = f.read(1)
        if not c:
            break
        elif c.isdigit():
            sudoku.append(int(c))

    f.close()
    return sudoku

def validate_sudoku(s):
    result = True
    if max(s) != 9 or min(s) != 1:
        return False
    result &= check_rows(s)

    result &= check_cols(s)
    result &= check_squares(s)

    # Add more checks here

    return result

# Checks that the rows have no duplicates
def check_rows(s):
    for row in range(9):
        row_elems = [0 for i in range(10)]
        for col in range(9):
            index = row * 9 + col
            if row_elems[s[index]] == 0:
                row_elems[s[index]] = 1
            else:
                return False

    return True
           
# STUB
def check_cols(s):
    return True

# STUB
def check_squares(s):
    return True

def main():
    s = new_sudoku()
    result = validate_sudoku(s)
    print result  

if __name__ == "__main__":
    main()

'''
A solved sudoku puzzle is a nine-by-nine graymap with these properties:

    - The maximum pixel intensity (aka the denominator for scaled integers) is nine.
    - No pixel has zero intensity.

    - In each row, no two pixels have the same intensity.
    - In each column, no two pixels have the same intensity.
    - If the nine-by-nine graymap is divided into nine three-by-three submaps
      (like a tic-tac-toe board), in each three-by-three submap, no two pixels have the same intensity.
'''