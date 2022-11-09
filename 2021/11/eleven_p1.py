import os

os.chdir('2021/11')

def star1(filename):

    board = []
    flashes = 0
    f = open(filename, "r")
    for line in f:
        if line.startswith("#"):
            continue
        line = line.strip()
        board.append([int(x) for x in list(line)])
    
    num_steps = 100
    print("start")
    # pretty_print(board)
    for i in range(num_steps):
        flashes += take_step(board)
        print("After Step {}".format(i+1))
        # pretty_print(board)
    print("total flashes {}".format(flashes))

def take_step(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] += 1
    
    # pretty_print(board)
    new_flashes = check_flash(board)
    flashes = new_flashes
    while new_flashes > 0:
        cleanup_flashes(board)
        update_neighbours(board)
        new_flashes = check_flash(board)
        flashes += new_flashes
    
    finalize_board(board)
    return flashes

def finalize_board(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] < 1:
                board[y][x] = 0

def cleanup_flashes(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                board[y][x] = -1
            if board[y][x] > 9:
                board[y][x] = 0


def update_neighbours(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                update_xy(board, x-1, y)
                update_xy(board, x+1, y)
                update_xy(board, x, y-1)
                update_xy(board, x, y+1)
                update_xy(board, x+1, y-1)
                update_xy(board, x+1, y+1)
                update_xy(board, x-1, y-1)
                update_xy(board, x-1, y+1)
    # pretty_print(board)

def update_xy(board, x, y):
    # print("attempting update of {} {}".format(x, y))
    if y in range(len(board)) and x in range(len(board[0])):
        # print("doing update of {} {}".format(x, y))
        if board[y][x] > 0:
            board[y][x] += 1
            # print("{} {} becomes {}".format(x,y,board[y][x]))
        # else:
            # print("{} {} is < 1, ignoring".format(x,y))

def check_flash(board):
    flashes = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] > 9:
                flashes += 1

    return flashes

def pretty_print(board):
    print("")
    for row in board:
        line = ""
        for foo in row:
            line = line + " " + str(foo)
        print(line)
    print("")

def star2(filename):

    board = []
    flashes = 0
    f = open(filename, "r")
    for line in f:
        if line.startswith("#"):
            continue
        line = line.strip()
        board.append([int(x) for x in list(line)])
    
    num_steps = 500
    print("start")
    # pretty_print(board)
    for i in range(num_steps):
        print("After Step {}".format(i+1))
        if take_step(board) == 100:
            print("Done on step {}".format(i+1))
            break
        
filename = "11.input"
# filename = "11-test.input"
# filename = "11-simple.input"
# star1(filename)
star2(filename)
#test