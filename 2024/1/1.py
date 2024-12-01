import os
import re

os.chdir('2024/1')

def star1(input_file):
    f = open(input_file, "r")

    a = []
    b = []
    for line in f:
        pair = line.strip().split(" ")
        a.append(int(pair[0]))
        b.append(int(pair[len(pair)-1]))
        # print(pair)
    
    a.sort()
    b.sort()
    big_diff = 0
    for i, x in enumerate(a):
        big_diff = big_diff + abs(x - b[i])

    print(big_diff)


def star2(input_file):
    f = open(input_file, "r")

    a = []
    b = []
    for line in f:
        pair = line.strip().split(" ")
        a.append(int(pair[0]))
        b.append(int(pair[len(pair)-1]))
        # print(pair)
    
    a.sort()
    b.sort()
    big_sum = 0
    for x in a:
        count = 0
        for y in b:
            if x == y:
                count += 1
        big_sum += count * x

    print(big_sum)    

input = "1-test.input"
input = "1.input"
star2(input)

