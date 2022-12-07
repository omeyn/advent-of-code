import os

os.chdir('2022/7')

class Dir:
  def __init__(self, name, parent, size):
    self.name = name
    self.parent = parent
    self.size = 0
    self.children = []
  
  def add_child(self, dir):
    self.children.append(dir)

  def add_size(self, moar):
    self.size += moar

def build_sums(dir):
  sum = dir.size
  if len(dir.children) == 0:
    return sum

  for child in dir.children:
    sum += build_sums(child)

  return sum

def build_tree(root_dir, all_dirs, f):
  current_dir = root_dir
  for raw in f:
      line = raw.strip()
      if line.startswith('$ cd'):
          fields = line.split(' ')
          if fields[2] == '..': # cd up one level
              current_dir = current_dir.parent
          else:
              # cd into dir
              new_dir = Dir(fields[2], current_dir, 0)
              all_dirs.append(new_dir)
              current_dir.add_child(new_dir)
              current_dir = new_dir
      elif line == ('$ ls'):
          continue
      else:
          fields = line.split(' ')
          if fields[0] == 'dir':
              continue
          else:
              # print(f"adding size {fields[0]} to current dir {current_dir.name}")
              current_dir.add_size(int(fields[0]))

def star1(filename):
  f = open(filename, 'r')
  f.readline()
  root = Dir('root', None, 0)
  all_dirs = []
  build_tree(root, all_dirs, f)

  small_sums = 0    
  for dir in all_dirs:
    sum = build_sums(dir)
    if sum <= 100000:
      small_sums += sum
      # print(f"for dir {dir.name} got sum {sum}")

  print(f"star 1 sum {small_sums}")

def star2(filename):
  f = open(filename, 'r')
  f.readline()
  root = Dir('root', None, 0)
  all_dirs = []
  build_tree(root, all_dirs, f)

  root_sum = build_sums(root)
  target_space = 30000000 - (70000000 - build_sums(root))
  print(f"root size {root_sum} target {target_space}")
  
  smallest_big_dir = root
  smallest_big_sum = root_sum

  for dir in all_dirs:
    sum = build_sums(dir)  
    if sum >= target_space:
      print(f"checking dir {dir.name} with sum {sum}")
      if sum >= target_space and sum < smallest_big_sum:
        print(f"hit, new leader is {dir.name}")
        smallest_big_dir = dir
        smallest_big_sum = sum

  print(f"star 2 dir choice: {smallest_big_sum}")


filename = "7.input"
# filename = "7-test2.input"
# filename = "7-test.input"
# star1(filename)
star2(filename)