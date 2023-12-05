import os
import re

os.chdir('2023/2')

def star1(input_file):
    f = open(input_file, "r")

    sum = 0
    for line in f:
        # print(line)
        game_id = int(re.sub('\D', '', line.split(':')[0]))
        # print(game_id)
        rounds = line.split(':')[1].split(';')
        # print(rounds)
        is_good = True
        for round in rounds:
            colours = round.split(',')
            for colour in colours:
                count, name = colour.strip().split(' ')
                # print(count + ' ' + name)
                if not possible(count, name):
                    is_good = False
        if is_good:
            sum += game_id
    print(sum)

def possible(count, colour_name):
    possible = True
    match colour_name:
        case 'red':
            if int(count) > 12:
                possible = False
        case 'green':
            if int(count) > 13:
                possible = False
        case 'blue':
            if int(count) > 14:
                possible = False

    return possible


input = "2-test.input"
input = "2.input"
star1(input)
