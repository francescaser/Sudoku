import numpy as np
import random

sudoku=np.array([[1,2,3,4,5,6,7,8,9],[7,8,9,1,2,3,4,5,6],[9,7,8,2,3,1,6,4,5],[8,9,7,3,1,2,5,6,4],[2,3,1,6,4,5,8,9,7],[5,6,4,9,7,8,2,3,1],[3,1,2,5,6,4,9,7,8],[6,4,5,8,9,7,3,1,2]])
print(sudoku)

for i in range(81):

    val1=random.randint(1,9)
    val2=random.randint(1,9)

    for i in range(0,9):

        for j in range(0,9):

            if sudoku[i][j]==val2:
                sudoku[i][j]=val1
                
            elif sudoku[i][j]==val1:
                sudoku[i][j]=val2
print(sudoku)