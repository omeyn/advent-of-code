import os
import re

os.chdir('2023/8')

def star1(input_file):
    f = open(input_file, "r")

    right_left = f.readline().strip()
    f.readline()
    nodes = {}
    for line in f:
        # print(line)

        name = line.split('=')[0].strip()
        tuple = line.split('=')[1].strip().split(',')
        tuple = [re.sub('\(|\)', '', t.strip()) for t in tuple]
        # print(f'name {name} tuple {tuple}')
        nodes[name] = tuple

    moves = 0
    node = 'AAA'
    i = -1
    while True:
        i += 1
        # print(f'check i {i}')
        moves += 1
        if right_left[i] == 'L':
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        if node == 'ZZZ':
            print(f'got ZZZ, moves: {moves}')
            break
        if i == len(right_left)-1:
            i = -1


input = "8-test.input"
input = "8-test2.input"
input = "8.input"
star1(input)
