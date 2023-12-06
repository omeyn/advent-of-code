import os
import math
import re

os.chdir('2023/4')

def star1(input_file):
    f = open(input_file, "r")

    card_counts = {}
    for line in f:
        print(line)
        card_num = int(re.sub('\D', '', line.split(':')[0]))
        if card_num in card_counts:
            card_counts[card_num] = card_counts[card_num] + 1 # for the original, this line
        else:
            card_counts[card_num] = 1

        # print(f'card num {card_num}')
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

        # print(f'winners {winners}')
        # print(f'ours {ours}')

        win_count = 0
        for winner in winners:
            if winner in ours:
                win_count += 1
        print(f'win count {win_count}')
        bonus = card_counts[card_num]
        for i in range(1,win_count+1):
            target_card = card_num + i
            if target_card in card_counts:
                card_counts[target_card] = card_counts[target_card] + bonus
            else:
                card_counts[target_card] = bonus
        print(f'card counts {card_counts}')
        print('')

    result = sum(card_counts.values())
    
    print(f'final sum {result}')

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


input = "4-test.input"
input = "4.input"
star1(input)