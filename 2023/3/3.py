import os
import re

os.chdir('2023/3')

def star1(input_file):
    f = open(input_file, "r")

    special_chars = '!@#$%^&*()_+-=/'
    lines = []
    for line in f:
        # print(line)
        lines.append(line.strip())

    # print(lines)
    for line in lines:
        print(line)
        for i, c in enumerate(line):
            if c in special_chars:
                print(f'found special char {c} at i {i}')


input = "3-test.input"
input = "3.input"
star1(input)
