import os

os.chdir('2023/5')

def star1(input_file):
    f = open(input_file, "r")
    for line in f:
        print(line)


input = "5-test.input"
# input = "5.input"
star1(input)