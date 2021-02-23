import numpy as np

grid = [] 
print("Enter the numbers of the puzzel rowwise:") 

for i in range(0, 9):
    a =[] 
    for j in range(0, 9):
        a.append(int(input())) 
    matrix.append(a) 

for i in range(0, 9): 
    for j in range(0, 9): 
        print(matrix[i][j], end=" ") 
    print()


def possible(row, column, number):
    global grid
    #Is the number appearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #Is the number appearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number:
            return False

    #Is the number appearing in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return

    print(np.matrix(grid))
    input('More possible solutions')

solve()