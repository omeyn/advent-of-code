import os
import re

os.chdir('2024/3')

def star1(input_file):
    f = open(input_file, "r")

    sum = 0
    for line in f:
        sum += sum_for_section(line)

    print(sum)
        
def star2(input_file):
    f = open(input_file, "r")

    sum = 0
    do_count = 0
    dont_count = 0
    for line in f:
    #     # check_input(line)
    #     # print(f"raw line: {line}\n")
    #     dos = re.split(r"do\(\)", line)
    #     # print(f"do count: {len(dos)}")
    #     # for foo in dos:
    #     #     print(f"foo: {foo}\n\n")
    #     donts = re.split(r"don\'t\(\)", line)
    #     # print(f"dont count: {len(donts)}")

    #     do_count += len(dos)
    #     dont_count += len(donts)

    # print(f"do count: {do_count}")
    # print(f"dont count: {dont_count}")


        dont_pat = r"don\'t\(\)"
        do_pat = r"do\(\)"
        raw = re.split(do_pat, line)
        for section in raw:
            
            split_up = re.split(dont_pat, section)
            if len(split_up) > 2:
                print(f"BIG split_up: {split_up}\n")
                print(f"raw section {section}\n")
            do = split_up[0]
            # print(f"do section {do}")
            sum += sum_for_section(do)

    print(sum)

def sum_for_section(section):
    # print(section)
    sum = 0
    matches = re.findall(r"mul\(\d*,\d*\)", section)
    print(matches)
    for match in matches:
        a, b = map(int, match[4:-1].split(","))
        # print(f"multiplying {a} and {b}")
        sum += a * b

    return sum

# def check_input(line):
#     # print(f"raw line: {line}\n")
#     dos = re.split(r"do\(\)", line)
#     print(f"do count: {len(dos)}")
#     # for foo in dos:
#     #     print(f"foo: {foo}\n\n")
#     donts = re.split(r"don\'t\(\)", line)
#     print(f"dont count: {len(donts)}")


# input = "3-test.input"
input = "3.input"
# star1(input)
# 102631226 is too high
star2(input)


