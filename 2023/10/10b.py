import os

os.chdir('2023/10')

class PipeNode:
    value = 0
    east = None
    west = None
    north = None
    south = None

    def __init__(self, pipe_type: str, x: int, y: int):
        self.pipe_type = pipe_type
        self.x = x
        self.y = y
    
def find_neighbour(pipe_node: PipeNode, map: list, x_delta: int, y_delta: int):
    new_x = pipe_node.x + x_delta
    new_y = pipe_node.y + y_delta
    if new_x >= 0 and new_x < len(map[0]) and new_y >=0 and new_y < len(map): # it's on the map
        new_node = PipeNode(pipe_type=map[new_y][new_x], x=new_x, y=new_y)
        if new_node.pipe_type != '.':
            return new_node

    return None

def find_compass_neighbour(node: PipeNode, map: list, direction: str):
    match direction:
        case 'north':
            return find_neighbour(node, map, x_delta=0, y_delta=-1)
        case 'east':
            return find_neighbour(node, map, x_delta=1, y_delta=0)
        case 'south':
            return find_neighbour(node, map, x_delta=0, y_delta=1)
        case 'west':
            return find_neighbour(node, map, x_delta=-1, y_delta=0)
        
def print_map(pipe_map):
    for y in pipe_map:
        print(*y)


def build_map(line_count, line_length, starting_char):
    pipe_map = []
    for i in range(line_count):
        row = []
        for i in range(line_length):
            row.append(starting_char)
        pipe_map.append(row)
    return pipe_map


