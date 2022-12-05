import os

os.chdir('5')

def get_letter_at(line, pos):
    if len(line) > pos:
        # print(f"checking line {line} at pos {pos}")
        return line[pos]

    return None

def star1(filename):
    stacks = [list() for x in range(9)]
    print(f"stacks {stacks}")
    f = open(filename, "r")
    mode = 'setup'
    for line in f:
        if mode == 'setup':
            for i in range(1, 34, 4):
                box = line[i] if len(line) > i else None
                # print(f"got box {box} for pos {i} in line {line}")
                if box is not None and len(box.strip()) > 0:
                    if box.isupper():
                        index = (i - 1) // 4
                        stacks[index].insert(0, box)
                    else:
                        mode = 'instructions'
        else:
            if 'move' in line:
                print(f"doing move {line}")
                move = int(line.split(' ')[1])
                fr = int(line.split(' ')[3])-1
                to = int(line.split(' ')[5])-1
                for i in range(move):
                    box = stacks[fr].pop()
                    print(f"moving box {box}")
                    stacks[to].append(box)

    # print(f"stacks {stacks}")
    result = ''.join([x.pop() for x in stacks if len(x) > 0])
    print(f"final string {result}")

def star2(filename):
    stacks = [list() for x in range(9)]
    print(f"stacks {stacks}")
    f = open(filename, "r")
    mode = 'setup'
    for line in f:
        if mode == 'setup':
            for i in range(1, 34, 4):
                box = line[i] if len(line) > i else None
                # print(f"got box {box} for pos {i} in line {line}")
                if box is not None and len(box.strip()) > 0:
                    if box.isupper():
                        index = (i - 1) // 4
                        stacks[index].insert(0, box)
                    else:
                        mode = 'instructions'
        else:
            if 'move' in line:
                print(f"doing move {line}")
                move = int(line.split(' ')[1])
                fr = int(line.split(' ')[3])-1
                to = int(line.split(' ')[5])-1
                pile = []
                for i in range(move):
                    box = stacks[fr].pop()
                    pile.insert(0, box)
                    print(f"moving box {box}")
                stacks[to] = stacks[to] + pile

    print(f"stacks {stacks}")
    result = ''.join([x.pop() for x in stacks if len(x) > 0])
    print(f"final string {result}")

filename = "5.input"
# filename = "5-test.input"
# star1(filename)
star2(filename)