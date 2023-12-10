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
        
def star1(input_file):
    f = open(input_file, "r")
    map = []
    for line in f:
        print(line.strip())
        map.append(line.strip())
        if 'S' in line:
            starting_node = PipeNode('S', y=len(map)-1, x=line.find('S'))
            print(f'found S at 0-based {starting_node.x},{starting_node.y}, proof {map[starting_node.y][starting_node.x]}')

    pipe_path = [starting_node]

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
            searching = False
        else:
            pipe_path.append(next_node)
            path_symbols.append(next_node.pipe_type)
            current_node = next_node
        # print(f'current path {path_symbols}')

    print(f'current path {path_symbols}')
    print(f'finished with pipe length {len(pipe_path)}')
    cost = len(pipe_path)/2
    print(f'highest cost is {cost}')
        

# input = "10-test.input"
# input = "10-test2.input"
input = "10.input"
star1(input)