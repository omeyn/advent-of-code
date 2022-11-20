def prep_nodes(map):
    all_nodes = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            all_nodes.append([x, y])
    return all_nodes

def prep_neighbors(node, all_nodes):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if neighbor in all_nodes:
            result.append(neighbor)
    return result

def prep(map):
    all_nodes = prep_nodes(map)
    for node in all_nodes:
        nbs = prep_neighbors(node, all_nodes)