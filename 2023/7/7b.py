import os

os.chdir('2023/7')

def star1(input_file):
    f = open(input_file, "r")
    for line in f:
        print(line.strip())


input = "7-test.input"
input = "7.input"
star1(input)
