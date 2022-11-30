from collections import Counter
import os
import copy
import math

os.chdir('2021/14')

# copied from reddit: https://www.reddit.com/r/adventofcode/comments/rfzq6f/comment/hoib78w/?utm_source=share&utm_medium=web2x&context=3

def read_puzzle(file):
  with open(file) as f:
    # the initial template is separated from the insertions by empty line
    template, insertions = f.read().split('\n\n')

    # a counter of our target string, the template
    chars = Counter(template)

    # redefine template as a counter of the starting pairs
    # zip for an example of "NNBC" produces: [('N', 'N'), ('N', 'B'), ('B', 'C')]
    # results in Counter({'NB': 1, 'NN': 1, 'BC': 1})
    template = Counter(a+b for a, b in zip(template, template[1:]))

    # parse the replacements
    insertions = {x[:2]: x[6] for x in insertions.split('\n')}
  return template, insertions, chars


def solve(old_temp, insertions, chars, steps):
  for _ in range(steps):
    new_temp = Counter()
    # for every letter pair in the existing Counter
    # fetch the replacement letter, pair it as a+insert and insert+b, give it the value in the old counter + 1
    # also update the count of the inserted char in the chars counter
    # what happens if there's no insertion for the a+b letter pair? -> I think it's safe to say that can't happen (doesn't happen in test input, appears to work in real input)
    for (a, b), value in old_temp.items():
    #   print(f"Checking letter pair {a}{b}")
      insert               = insertions[a+b]
    #   print(f"Got insertion {insert}")
      new_temp[a+insert]  += value
      new_temp[insert+b]  += value
      chars[insert]       += value
    old_temp = new_temp
  return max(chars.values()) - min(chars.values())

print(solve(*read_puzzle('14-test.input'), 1))
# print(solve(*read_puzzle('14.input'), 10))
# print(solve(*read_puzzle('14.input'), 40))
