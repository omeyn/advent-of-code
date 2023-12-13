import os
import re
import numpy as np

os.chdir('2023/8')

def all_z(node_set):
    result = True
    for node in node_set:
        result = result and node.endswith('Z')

    return result

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
    node_set = []
    for node in nodes.keys():
        if node.endswith('A'):
            node_set.append(node)
    print(f'starting nodes: {node_set}')

    min_moves = []
    for start_node in node_set:
        node = start_node
        moves = 0
        i = -1
        no_z = True
        while no_z:
            i += 1
            # print(f'check i {i}')
            moves += 1
            if right_left[i] == 'L':
                node = nodes[node][0]
            else:
                node = nodes[node][1]
            if node.endswith('Z'):
                print(f'for start {start_node} got end in Z {node}, moves: {moves}')
                min_moves.append(moves)
                no_z = False
                break
            if i == len(right_left)-1:
                i = -1

    print(f'least common multiple {np.lcm.reduce(min_moves)}')


# input = "8-test.input"
# input = "8-test2.input"
# input = "8-test3.input"
input = "8.input"
star1(input)
