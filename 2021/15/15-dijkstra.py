import os
import copy
import random

os.chdir('2021/15')


# dijkstra in python stolen from https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php#:~:text=Dijkstra's%20algorithm%20is%20an%20iterative,variable%20in%20the%20Vertex%20class.

import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def __lt__(self, other):
        return self.distance < other.distance

    def __le__(self, other):
        return self.distance <= other.distance

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    # ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

def cost_of_shortest(path, map):
    cost = 0
    for i in range(1, len(path)-1):
        y = int(path[i].split(',')[0])
        x = int(path[i].split(',')[1])
        # print(f"{path[i]} cost is {map[y][x]}")
        cost += int(map[y][x])
    return cost

import heapq

def dijkstra(aGraph, start, target):
    print('''Dijkstra's shortest path''')
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # print(f"checking next: [{next}] but has it been visited? {next.visited}")
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            # print(f"new dist {new_dist} and next.get_distance {next.get_distance()}")
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                # print('updated : current = %s next = %s new_dist = %s' %(current.get_id(), next.get_id(), next.get_distance()))
            # else:
                # print('not updated : current = %s next = %s new_dist = %s' %(current.get_id(), next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

def star1(filename):
    map = []
    f = open(filename, "r")
    for line in f:
        if line.startswith("#") or len(line.strip()) == 0:
            continue
        line = line.strip()
        map.append(line)

    g = Graph()

    for y in range(len(map)):
        for x in range(len(map[0])):
            g.add_vertex(f"{y},{x}")

    for y in range(len(map)):
        for x in range(len(map[0])):
            if (y-1) >= 0:
                g.add_edge(f"{y},{x}", f"{y-1},{x}", int(map[y-1][x]))
            if (y+1) < len(map):
                g.add_edge(f"{y},{x}", f"{y+1},{x}", int(map[y+1][x]))
            if (x-1) >= 0:
                g.add_edge(f"{y},{x}", f"{y},{x-1}", int(map[y][x-1]))
            if (x+1) < len(map[0]):
                g.add_edge(f"{y},{x}", f"{y},{x+1}", int(map[y][x+1]))

    # g.add_vertex('a')
    # g.add_vertex('b')
    # g.add_vertex('c')
    # g.add_vertex('d')
    # g.add_vertex('e')
    # g.add_vertex('f')

    # g.add_edge('a', 'b', 7)  
    # g.add_edge('a', 'c', 9)
    # g.add_edge('a', 'f', 14)
    # g.add_edge('b', 'c', 10)
    # g.add_edge('b', 'd', 15)
    # g.add_edge('c', 'd', 11)
    # g.add_edge('c', 'f', 2)
    # g.add_edge('d', 'e', 6)
    # g.add_edge('e', 'f', 9)

    print('Graph data:')
    for v in g:
        print(f"Got v {v}")
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('(%s, %s, %3d)'  % (vid, wid, v.get_weight(w)))

    final_v = '2,2'
    final_v = '9,9'
    final_v = '99,99'
    # dijkstra(g, g.get_vertex('a'), g.get_vertex('e')) 
    dijkstra(g, g.get_vertex('0,0'), g.get_vertex(final_v)) 

    # target = g.get_vertex('e')
    target = g.get_vertex(final_v)
    path = [target.get_id()]
    shortest(target, path)
    print('The shortest path : %s' %(path[::-1]))
    forward_path = path[::-1]
    forward_path.append(g.get_vertex(final_v))
    print(f"The cost of shortest is {cost_of_shortest(forward_path, map)}")

filename = "15.input"
# filename = "15-test.input"
# filename = "15-simple.input"
star1(filename)