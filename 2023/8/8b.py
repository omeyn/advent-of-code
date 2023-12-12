import os
import re

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

    i = -1
    while True:
        i += 1
        # print(f'check i {i}')
        moves += 1
        new_nodes = []
        for node in node_set:
            if right_left[i] == 'L':
                new_nodes.append(nodes[node][0])
            else:
                new_nodes.append(nodes[node][1])
        if all_z(new_nodes):
            print(f'got all end in Z {new_nodes}, moves: {moves}')
            break
        else:
            node_set = new_nodes
        if i == len(right_left)-1:
            i = -1


# input = "8-test.input"
# input = "8-test2.input"
# input = "8-test3.input"
input = "8.input"
star1(input)
