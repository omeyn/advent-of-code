import os
import re

os.chdir('2024/2')

def star1(input_file):
    f = open(input_file, "r")

    safe_count = 0
    for line in f:
        levels = [int(x) for x in line.strip().split(" ")]
        orig = levels
        if levels[0]-levels[1] < 0:
            # increasing, boo
            levels.reverse()
        safe = True
        for i in range(len(levels)-1):
            diff = levels[i] - levels[i+1]
            safe = safe and diff >=1  and diff <= 3

        if safe:
            print(f"declared safe: \n{orig} \nevaluated as \n{levels}")
            safe_count += 1

    print(f"safe count {safe_count}")



def star2(input_file):
    f = open(input_file, "r")

    safe_count = 0
    for line in f:
        levels = [int(x) for x in line.strip().split(" ")]
        safe = check_levels(levels)
        if not safe:
            print(f"first pass of {levels} failed")
            for i in range(len(levels)):
                sub = levels.copy()
                sub.pop(i)
                print(f"checking {sub}")
                safe = check_levels(sub)
                if safe:
                    print(f"found safe {sub}")
                    break

        if not safe:
            print(f"{safe} : {levels}")
        if safe:
            safe_count += 1

    print(f"safe count {safe_count}")


# def check_levels(levels):
#     orig = levels
#     if levels[0]-levels[1] < 0:
#         # increasing, boo
#         levels.reverse()
#     safe = True
#     for i in range(len(levels)-1):
#         diff = levels[i] - levels[i+1]
#         safe = safe and diff >=1  and diff <= 3
    
#     return safe

def check_levels(levels):
    if levels[0] - levels[1] > 0:
        #decreasing
        idx = range(len(levels)-1)
        for i in idx:
            # print(f"checking index {i} minus {i+1} so {levels[i]}-{levels[i+1]}")
            diff = levels[i] - levels[i+1]
            if diff < 0 or abs(diff) < 1 or abs(diff) > 3:
                print(f"dec bad diff {diff} at index {i}, {i+1} in {levels}")
                return False
    else:
        #increasing
        idx = list(range(len(levels)))
        idx.reverse()
        for i in idx:
            # print(f"checking index {i-1} minus {i} so {levels[i-1]}-{levels[i]}")
            if i > 0:
                diff = levels[i-1] - levels[i]
                if diff > 0 or abs(diff) < 1 or abs(diff) > 3:
                    print(f"inc bad diff {diff} at index {i-1}, {i} in {levels}")
                    return False
    
    return True


input = "2-test.input"
input = "2.input"
# star1(input)
star2(input)

