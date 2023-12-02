import os
import re

os.chdir('2023/1')

def star1(input_file):
    f = open(input_file, "r")

    pattern = '/\D+'

    sum = 0
    for line in f:
        print(line)
        ready = False
        digits = 0
        offset = 3
        while not ready:
            foo = find_num(line[0:offset])
            if foo != None:
                digits = 10*foo
                ready = True
            offset += 1

        offset = 1
        ready = False
        while not ready:
            foo = find_num(line[-offset:len(line)])
            if foo != None:
                digits += foo
                ready = True
            offset += 1
        print(digits)
        sum += digits

    print(sum)

def find_num(line):
    print(f"checking line {line}")
    line = sub_words(line)
    if bool(re.search(r'\d', line)):
        nums = re.sub('\D', '', line)
        return int(nums[0])
    
    return None


def sub_words(line):
    line = re.sub('one', '1', line)
    line = re.sub('two', '2', line)
    line = re.sub('three', '3', line)
    line = re.sub('four', '4', line)
    line = re.sub('five', '5', line)
    line = re.sub('six', '6', line)
    line = re.sub('seven', '7', line)
    line = re.sub('eight', '8', line)
    line = re.sub('nine', '9', line)
    return line

input = "1-test.input"
input = "1b-test.input"
input = "1.input"
star1(input)
