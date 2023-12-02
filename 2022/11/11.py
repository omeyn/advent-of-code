import os

os.chdir('2022/11')

class Monkey:
    def __init__(self, items):
        self.items = items

    def 
def star1(filename):
    f = open(filename, 'r')
    cycle = 1
    x = 1
    power_sum = 0
    for raw in f:
        line = raw.strip()
        if line.startswith('#'):
            continue
        parsed = line.split(" ")


filename = "11.input"
filename = "11-test.input"
star1(filename)
# star2(filename)