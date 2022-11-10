import os
from copy import deepcopy

os.chdir('2021/12')

class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = []
    
    def add_connection(self, id):
        self.connections.append(id)

    def __str__(self):
        return f"{self.name} connects to: {self.connections}"

def build_paths(paths, caves):
    new_paths = []
    for path in paths:
        if path[-1] == "end":
            new_paths.append(path)
        else:
            cave = caves.get(path[-1])
            for exit in cave.connections:
                if exit != "start":
                    new_path = deepcopy(path)
                    new_path.append(exit)
                    new_paths.append(new_path)

    return new_paths

def prune_paths(paths):
    new_paths = []
    for path in paths:
        good_path = True
        counts = {}
        for cave in path:
            if cave.islower():
                if cave in counts:
                    counts[cave] += 1
                else:
                    counts[cave] = 1
        for cave in counts:
            if counts[cave] > 1:
                good_path = False
        if (good_path):
            new_paths.append(path)
    
    return new_paths

def prune_paths_2(paths):
    new_paths = []
    for path in paths:
        good_path = True
        counts = {}
        for cave in path:
            if cave.islower():
                if cave in counts:
                    counts[cave] += 1
                else:
                    counts[cave] = 1

        got_double = False
        for cave in counts:
            if counts[cave] > 2:
                good_path = False
            elif counts[cave] == 2:
                if got_double:
                    good_path = False
                else:
                    got_double = True
                
        if (good_path):
            new_paths.append(path)
    
    return new_paths

# build all caves
# starting with cave 'start', build paths that go out one cave
# next iteration, build all the paths from going one cave more than previous step
# after an iteration, prune all paths that visit small cave more than once
# if all remaining paths end with cave 'end', we're done


def star1(filename):
    caves = {}
    f = open(filename, "r")
    for line in f:
        if line.startswith("#"):
            continue
        line = line.strip()
        raw_edge = line.split('-')
        if caves.get(raw_edge[0]):
            caves.get(raw_edge[0]).add_connection(raw_edge[1])
        else:
            cave = Cave(raw_edge[0])
            # print(f"making new cave {cave}")
            cave.add_connection(raw_edge[1])
            caves[raw_edge[0]] = cave
        if caves.get(raw_edge[1]):
            caves.get(raw_edge[1]).add_connection(raw_edge[0])
        else:
            cave = Cave(raw_edge[1])
            # print(f"making new cave {cave}")
            cave.add_connection(raw_edge[0])
            caves[raw_edge[1]] = cave

    start = caves.get('start')
    paths = []
    for exit in start.connections:
        path = ['start']
        path.append(exit)
        paths.append(path)

    # print(f"starting paths {paths}")
    done = False
    while not done:
        paths = build_paths(paths, caves)
        paths = prune_paths(paths)
        done = True
        for path in paths:
            if path[-1] != 'end':
                done = False


    # for path in paths:
        # print(f"Got path: {path}")
    print(f"Total path count is: {len(paths)}")

def star2(filename):
    caves = {}
    f = open(filename, "r")
    for line in f:
        if line.startswith("#"):
            continue
        line = line.strip()
        raw_edge = line.split('-')
        if caves.get(raw_edge[0]):
            caves.get(raw_edge[0]).add_connection(raw_edge[1])
        else:
            cave = Cave(raw_edge[0])
            # print(f"making new cave {cave}")
            cave.add_connection(raw_edge[1])
            caves[raw_edge[0]] = cave
        if caves.get(raw_edge[1]):
            caves.get(raw_edge[1]).add_connection(raw_edge[0])
        else:
            cave = Cave(raw_edge[1])
            # print(f"making new cave {cave}")
            cave.add_connection(raw_edge[0])
            caves[raw_edge[1]] = cave

    start = caves.get('start')
    paths = []
    for exit in start.connections:
        path = ['start']
        path.append(exit)
        paths.append(path)

    # print(f"starting paths {paths}")
    done = False
    while not done:
        paths = build_paths(paths, caves)
        paths = prune_paths_2(paths)
        done = True
        for path in paths:
            if path[-1] != 'end':
                done = False


    # for path in paths:
    #     print(f"Got path: {path}")
    print(f"Total path count is: {len(paths)}")

filename = "12.input"
# filename = "12-test.input"
# filename = "12-simple.input"
# star1(filename)
star2(filename)
