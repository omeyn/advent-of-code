import os
import copy

os.chdir('2021/5')

def star1():
    f = open("5.input", "r")
    # f = open("5-test.input", "r")

    board = [[0 for y in range(1000)] for x in range(1000)]
    for line in f:
        print(line)
        split_line = line.split()
        start = [int(x) for x in split_line[0].split(',')]
        end = [int(x) for x in split_line[2].split(',')]
        if start[0] == end[0]:
            dir = "vert"
        elif start[1] == end[1]:
            dir = "hori"
        else:
            dir = "diag"

        if dir == "vert":
            r = abs(end[1] - start[1]) + 1
            for dy in range(r):
                x = start[0]
                y = start[1]
                if end[1] - start[1] > 0:
                    board[x][y + dy] = board[x][y + dy] + 1
                    # print("updating {} {}".format(x, y + dy))
                else:
                    board[x][y - dy] = board[x][y - dy] + 1
                    # print("updating {} {}".format(x, y - dy))
        elif dir == "hori":
            r = abs(end[0] - start[0]) + 1
            for dx in range(r):
                x = start[0]
                y = start[1]
                if end[0] - start[0] > 0:
                    board[x + dx][y] = board[x + dx][y] + 1
                    # print("updating {} {}".format(x + dx, y))
                else:
                    board[x - dx][y] = board[x - dx][y] + 1
                    # print("updating {} {}".format(x - dx, y))
        # comment this bit for star1
        else:
            board = fill_diag(start[0], start[1], end[0], end[1], board)
            
    overlap = 0
    for x in range(1000):
        for y in range(1000):
            if board[x][y] >= 2:
                overlap = overlap + 1

    print("Danger zone count: {}".format(overlap))

# python will change the orginal through "pass by assignment"
def fill_diag(start_x, start_y, end_x, end_y, board):
    # this is CRAZY slow, wow
    # safe = copy.deepcopy(board)
    safe = board
    # 45 deg lines means diff in x and y will be same
    diff = abs(end_x - start_x) + 1
    dir_x = "pos"
    dir_y = "pos"
    if (end_x - start_x < 0):
        dir_x = "neg"
    if (end_y - start_y < 0):
        dir_y = "neg"

    for d in range(diff):
        targ_x = 0
        targ_y = 0
        if dir_x == "pos":
            targ_x = start_x + d
        else:
            targ_x = start_x - d
        if dir_y == "pos":
            targ_y = start_y + d
        else:
            targ_y = start_y - d
        # print("Updating {} {}".format(targ_x, targ_y))
        safe[targ_x][targ_y] = safe[targ_x][targ_y] + 1

    return safe

star1()