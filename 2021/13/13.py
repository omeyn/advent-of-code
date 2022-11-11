import os

os.chdir('2021/13')

def draw_dots(coords, max_x, max_y):
    # print(f"drawing dots for max x {max_x} max y {max_y}")
    map = [[0 for y in range(int(max_y+1))] for x in range(int(max_x+1))]
    for coord in coords:
        # print(f"drawing coord {coord[0]} {coord[1]}")
        map[int(coord[0])][int(coord[1])] = 1
    return map

def fold_map(map, axis, index):
    print(f"Folding on axis {axis} at pos {index}")
    if axis == 'x':
        max_x = int(index)
        max_y = len(map[0])
        new_map = [[0 for y in range(int(max_y))] for x in range(int(max_x))]
        for x in range(max_x):
            for y in range(max_y):
                # print(f"mapping x {x} y {y}")
                new_map[x][y] = new_map[x][y] + map[x][y]
                diff = max_x - x
                new_map[x][y] = new_map[x][y] + map[max_x+diff][y]
    elif axis == 'y':
        max_x = len(map)
        max_y = int(index)
        new_map = [[0 for y in range(int(max_y))] for x in range(int(max_x))]
        for x in range(max_x):
            for y in range(max_y):
                # print(f"mapping x {x} y {y}")
                new_map[x][y] = new_map[x][y] + map[x][y]
                diff = max_y - y
                new_map[x][y] = new_map[x][y] + map[x][max_y+diff]

    # print(f"old map {map}")
    # print(f"new map {new_map}")
    return new_map

def star1(filename):
    coords = []
    folds = []
    max_x = 0
    max_y = 0
    f = open(filename, "r")
    for line in f:
        if line.startswith("#") or len(line.strip()) == 0:
            continue
        line = line.strip()
        if "=" in line:
            raw_fold = line.split('=')
            if raw_fold[0].endswith('x'):
                folds.append(['x', raw_fold[1]])
            else:
                folds.append(['y', raw_fold[1]])
        else:
            coord = line.split(',')
            if int(coord[0]) > max_x:
                max_x = int(coord[0])
            if int(coord[1]) > max_y:
                max_y = int(coord[1])
            coords.append(coord)
    
    # print(f"got coords {coords}")
    # print(f"got folds {folds}")

    map = draw_dots(coords, max_x, max_y)
    # print(f"built map {map}")

    part1_result(map, folds)
    part2_result(map, folds)


def part1_result(map, folds):
    map = fold_map(map, folds[0][0], folds[0][1])

    count = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] > 0:
                count += 1
    print(f"Map count {count}")

def part2_result(map, folds):
    for fold in folds:
        map = fold_map(map, fold[0], fold[1])

    for x in range(len(map)):
        line = ""
        for y in range(len(map[0])):
            if map[x][y] > 0:
                line = line + "#"
            else:
                line = line + " "
        print(line)
        #RKHFZGUB


filename = "13.input"
# filename = "13-test.input"
# filename = "13-simple.input"
star1(filename)
