import os
import re

os.chdir('2023/2')

def star2(input_file):
    f = open(input_file, "r")

    sum = 0
    for line in f:
        print(line)
        colour_max = {}
        game_id = int(re.sub('\D', '', line.split(':')[0]))
        # print(game_id)
        rounds = line.split(':')[1].split(';')
        # print(rounds)
        is_good = True
        for round in rounds:
            colours = round.split(',')
            for colour in colours:
                count, name = colour.strip().split(' ')
                count = int(count)
                if name in colour_max:
                    if count > colour_max[name]:
                        colour_max[name] = count
                else:
                    colour_max[name] = count
        print(colour_max)
        power = colour_max['red'] * colour_max['green'] * colour_max['blue']
        print(f"game {game_id} power {power}")
        print("")
        sum += power

    print(sum)



input = "2-test.input"
input = "2.input"
star2(input)
