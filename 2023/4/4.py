import os
import math

os.chdir('2023/4')

def star1(input_file):
    f = open(input_file, "r")

    sum = 0
    for line in f:
        print(line)
        winners = []
        for x in line.split(':')[1].split('|')[0].split(' '):
            if len(x.strip()) > 0:
                winners.append(int(x))
        winners.sort()
        ours = []
        for x in line.split(':')[1].split('|')[1].split(' '):
            if len(x.strip()) > 0:
                ours.append(int(x))
        ours.sort()

        print(f'winners {winners}')
        print(f'ours {ours}')

        win_count = 0
        for winner in winners:
            if winner in ours:
                win_count += 1
        score = 0
        if win_count > 0:
            score = int(math.pow(2, win_count-1))
        print(f'win count {win_count} for score {score}')
        print('')
        sum += score
    
    print(f'final sum {sum}')

# scoring
# 1 gives 1
# 2 gives 2
# 3 gives 4
# 4 gives 8
# 5 gives 16

# 2^0 = 1
# 2^1 = 2
# 2^2 = 4
# 2^3 = 8
# 2^4 = 16


# input = "4-test.input"
input = "4.input"
star1(input)