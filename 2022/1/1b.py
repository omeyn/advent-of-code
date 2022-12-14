# using tips from Jordan

from aocd import lines, submit
import heapq 

def elves(lines):
    s = 0
    for l in lines:
        if len(l) == 0:
            yield s
            s = 0
        else:
            s += int(l)

m = max(elves(lines))
three = sum(heapq.nlargest(3, elves(lines)))

submit(m, part="a", day=1, year=2022)
# submit(three, part="b", day=1, year=2022)
