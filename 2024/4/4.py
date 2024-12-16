import os
import re
import numpy as np

os.chdir('2024/4')

def star1(input_file):
    f = open(input_file, "r")

    grid = list()
    count = 0
    x = 0
    for line in f:
        grid.append(list(line.strip()))
        
    display_grid(grid)
    count += count_straight(grid)
    print(f"\n\n{count}")

    grid_prime = np.transpose(grid)
    count += count_straight(grid_prime)
    display_grid(grid_prime)
    print(f"\n\n{count}")

    count += count_diagonals(grid)


    print(count)

def count_diagonals(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i + 3 < len(grid) and j + 3 < len(grid[0]):
                if grid[i][j] == 'X' and grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A' and grid[i+3][j+3] == 'S':
                    count += 1
                if grid[i][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'M' and grid[i+3][j+3] == 'X':
                    count += 1
            if i + 3 < len(grid) and j - 3 >= 0:
                if grid[i][j] == 'X' and grid[i+1][j-1] == 'M' and grid[i+2][j-2] == 'A' and grid[i+3][j-3] == 'S':
                    count += 1
                if grid[i][j] == 'S' and grid[i+1][j-1] == 'A' and grid[i+2][j-2] == 'M' and grid[i+3][j-3] == 'X':
                    count += 1
    
    print(f"\n\n diag: {count}")

    return count

def count_straight(grid):
    count = 0
    for row in grid:
        line = "".join(row)
        count += len(re.findall(r'XMAS', line))
        count += len(re.findall(r'SAMX', line))

    return count

def display_grid(grid):
    for row in grid:
        print("".join(row))

def star2(input_file):
    f = open(input_file, "r")

    grid = list()
    count = 0
    for line in f:
        grid.append(list(line.strip()))
    count += count_mas(grid)

    print(count)

def count_mas(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i + 2 < len(grid) and j + 2 < len(grid[0]):
                if grid[i][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'M' and grid[i+2][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i][j+2] == 'M':
                    count += 1
                if grid[i][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'M' and grid[i+2][j] == 'M' and grid[i+1][j+1] == 'A' and grid[i][j+2] == 'S':
                    count += 1
                if grid[i][j] == 'M' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'S' and grid[i+2][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i][j+2] == 'M':
                    count += 1
                if grid[i][j] == 'M' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'S' and grid[i+2][j] == 'M' and grid[i+1][j+1] == 'A' and grid[i][j+2] == 'S':
                    count += 1

            # M S   S M   S S  M M
            #  A     A     A    A
            # M S   S M   M M  S S
    return count

input = "4-test.input"
input = "4.input"
# star1(input)
star2(input)
