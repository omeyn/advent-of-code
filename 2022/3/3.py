import os

os.chdir('2022/3')

# A = 65
# Z = 90
# a = 97
# z = 122

def common_letter(line):
    first_half  = line[:len(line)//2]
    second_half = line[len(line)//2:]
    for letter in first_half:
        if letter in second_half:
            return letter
    
    return None

def letter_value(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26

def common_among_three(lines):
    for letter in lines[0]:
        if letter in lines[1] and letter in lines[2]:
            return letter
    return None

def star1(filename):
    f = open(filename, "r")
    sum = 0
    for line in f:
        clean = line.strip()
        # print(f"common {common_letter(clean)} worth {letter_value(common_letter(clean))} in {clean}")
        sum += letter_value(common_letter(clean))
    print(f"star 1 sum is {sum}")

def star2(filename):
    sums = []
    f = open(filename, "r")
    sum = 0
    lines = []
    for line in f:
        clean = line.strip()
        lines.append(clean)
        if len(lines) == 3:
            sum += letter_value(common_among_three(lines))
            lines = []
    print(f"star 2 sum is {sum}")


filename = "3.input"
# filename = "3-test.input"
# star1(filename)
star2(filename)