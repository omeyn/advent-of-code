import os

os.chdir('2022/8')

def pretty_print_grid(grid):
    for y in range(len(grid)):
        print(''.join([str(x) for x in grid[y]]))

def build_visible(forest):
    visible_trees = [[0 for x in range(len(forest[0]))] for y in range(len(forest))]
    for y in range(len(visible_trees)):
        for x in range(len(visible_trees[0])):
            if x == 0 or x == len(visible_trees[0])-1 or y == 0 or y == len(visible_trees)-1:
                visible_trees[y][x] = 1
    return visible_trees

def check_visible(forest):
    visible_trees = build_visible(forest)
    for y in range(1, len(forest)-1):
        # check row left to right
        highest_left = int(forest[y][0])
        for x in range(1, len(forest[y])-1):
            if int(forest[y][x]) > highest_left:
                visible_trees[y][x] = 1
                highest_left = int(forest[y][x])
        # check row right to left
        highest_right = int(forest[y][-1])
        # print(f"checking row {y}")
        for x in range(len(forest[y])-1, 0, -1):
            if int(forest[y][x]) > highest_right:
                # print(f"x {x} y {y} value {forest[y][x]} is higher than {highest_right}")
                visible_trees[y][x] = 1
                highest_right = int(forest[y][x])

    for x in range(1, len(forest[0])-1):
        # check col top down
        highest_top = int(forest[0][x])
        for y in range(1, len(forest)-1):
            if int(forest[y][x]) > highest_top:
                visible_trees[y][x] = 1
                highest_top = int(forest[y][x])
        # check col bottom up
        highest_bottom = int(forest[-1][x])
        for y in range(len(forest)-1, 0, -1):
            if int(forest[y][x]) > highest_bottom:
                visible_trees[y][x] = 1
                highest_bottom = int(forest[y][x])

    # pretty_print_grid(forest)
    # print('')
    # pretty_print_grid(visible_trees)
    visible_count = sum([sum(x) for x in visible_trees])
    return visible_count

def check_scenic_tree(tree_x, tree_y, forest):
    if tree_x == 0 or tree_x == len(forest[0])-1 or tree_y == 0 or tree_y == len(forest)-1:
        # print(f"tree at y {tree_y} and x {tree_x} has scenic product 0")
        return 0

    tree_height = forest[tree_y][tree_x]
    scenic_product = 1
    scenic_count = 0
    # check up
    for y in range(tree_y-1, -1, -1):
        if forest[y][tree_x] < tree_height:
            scenic_count += 1
        else:
            scenic_count += 1
            break
    # print(f"count up {scenic_count}")
    scenic_product *= scenic_count
    scenic_count = 0
    # check down
    for y in range(tree_y+1, len(forest), 1):
        if forest[y][tree_x] < tree_height:
            scenic_count += 1
        else:
            scenic_count += 1
            break
        # print(f"count down {scenic_count}")
    scenic_product *= scenic_count
    scenic_count = 0
    # check right
    for x in range(tree_x+1, len(forest[0]), 1):
        if forest[tree_y][x] < tree_height:
            scenic_count += 1
        else:
            scenic_count += 1
            break
    # print(f"count right {scenic_count}")
    scenic_product *= scenic_count
    scenic_count = 0
    # check left
    for x in range(tree_x-1, -1, -1):
        if forest[tree_y][x] < tree_height:
            scenic_count += 1
        else:
            scenic_count += 1
            break
    # print(f"count left {scenic_count}")
    scenic_product *= scenic_count

    # print(f"tree at y {tree_y} and x {tree_x} is height {tree_height} and has scenic product {scenic_product}")
    return scenic_product

def check_scenic(forest):
    top_score = 0
    for y in range(len(forest)):
        for x in range(len(forest[0])):
            scenic_count = check_scenic_tree(x, y, forest)
            if scenic_count > top_score:
                top_score = scenic_count
    
    return top_score

def star1(filename):
    f = open(filename, 'r')
    forest = []
    for raw in f:
        line = raw.strip()
        forest.append(list(line))

    visible = check_visible(forest)
    print(f"star 1 visible trees: {visible}")

def star2(filename):
    f = open(filename, 'r')
    forest = []
    for raw in f:
        line = raw.strip()
        forest.append(list(line))

    # pretty_print_grid(forest)
    top_score = check_scenic(forest)
    # top_score = check_scenic_tree(2,3,forest)
    print(f"star 2 scenic optimum: {top_score}")

filename = "8.input"
# filename = "8-test.input"
# star1(filename)
star2(filename)