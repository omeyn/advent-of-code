import os

os.chdir('2021/2')

def star1():
    f = open("2.input", "r")
    h = 0
    d = 0
    for line in f:
        instr = line.split()
        if instr[0] == "down":
            d = d + int(instr[1])
        elif instr[0] == "up":
            d = d - int(instr[1])
        elif instr[0] == "forward":
            h = h + int(instr[1])
        # print("h: {}, d: {}".format(h, d))
    print("depth & horizontal = {}".format(h * d))

def star2():
    f = open("2.input", "r")
    h = 0
    d = 0
    aim = 0
    for line in f:
        instr = line.split()
        if instr[0] == "down":
            aim = aim + int(instr[1])
        elif instr[0] == "up":
            aim = aim - int(instr[1])
        elif instr[0] == "forward":
            h = h + int(instr[1])
            d = d + int(instr[1]) * aim
        print("h: {}, d: {}, aim: {}".format(h, d, aim))
    print("depth & horizontal = {}".format(h * d))


# star1()
star2()