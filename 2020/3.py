import os

os.chdir('2020')

def find_slope(trees, delta_x, delta_y):
    print(trees)
    # goal is reach y = len(trees)-1
    x = 0
    y = 0
    treecount = 0
    while y < len(trees):
        if x >= len(trees[0]):
            trees = [row + row for row in trees]
            print(f"new trees after growth {trees}")
        print(f"checking y {y} x {x}")
        print(f"current tree shape is y {len(trees)} x {len(trees[0])}")
        treecount += trees[y][x]
        x += delta_x
        y += delta_y
    print(f"Got tree count {treecount}")
    return treecount

def star1(filename):
    trees = []
    tree_template = []
    f = open(filename, "r")
    for line in f:
        clean = line.strip()
        row = [1 if x == '#' else 0 for x in clean]
        trees.append(row)
        tree_template.append(row)

    tree_product = 1
    tree_product *= find_slope(trees, 1, 1)
    tree_product *= find_slope(trees, 3, 1)
    tree_product *= find_slope(trees, 5, 1)
    tree_product *= find_slope(trees, 7, 1)
    tree_product *= find_slope(trees, 1, 2)
    print(f"tree product {tree_product}")


filename = "3.input"
# filename = "3-test.input"
star1(filename)
# star2(filename)