def star1(input_file):
    f = open(input_file, "r")
    map = []
    pipe_map = []
    for line in f:
        print(line.strip())
        map.append(line.strip())
        if 'S' in line:
            starting_node = PipeNode('S', y=len(map)-1, x=line.find('S'))
            # print(f'found S at 0-based {starting_node.x},{starting_node.y}, proof {map[starting_node.y][starting_node.x]}')

    pipe_path = [starting_node]
    pipe_map = build_map(len(map), len(map[0]), 0)
    symbol_map = build_map(len(map), len(map[0]), '.')
    symbol_map[starting_node.y][starting_node.x] = 'S'
    # print(f'empty pipe map {pipe_map}')
    pipe_map[starting_node.y][starting_node.x] = 'H'
    

    north = find_compass_neighbour(starting_node, map, 'north')
    east = find_compass_neighbour(starting_node, map, 'east')
    south = find_compass_neighbour(starting_node, map, 'south')
    west = find_compass_neighbour(starting_node, map, 'west')
    if north:
        if north.pipe_type in ['|', '7', 'F']:
            starting_node.north = north
            current_node = north
            current_node.south = starting_node
    if south:
        if south.pipe_type in ['|', 'J', 'L']:
            starting_node.south = south
            current_node = south
            current_node.north = starting_node
    if east:
        if east.pipe_type in ['-', 'J', '7']:
            starting_node.east = east
            current_node = east
            current_node.west = starting_node
    if west:
        if west.pipe_type in ['-', 'F', 'L']:
            starting_node.west = west
            current_node = west
            current_node.east = starting_node
            
    print(f'first node from S is {current_node.pipe_type}')
    pipe_path.append(current_node)
    path_symbols = ['S']
    path_symbols.append(current_node.pipe_type)
    
    if current_node.pipe_type == '|':
        pipe_map[current_node.y][current_node.x] = 'V'
    else:
        pipe_map[current_node.y][current_node.x] = 'H'
    symbol_map[current_node.y][current_node.x] = current_node.pipe_type

    searching = True
    i = 0
    while searching and len(pipe_path) < 140*100:
        i += 1
        match current_node.pipe_type:
            case '|':
                if current_node.south:
                    next_node = find_compass_neighbour(current_node, map, 'north')
                    current_node.north = next_node
                    next_node.south = current_node
                else:
                    next_node = find_compass_neighbour(current_node, map, 'south')
                    current_node.south = next_node
                    next_node.north = current_node
            case '7':
                if current_node.south:
                    next_node = find_compass_neighbour(current_node, map, 'west')
                    current_node.west = next_node
                    next_node.east = current_node
                else:
                    next_node = find_compass_neighbour(current_node, map, 'south')
                    current_node.south = next_node
                    next_node.north = current_node
            case '-':
                if current_node.east:
                    next_node = find_compass_neighbour(current_node, map, 'west')
                    current_node.west = next_node
                    next_node.east = current_node
                else:
                    next_node = find_compass_neighbour(current_node, map, 'east')
                    current_node.east = next_node
                    next_node.west = current_node
            case 'J':
                if current_node.north:
                    next_node = find_compass_neighbour(current_node, map, 'west')
                    current_node.west = next_node
                    next_node.east = current_node
                else:
                    next_node = find_compass_neighbour(current_node, map, 'north')
                    current_node.north = next_node
                    next_node.south = current_node
            case 'F':
                if current_node.east:
                    next_node = find_compass_neighbour(current_node, map, 'south')
                    current_node.south = next_node
                    next_node.north = current_node
                else:
                    next_node = find_compass_neighbour(current_node, map, 'east')
                    current_node.east = next_node
                    next_node.west = current_node
            case 'L':
                if current_node.north:
                    next_node = find_compass_neighbour(current_node, map, 'east')
                    current_node.east = next_node
                    next_node.west = current_node
                else:
                    next_node = find_compass_neighbour(current_node, map, 'north')
                    current_node.north = next_node
                    next_node.south = current_node
        if next_node.pipe_type == 'S':
            print("Found S, stopping")
            if next_node.north and next_node.south:
                pipe_map[next_node.y][next_node.x] = 'V'
            searching = False
        else:
            pipe_path.append(next_node)
            path_symbols.append(next_node.pipe_type)
            current_node = next_node
            if current_node.pipe_type in ['|']:
                pipe_map[current_node.y][current_node.x] = 'V'
            else:
                pipe_map[current_node.y][current_node.x] = 'H'
            
            symbol_map[current_node.y][current_node.x] = current_node.pipe_type
        # print(f'current path {path_symbols}')

    print_map(symbol_map)
    print('starting pipe map')
    # print_map(pipe_map)
    # print('')

    # # for every row, eliminate leading
    # for y, row in enumerate(pipe_map):
    #     for x, col in enumerate(row):
    #         if pipe_map[y][x] == 0 or pipe_map[y][x] == 'B':
    #             pipe_map[y][x] = 'B'
    #         else:
    #             break

    # # for every row eliminate trailing 0s
    # for y, row in enumerate(pipe_map):
    #     for x in range(len(row)-1, -1, -1):
    #         if pipe_map[y][x] == 0 or pipe_map[y][x] == 'B':
    #             pipe_map[y][x] = 'B'
    #         else:
    #             break

    # # for every column, eliminate leading 0s
    # for x in range(0, len(pipe_map[0])):
    #     for y in range(0, len(pipe_map)):
    #         if pipe_map[y][x] == 0 or pipe_map[y][x] == 'B':
    #             pipe_map[y][x] = 'B'
    #         else:
    #             break

    # # for every column, eliminate trailing 0s
    # for x in range(0, len(pipe_map[0])):
    #     for y in range(len(pipe_map)-1, -1, -1):
    #         # print(f'checking (x,y) {x},{y} got {pipe_map[y][x]}')
    #         if pipe_map[y][x] == 0 or pipe_map[y][x] == 'B':
    #             pipe_map[y][x] = 'B'
    #         else:
    #             break

    # print('bounded pipe map')
    # print_map(pipe_map)
    # print('')

    # count enclosed
    enclosed = 0
    for y, row in enumerate(pipe_map):
        for x, col in enumerate(row):
            if col == 0:
                # shoot ray in x and count number of boundaries we hit. if odd we're enclosed
                count = 0
                in_h = False
                for ray in range(x, len(row)):
                    if pipe_map[y][ray] == 0:
                        if in_h:
                            count += 1
                            in_h = False
                    elif pipe_map[y][ray] == 'V':
                        if in_h:
                            count += 1
                            in_h = False
                        count += 1
                    elif pipe_map[y][ray] == 'H': # TODO this is too simple - have to take into account the different corner types
                        if in_h and symbol_map[y][ray] == 'L':
                            count += 1
                        in_h = True
                # if in_h:
                #     count +=1
                if count > 0 and count % 2 == 1:
                    enclosed += 1
                    # print(f'found enclosed at x {x} and y {y}')
                    symbol_map[y][x] = 'I'
                    pipe_map[y][x] = 'I'

    print('enclosed pipe map')
    print_map(pipe_map)

    print(f'final enclosed: {enclosed}')
        

# input = "10-test.input"
# input = "10-test1.input"
# input = "10-test2.input"
# input = "10-test3.input"

# first attempt 508, too low
# from cheating, answer is 576

input = "10.input"
star1(input)