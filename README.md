# Sudoku Checker

This program reads in a solved sudoku from a file and checks if it has been solved correctly.

A correct sudoku has the following properties (and the program follows this logical reasoning):
* The sudoku has 81 elements.
* The smallest value in the sudoku is 1, and the largest value is 9.
* No row contains any duplicate integers.
* No column contains any duplicate integers.
* No 9x9 square contains any duplicate integers.

I created this program to learn python, especially I/O functionality and list comprehension.


## sudoku-checker.py
This file solves the problem using only standard python lists, and python list comprehension. It is completely correct, but since we are representing a two dimensional, 9x9 object, it can get ugly. For example, to get an element at a certain row and column, the following code is required: 
    
    sudoku[col * 9 + row]

## sudoku-checker-numpy.py
This file utilizes NumPy to clean up the code. The above code snippet can be rewritten as 

    sudoku[col][row]
    
Much clearer! Additionally, NumPy includes powerful functions to operate on its arrays and matrices. For example, instead of writing two seperate algorithms to check that neither the rows, nor the columns contain duplicates, I can write one function to check the rows, and then pass the transpose of the sudoku into the same function to check the columns.
    
    >>> sudoku
    array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9]])
    >>> t_sudoku = np.transpose(sudoku)
    >>> t_sudoku
    array([[1, 1, 1, 1, 1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2, 2, 2, 2, 2],
           [3, 3, 3, 3, 3, 3, 3, 3, 3],
           [4, 4, 4, 4, 4, 4, 4, 4, 4],
           [5, 5, 5, 5, 5, 5, 5, 5, 5],
           [6, 6, 6, 6, 6, 6, 6, 6, 6],
           [7, 7, 7, 7, 7, 7, 7, 7, 7],
           [8, 8, 8, 8, 8, 8, 8, 8, 8],
           [9, 9, 9, 9, 9, 9, 9, 9, 9]])
    
      
