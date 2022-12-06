import os

os.chdir('6')

def star1(filename):
    f = open(filename, "r")
    line = f.readline()
    for i in range(len(line)):
        print(f"{line[i:i+4]}")
        if len(set(line[i:i+4])) == 4:
            print(f"First marker {line[i:i+4]} after {i+4}")
            break

def star2(filename):
    f = open(filename, "r")
    line = f.readline()
    for i in range(len(line)):
        # print(f"{line[i:i+14]}")
        if len(set(line[i:i+14])) == 14:
            print(f"First marker {line[i:i+14]} after {i+14}")
            break

filename = "6.input"
# filename = "6-test.input"
# star1(filename)
star2(filename)