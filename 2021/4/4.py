import os

os.chdir('2021/4')

class BingoBoard:
    # board is 2d array - first index is row, 2nd is col
    def __init__(self, board, drawn_numbers):
        self.drawn_numbers = drawn_numbers
        self.board = board
        self.state = [[0 for y in range(5)] for x in range(5)]
        # print("Creating new board {}".format(board))
        for i in range(len(drawn_numbers)-1):
            drawn = drawn_numbers[i]
            # print("checking draw {}".format(drawn))
            self.update_state(drawn)
            if self.bingo():
                self.winning_num = drawn
                self.winning_pos = i
                print("Bingo at ball {} with value {}".format(i, drawn))
                break

    def update_state(self, drawn):
        for row in range(5):
            for col in range(5):
                if self.board[row][col] == drawn:
                    self.state[row][col] = 1
                    break

    def bingo(self):
        winning_row = [1 for x in range(5)]
        for row in range(5):
            if self.state[row] == winning_row:
                return True
        # TODO: dumb way to do transpose, learn zip() or pandas
        for col in range(5):
            tmp_col = []
            for row in range(5):
                tmp_col.append(self.state[row][col])
            if tmp_col == winning_row:
                return True

    def winning_score(self):
        unmarked_sum = 0
        for row in range(5):
            for col in range(5):
                if self.state[row][col] == 0:
                    unmarked_sum = unmarked_sum + int(self.board[row][col])
        final_score = int(self.winning_num) * unmarked_sum
        return final_score



def star1():
    f = open("4.input", "r")
    drawn_numbers = next(f).split(",")
    next(f) # discard blank line
    boards = []
    board = []
    for line in f:
        if len(line.strip()) == 0:
            # end of board
            boards.append(BingoBoard(board=board, drawn_numbers=drawn_numbers))
            board = []
        else:
            board.append(line.strip().split())
    
    winning_board = None
    lowest_pos = 1000
    for board in boards:
        if board.winning_pos < lowest_pos:
            winning_board = board
            lowest_pos = board.winning_pos
    
    print("winning board had pos {} with ball val {} and score {}".format(lowest_pos, winning_board.winning_num, winning_board.winning_score()))



star1()