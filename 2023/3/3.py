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
    sum = 0
    for line_num, line in enumerate(lines):
        print('')
        print(f'above: {lines[line_num-1]}')
        print(f'this : {line}')
        if line_num+1 < len(lines):
            print(f'below: {lines[line_num+1]}')

        for i, c in enumerate(line):
            if c in special_chars:
                
                print(f'found special char {c} at i {i}')
                above = find_num_near(lines[line_num-1], i)
                print(f'found number in line above {above}')
                this_line = find_num_near(line, i)
                print(f'found number in this line {this_line}')
                below = find_num_near(lines[line_num+1], i)
                print(f'found number in line below {below}')
                char_sum = above + this_line + below
                print(f'this char sum is {char_sum}')
                sum += char_sum
    
    print(f'final sum is {sum}')

# all nums btw 1 and 3 digits
def find_num_near(line, index):
    # print(f'checking char {line[index]} which is {index} in line {line} ')
    sum = 0
    if line[index].isdigit():
        sum = build_number_at(line, index)
    else:
        sum = 0
        if index-1 >= 0:
            if line[index-1].isdigit():
                sum += build_number_at(line, index-1)
        if index+1 < len(line):
            if line[index+1].isdigit():
                sum += build_number_at(line, index+1)
        
    return sum

def build_number_at(line, index):
    num_str = line[index]
    if index+1 < len(line):
        if line[index+1].isdigit():
            num_str += line[index+1]
            if index+2 < len(line):
                if line[index+2].isdigit():
                    num_str += line[index+2]
    if index-1 >= 0:
        if line[index-1].isdigit():
            num_str = line[index-1] + num_str
            if index-2 >= 0:
                if line[index-2].isdigit():
                    num_str = line[index-2] + num_str

    return int(num_str)

input = "3-test.input"
input = "3.input"
star1(input)
