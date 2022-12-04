import os

os.chdir('2022/4')

def star1(filename):
    f = open(filename, "r")
    sum = 0
    for line in f:
        clean = line.strip()
        start1, end1 = clean.split(',')[0].split('-')
        start2, end2 = clean.split(',')[1].split('-')
        # print(f"{start1} {end1} {start2} {end2} for line {clean}")
        a = set(range(int(start1), int(end1)+1))
        b = set(range(int(start2), int(end2)+1))
        if a.issubset(b) or b.issubset(a):
            sum += 1
    print(f"star 1 sum {sum}")

def star2(filename):
    f = open(filename, "r")
    sum = 0
    for line in f:
        clean = line.strip()
        start1, end1 = clean.split(',')[0].split('-')
        start2, end2 = clean.split(',')[1].split('-')
        # print(f"{start1} {end1} {start2} {end2} for line {clean}")
        a = set(range(int(start1), int(end1)+1))
        b = set(range(int(start2), int(end2)+1))
        if len(a.intersection(b)) > 0:
            sum += 1
    print(f"star 1 sum {sum}")

filename = "4.input"
# filename = "4-test.input"
# star1(filename)
star2(filename)