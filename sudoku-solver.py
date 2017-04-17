def new_sudoku():
    sudoku = [];

    f = open("sudoku.txt", "r")
    while True:
        c = f.read(1)
        if not c:
            break
        elif c.isdigit():
            sudoku.append(c)

    f.close()
    return sudoku

def validate_sudoku(s):
    if not max(s) != 9:
        return False




    # Add more checks here
    return True


def main():
    result = True
    s = new_sudoku()
    result &= validate_sudoku(s)
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