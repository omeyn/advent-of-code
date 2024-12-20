import os
import itertools

os.chdir('2024/8')

def star1(input_file):
    f = open(input_file, "r")
    map = []
    freqs = {}
    for line in f:
        print(line.strip())
        map.append(list(line.strip()))

    # pretty_print(map)
    node_map = []
    for i in range(len(map)):
        node_map.append(['.'] * len(map[0]))
        for j in range(len(map[0])):
            print(freqs)
            symb = map[i][j]
            if symb != ".":
                if symb in freqs:
                    freqs[symb].append((i, j))
                else:
                    freqs[symb] = [(i, j)]

    node_count = 0
    for freq in freqs:
        coords = freqs[freq]
        print(f"{freq}: {coords}")
        pairs = list(itertools.combinations(coords, 2))
        for pair in pairs:
            # print(f"{pair}: {distance(pair[0], pair[1])}")
            a_delta_i = pair[0][0] - pair[1][0]
            a_delta_j = pair[0][1] - pair[1][1]
            a_node = pair[0][0] + a_delta_i, pair[0][1] + a_delta_j

            b_delta_i = pair[1][0] - pair[0][0]
            b_delta_j = pair[1][1] - pair[0][1]
            b_node = pair[1][0] + b_delta_i, pair[1][1] + b_delta_j

            if is_legal(a_node, map):
                if node_map[a_node[0]][a_node[1]] != '#':
                    node_count += 1
                    node_map[a_node[0]][a_node[1]] = '#'

            if is_legal(b_node, map):
                if node_map[b_node[0]][b_node[1]] != '#':
                    node_count += 1
                    node_map[b_node[0]][b_node[1]] = '#'


            # 5,5 and 3,3
            # a - b
            # di = 2, dj = 2 (applied to 5,5 gives 7,7)
            # b - a
            # di = -2, dj = -2 (applied to 3,3 gives 1,1)

            # 5,5 and 4,6
            # a - b
            # di = 1, -1 (applied to 5,5 gives 6, 4)
            # b - a 
            # di = -1, 1 (applied to 4,6 gives 3, 7)

    pretty_print(map)
    print()
    pretty_print(node_map)
    print(node_count)


def is_legal(node, map):
    return node[0] >= 0 and node[0] < len(map) and node[1] >= 0 and node[1] < len(map[0])

def pretty_print(maze):
    for row in maze:
        print("".join(row))

def factor_pair(diff_i, diff_j):
    factors = []
    for i in range(2, max(diff_i//2, diff_j//2)):
        if diff_i % i == 0 and diff_j % i == 0:
            factors.append(i)
    return factors

def star2(input_file):
    f = open(input_file, "r")
    map = []
    freqs = {}
    for line in f:
        print(line.strip())
        map.append(list(line.strip()))

    # pretty_print(map)
    node_map = []
    for i in range(len(map)):
        node_map.append(['.'] * len(map[0]))
        for j in range(len(map[0])):
            print(freqs)
            symb = map[i][j]
            if symb != ".":
                if symb in freqs:
                    freqs[symb].append((i, j))
                else:
                    freqs[symb] = [(i, j)]

    node_count = 0
    for freq in freqs:
        coords = freqs[freq]
        print(f"{freq}: {coords}")
        pairs = list(itertools.combinations(coords, 2))
        for pair in pairs:
            print(f"{pair}")
            if node_map[pair[0][0]][pair[0][1]] != '#':
                node_count += 1
                node_map[pair[0][0]][pair[0][1]] = '#'

            if node_map[pair[1][0]][pair[1][1]] != '#':
                node_count += 1
                node_map[pair[1][0]][pair[1][1]] = '#'

            a_delta_i = pair[0][0] - pair[1][0]
            a_delta_j = pair[0][1] - pair[1][1]
            a_factors = factor_pair(a_delta_i, a_delta_j)
            a_inc_i = a_delta_i
            a_inc_j = a_delta_j
            if len(a_factors) > 0:
                for factor in a_factors:
                    a_inc_i  = a_inc_i // factor
                    a_inc_j = a_inc_j // factor
                print(f"a factors: {a_factors}")
            print(f"a inc after factoring: {a_inc_i},{a_inc_j}")

            b_delta_i = pair[1][0] - pair[0][0]
            b_delta_j = pair[1][1] - pair[0][1]
            b_factors = factor_pair(b_delta_i, b_delta_j)
            b_inc_i = b_delta_i
            b_inc_j = b_delta_j
            if len(b_factors) > 0:
                for factor in b_factors:
                    b_inc_i  = b_inc_i // factor
                    b_inc_j = b_inc_j // factor
                print(f"b factors: {b_factors}")
            print(f"b inc after factoring: {b_inc_i},{b_inc_j}")

            a_legal = True
            b_legal = True
            a_node = pair[0]
            b_node = pair[0]
            while a_legal or b_legal:
                a_node = a_node[0] + a_inc_i, a_node[1] + a_inc_j
                b_node = b_node[0] - a_inc_i, b_node[1] - a_inc_j

                # print(f"checking node a: {a_node}")
                a_legal = is_legal(a_node, map)
                if a_legal:
                    if node_map[a_node[0]][a_node[1]] != '#':
                        node_count += 1
                        node_map[a_node[0]][a_node[1]] = '#'

                # print(f"checking node b: {a_node}")
                b_legal = is_legal(b_node, map)
                if b_legal:
                    if node_map[b_node[0]][b_node[1]] != '#':
                        node_count += 1
                        node_map[b_node[0]][b_node[1]] = '#'

                print(f"a_legal: {a_legal}, b_legal: {b_legal}")
                



            # 5,5 and 3,3
            # a - b
            # di = 2, dj = 2 (applied to 5,5 gives 7,7)
            # b - a
            # di = -2, dj = -2 (applied to 3,3 gives 1,1)

            # 5,5 and 4,6
            # a - b
            # di = 1, -1 (applied to 5,5 gives 6, 4)
            # b - a 
            # di = -1, 1 (applied to 4,6 gives 3, 7)


            # 3,3 and 45,50
            # diff 43, 47
            # divide by itself, then primes starting from 2 through 50/2 (2,3,5,7,11,13,17,19,23)

            # 1,1 and 13,7
            # diff 12, 6
            # primes gives 6, 3  then 2,1 (loop til nothing)


    pretty_print(map)
    # print()
    pretty_print(node_map)
    print(node_count)





input = "8-test.input"
input = "8.input"

# star1(input)
star2(input)