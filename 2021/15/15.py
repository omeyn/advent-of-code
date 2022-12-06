import os
import copy
import random

os.chdir('2021/15')

def is_legal(map, coord):
  return coord[0] >= 0 and coord[0] < len(map) and coord[1] >= 0 and coord[1] < len(map[0])

def extend_path(map, path):
  last_coord = path[-1]
  # print(last_coord)
  move_right = (last_coord[0], last_coord[1]+1)
  move_down = (last_coord[0]+1, last_coord[1])

  right_path = None
  if is_legal(map, move_right):
    right_path = copy.deepcopy(path)
    # right_path = path
    right_path.append(move_right)

  down_path = None
  if is_legal(map, move_down):
    down_path = copy.deepcopy(path)
    # down_path = path
    down_path.append(move_down)

  return (down_path, right_path)

def score_path(map, path):
  path_score = 0 - int(map[0][0])
  for coord in path:
    path_score += int(map[coord[0]][coord[1]])

  return path_score

def find_safest_path(map, paths):
  lowest_score = 100000000
  safest_path = []
  for path in paths:
    path_score = score_path(map, path)
    if path_score < lowest_score:
      lowest_score = path_score
      safest_path = path

  return (lowest_score, safest_path)

def build_random_path(map):
  path = []
  path.append((0,0))
  finished = False
  while not finished:
    options = extend_path(map, path)
    if options[0] == None and options[1] == None:
      finished = True
    elif options[0] == None:
      path = options[1]
    elif options[1] == None:
      path = options[0]
    else:
      path = options[random.randint(0,1)]
  
  return path

def build_feeler_paths(map):
  feelers = []
  for i in range(100):
    feelers.append(build_random_path(map))

  safest = find_safest_path(map, feelers)
  print(f"Lowest score is {safest[0]} in path {safest[1]}")
  return safest[0]

def prune_paths(map, paths, best_known_score):
  pruned = []
  for path in paths:
    score = score_path(map, path)
    if score < best_known_score and score < 5 * len(path):
      pruned.append(path)

  return pruned

def build_real_paths(map, best_known_score):
  best_local_score = best_known_score
  paths = []
  path = []
  path.append((0,0))
  paths.append(path)
  
  has_more = True
  while has_more:
    new_paths = []
    has_more = False
    for path in paths:
      if path[-1] == (len(map)-1, len(map[0])-1):
        # path is done
        # print(f"checked {path[-1]} against {len(map)-1} and {len(map[0])-1} and they are the same")
        score = score_path(map, path)
        if score < best_known_score:
          best_local_score = score
        new_paths.append(path)
      else:
        has_more = True
        extended = extend_path(map, path)
        if extended[0] != None:
          new_paths.append(extended[0])
        if extended[1] != None:
          new_paths.append(extended[1])
    
    # print(new_paths)
    # paths = copy.deepcopy(new_paths)
    print(f"Path count is {len(new_paths)}")
    pruned = prune_paths(map, new_paths, best_known_score)
    print(f"Pruned path count is {len(pruned)}")
    paths = pruned

  safest = find_safest_path(map, paths)
  print(f"Lowest score is {safest[0]} in path {safest[1]}")

def star1(filename):
  map = []
  f = open(filename, "r")
  for line in f:
      if line.startswith("#") or len(line.strip()) == 0:
          continue
      line = line.strip()
      map.append(line)

  best_known_score = build_feeler_paths(map)
  # best_known_score = 400
  print(f"Best score {best_known_score}")
  # build_real_paths(map, best_known_score)

filename = "15.input"
filename = "15-test.input"
# filename = "15-simple.input"
star1(filename)