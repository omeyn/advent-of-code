import os
import re
import copy

os.chdir('2024/6')

def star1(input_file):
    f = open(input_file, "r")
    maze = []
    for line in f:
        print(line.strip())
        maze.append(list(line.strip()))

    for i in range(len(maze)):
        # print(maze[i])
        for j in range(len(maze[0])):            
            if maze[i][j] == "^":
                start_i = i
                start_j = j
                print(f"found start at i: {i}, j: {j}")
                maze[i][j] = "V"
                break
    print()

    print(f"start_i: {start_i}, start_j: {start_j}")
    inside = True
    i = start_i
    j = start_j
    cardinal = "N"
    while inside:
        i, j, cardinal = take_step(i, j, maze, cardinal)
        if i >= 0 and i < len(maze) and j >= 0 and j < len(maze[0]):
            maze[i][j] = "V"
        else:
            inside = False
    
    steps = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):            
            if maze[i][j] == "V":
                steps += 1

    # 5210 too low (off by one), 5211 too low (forgot starting point)
    print(f"done with steps: {steps}")
    # pretty_print(maze)
        


def take_step(i, j, maze, cardinal):
    # print(f"taking step from i: {i}, j: {j}, cardinal: {cardinal}")
    new_i = i
    new_j = j
    if cardinal == "N":
        new_i -= 1
    elif cardinal == "S":
        new_i += 1
    elif cardinal == "E":
        new_j += 1
    elif cardinal == "W":
        new_j -= 1

    # print(f"checking new_i: {new_i}, new_j: {new_j}, which has value: {maze[new_i][new_j]}")

    if new_i >= 0 and new_i < len(maze) and new_j >= 0 and new_j < len(maze[0]):
        if maze[new_i][new_j] == "#" or maze[new_i][new_j] == "O":
            # i and j unchanged, cardinal changed, count unchanged
            # print(f"found #, turning to {turn(cardinal)}")
            # pretty_print(maze)
            return i, j, turn(cardinal)
        else:
            # new i and j, cardinal unchanged
            # print(f"found ., returning new_i: {new_i}, new_j: {new_j}")
            return new_i, new_j, cardinal
    else:
        # we're done
        return new_i, new_j, cardinal
    
def turn(cardinal):
    if cardinal == "N":
        return "E"
    elif cardinal == "E":
        return "S"
    elif cardinal == "S":
        return "W"
    elif cardinal == "W":
        return "N"

def pretty_print(maze):
    for row in maze:
        print("".join(row))


def star2(input_file):
    # brute force, try every ., run from start, and see if we get stuck
    f = open(input_file, "r")
    maze = []
    for line in f:
        print(line.strip())
        maze.append(list(line.strip()))

    for i in range(len(maze)):
        # print(maze[i])
        for j in range(len(maze[0])):            
            if maze[i][j] == "^":
                start_i = i
                start_j = j
                print(f"found start at i: {i}, j: {j}")
                maze[i][j] = "V"
                break
    print()

    block_count = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == ".":
                blocked_maze = copy.deepcopy(maze)
                blocked_maze[i][j] = "O"
                # print("new blocked maze")
                # pretty_print(blocked_maze)
                if is_walk_looped(start_i, start_j, blocked_maze):
                    block_count += 1
                # print("walked blocked maze")
                # pretty_print(blocked_maze)
                # print()

    print(f"block count: {block_count}")

def is_walk_looped(start_i, start_j, m):
    # print(f"new walk")
    inside = True
    i = start_i
    j = start_j
    cardinal = "N"
    step_count = 0
    looped = False
    while inside and not looped:
        i, j, cardinal = take_step(i, j, m, cardinal)
        step_count += 1
        # if step_count > 5211:
        if step_count > 10000:
            print(f"looped at step: {step_count}")
            # pretty_print(m)
            return True
            break
        if i >= 0 and i < len(m) and j >= 0 and j < len(m[0]):
            m[i][j] = "V"
        else:
            inside = False
    
    # print(f"done with steps: {step_count}")
    return False

input = "6-test.input"
input = "6.input"
# star1(input)
star2(input)