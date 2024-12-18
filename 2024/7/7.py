import os
import itertools

os.chdir('2024/7')

def star1(input_file):
    f = open(input_file, "r")
    calibration = 0
    for line in f:
        print(line.strip())
        raw = line.split(":")
        target = int(raw[0].strip())
        numbers = [int(x) for x in raw[1].strip().split(" ")]
        print(f"target: {target} numbers: {numbers}")
        
        # tuple of all possible operations
        ops = gen_ops(len(numbers))
        for op in ops:
            result = eval_ops(op, numbers)
            if result == target:
                print(f"found: {target} with {op}")
                calibration += result
                break
        
    print(f"star 1 calibration: {calibration}")

def eval_ops(ops, numbers):
    result = 0
    for i, op in enumerate(ops):
        if op == "a":
            result += numbers[i]
        elif op == "m":
            result *= numbers[i]
    return result

def gen_ops(count):
    ops = itertools.product('am', repeat=count)
    return ops

def star2(input_file):
    f = open(input_file, "r")
    calibration = 0
    for line in f:
        print(line.strip())
        raw = line.split(":")
        target = int(raw[0].strip())
        numbers = [int(x) for x in raw[1].strip().split(" ")]
        # print(f"target: {target} numbers: {numbers}")
        
        # tuple of all possible operations
        ops = gen_ops2(len(numbers)-1)
        for op in ops:
            result = eval_ops2(op, numbers)
            if result == target:
                print(f"found: {target} with {op}")
                calibration += result
                break
        
    print(f"star 2 calibration: {calibration}")

def eval_ops2(ops, numbers):
    result = numbers[0]
    for i, op in enumerate(ops):
        if op == "a":
            result += numbers[i+1]
        elif op == "m":
            result *= numbers[i+1]
        elif op == "p":
            result = int(str(result) + str(numbers[i+1]))
    return result

def gen_ops2(count):
    ops = itertools.product('amp', repeat=count)
    return ops


# foo = gen_ops2(2)
# for f in foo:
#     print(f)


input = "7-test.input"
input = "7.input"

# 2654749936343 answer for star1
# star1(input)

# 124060392153764 too high for star2
# 124060392153684
# 795746075 too low for star2
star2(input)