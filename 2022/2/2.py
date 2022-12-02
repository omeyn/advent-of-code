import os

os.chdir('2')

# Opponent
# A is rock
# B is paper
# C is scissors

# Response move
# X rock, score 1,
# Y paper, score 2
# Z scissors, score 3

# round result
# X is lose
# Y is draw
# Z is win

# Points
# 0 for loss, 3 for draw, 6 for win

def round_score(them, me):
    score = 0
    if them == 'A':
        if me == 'X':
            score = 3
        elif me == 'Y':
            score = 6
    elif them == 'B':
        if me == 'Y':
            score = 3
        elif me == 'Z':
            score = 6
    else: # them == C
        if me == 'X':
            score = 6
        elif me == 'Z':
            score = 3
    return score

def move_score(me):
    if me == 'X':
        return 1
    if me == 'Y':
        return 2
    if me == 'Z':
        return 3

def find_my_move(them, result):
    move = ''
    if result == 'X': # loss
        if them == 'A':
            move = 'Z'
        elif them == 'B':
            move = 'X'
        else: # them == C
            move = 'Y'
    elif result == 'Y': # draw
        if them == 'A':
            move = 'X'
        elif them == 'B':
            move = 'Y'
        else:
            move = 'Z'
    else: # result == Z, win
        if them == 'A':
            move = 'Y'
        elif them == 'B':
            move = 'Z'
        else: # them == C
            move = 'X'

    return move

def star1(filename):
    sums = []
    f = open(filename, "r")
    sum = 0
    for line in f:
        if line.strip() != '':
            them, me = line.strip().split(' ')
            print(f"got them {them} me {me}")
            sum += round_score(them, me) + move_score(me)

    print(f"star 1 sum {sum}")

def star2(filename):
    sums = []
    f = open(filename, "r")
    sum = 0
    for line in f:
        if line.strip() != '':
            them, result = line.strip().split(' ')
            # print(f"got them {them} result {result}")
            me = find_my_move(them, result)
            # print(f"got me {me}")
            sum += round_score(them, me) + move_score(me)

    print(f"star 2 sum {sum}")

filename = "2.input"
# filename = "2-test.input"
# star1(filename)
star2(filename)