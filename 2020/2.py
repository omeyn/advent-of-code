import os

os.chdir('2020')

def star1(filename):
    valid = 0
    f = open(filename, "r")
    for line in f:
        clean = line.strip()
        instr = clean.split(" ")
        min_count = int(instr[0].split('-')[0])
        max_count = int(instr[0].split('-')[1])
        letter = instr[1][0]
        password = instr[2]
        print(f"got min {min_count} max {max_count} letter {letter} password {password}")
        count = password.count(letter)
        if count >= min_count and count <= max_count:
            valid += 1

    print(f"got {valid} valid passwords")

def star2(filename):
    valid = 0
    f = open(filename, "r")
    for line in f:
        clean = line.strip()
        instr = clean.split(" ")
        first_pos = int(instr[0].split('-')[0])-1
        second_pos = int(instr[0].split('-')[1])-1
        letter = instr[1][0]
        password = instr[2]
        print(f"checking that {password} contains {letter} at one of {first_pos} and {second_pos}")
        if (password[first_pos] == letter and password[second_pos] != letter) or (password[first_pos] != letter and password[second_pos] == letter):
            print(f"line {clean} looks good")
            valid += 1

    print(f"got {valid} valid passwords")


filename = "2.input"
# filename = "2-test.input"
# star1(filename)
star2(filename)