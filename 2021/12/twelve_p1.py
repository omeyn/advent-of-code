import os

os.chdir('2021/12')

# class Edge:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
    
#     def __str__(self):
#         return self.start + "->" + self.end

# def build_path(growing_path, edges):
#     # growing_path.append(edge)
#     if growing_path[-1] == "end":
#         print("got end, stopping")
#         return growing_path

#     for poss in edges:
#         print("got path {} checking edge {}".format(growing_path, poss))
#         if poss[0] == growing_path[-1]:
#             growing_path.append(poss[1])
#             print("building path, now at {}".format(growing_path))
#             return build_path(growing_path, edges)
    
#     return growing_path

def build_paths(paths, edges):
    got_more = True
    x = 0
    while got_more and x < 5:
        x += 1
        print("Got more, paths is {}".format(paths))
        new_paths = []
        pops = []
        for i in range(len(paths)):
            path = paths[i]
            print("CHECKING PATH {}".format(path))
            for edge in edges:
                # print("checking edge {}".format(edge))
                # print("comparing {} and {}".format(edge[0], path[-1]))
                if edge[0] == path[-1]:
                    new_path = [i for i in path]
                    new_path.append(edge[1])
                    new_paths.append(new_path)
                    # print("got match, new path is {}".format(path))
                    if edge[1] == "end":
                        got_more = False
                    else:
                        got_more = True

        paths = new_paths
    return paths



def star1(filename):
    nodes = set()
    edges = []
    f = open(filename, "r")
    for line in f:
        if line.startswith("#"):
            continue
        line = line.strip()
        raw_edge = line.split('-')
        nodes.add(raw_edge[0])
        nodes.add(raw_edge[1])
        edges.append((raw_edge[0], raw_edge[1]))
    
    print("")
    for node in nodes:
        print(node)
    print("")
    for edge in edges:
        print(edge)
    print("")
    paths = []
    for edge in edges:
        if edge[0] == "start":
            paths.append(list(edge))

    paths = build_paths(paths, edges)

    for path in paths:
        print("Got path:")
        print(path)
        
filename = "12.input"
filename = "12-test.input"
filename = "12-test2.input"
filename = "12-simple.input"
star1(filename)
#star2(filename)
