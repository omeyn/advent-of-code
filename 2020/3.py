import os

os.chdir('2020')

def star1(filename):
    trees = []
    tree_template = []
    f = open(filename, "r")
    for line in f:
        clean = line.strip()
        row = [1 if x == '#' else 0 for x in clean]
        trees.append(row)
        tree_template.append(row)

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
        x += 3
        y += 1
    print(f"Got tree count {treecount}")

filename = "3.input"
# filename = "3-test.input"
star1(filename)
# star2(filename)