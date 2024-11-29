import os
import re

os.chdir('2024/1')

def star1(input_file):
    f = open(input_file, "r")

    for line in f:
        print(line)

input = "1-test.input"
input = "1.input"
star1(input)
