import os

os.chdir('2021/9')

def star1(filename):
    f = open(filename, "r")
    seafloor = []
    for line in f:
        row = list(line.strip())
        row = [int(x) for x in row]
        seafloor.append(row)

    width = len(seafloor[0])
    height = len(seafloor)

    lows = [[0 for x in range(width)] for y in range(height)]
    # print(seafloor)
    # print(lows)

    # top left is origin
    for y in range(height):
        for x in range(width):
            here = seafloor[y][x]
            if x > 0 and x < width-1 and y > 0 and y < height-1:
                up = seafloor[y-1][x]
                down = seafloor[y+1][x]
                right = seafloor[y][x+1]
                left = seafloor[y][x-1]
                if here < up and here < down and here < left and here < right:
                    lows[y][x] = 1 + seafloor[y][x]
            elif x == 0:
                if y == 0:
                    down = seafloor[y+1][x]
                    right = seafloor[y][x+1]
                    if here < down and here < right:
                        lows[y][x] = 1 + seafloor[y][x]
                elif y == height-1:
                    up = seafloor[y-1][x]
                    right = seafloor[y][x+1]
                    if here < up and here < right:
                        lows[y][x] = 1 + seafloor[y][x]
                else:
                    up = seafloor[y-1][x]
                    down = seafloor[y+1][x]
                    right = seafloor[y][x+1]
                    if here < up and here < down and here < right:
                        lows[y][x] = 1 + seafloor[y][x]
            elif y == 0:
                if x == width-1:
                    down = seafloor[y+1][x]
                    left = seafloor[y][x-1]
                    if here < down and here < left:
                        lows[y][x] = 1 + seafloor[y][x]
                else:
                    down = seafloor[y+1][x]
                    right = seafloor[y][x+1]
                    left = seafloor[y][x-1]
                    if here < down and here < left and here < right:
                        lows[y][x] = 1 + seafloor[y][x]
            elif x == width-1:
                if y == height-1:
                    up = seafloor[y-1][x]
                    left = seafloor[y][x-1]
                    if here < up and here < left:
                        lows[y][x] = 1 + seafloor[y][x]
                else:
                    up = seafloor[y-1][x]
                    down = seafloor[y+1][x]
                    left = seafloor[y][x-1]
                    if here < up and here < down and here < left:
                        lows[y][x] = 1 + seafloor[y][x]
            elif y == height-1:
                up = seafloor[y-1][x]
                right = seafloor[y][x+1]
                left = seafloor[y][x-1]
                if here < up and here < left and here < right:
                    lows[y][x] = 1 + seafloor[y][x]

    # print(lows)
    lowsum = 0
    for row in lows:
        for low in row:
            lowsum += low
    # print(lowsum)
    return lows


filename = "9.input"
filename = "9-test.input"
star1(filename)