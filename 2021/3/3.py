import os

os.chdir('2021/3')

def star1():
    f = open("3.input", "r")
    total_readings = 0
    on_bits = []
    for line in f:
        if len(on_bits) == 0:
            on_bits = [0 for q in range(len(line)-1)]
        total_readings = total_readings + 1
        for i in range(len(line)):
            digit = line[i]
            if digit == "1":
                on_bits[i] = on_bits[i] + 1
    
    print("on bits {}".format(on_bits))
    gamma = ""
    epsilon = ""
    for sum in on_bits:
        if (sum > (total_readings/2)):
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
    print("epsilon: {} as bin {} gamma: {} as bin {}".format(epsilon, int(epsilon, 2), gamma, int(gamma, 2)))
    print("Product of epsilon and gamma: {}".format(int(epsilon, 2) * int(gamma, 2)))

def star2():
    f = open("3.input", "r")
    total_readings = 0
    lines = []
    for line in f:
        lines.append(line.strip())
    
    filtered_lines = lines
    for i in range(len(lines[0])):
        filtered_lines = filter_lines(filtered_lines, i, "most")
        if len(filtered_lines) == 1:
            break
    oxygen = filtered_lines[0]

    filtered_lines = lines
    for i in range(len(lines[0])):
        filtered_lines = filter_lines(filtered_lines, i, "least")
        if len(filtered_lines) == 1:
            break
    c02 = filtered_lines[0]

    print("co2 * oxygen is: {}".format(int(oxygen, 2) * int(c02, 2)))

def filter_lines(lines, position, most_or_least):
    on_bits = 0
    for line in lines:
        if line[position] == "1":
            on_bits = on_bits + 1
    if on_bits >= len(lines)/2:
        most_common = "1"
        least_common = "0"
    else:
        most_common = "0"
        least_common = "1"

    if most_or_least == "most":
        target_bit = most_common
    else:
        target_bit = least_common

    return [line for line in lines if line[position] == target_bit]


# star1()
star2()