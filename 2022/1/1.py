import os

os.chdir('1')

def star1():
    sums = []
    f = open("1.input", "r")
    sum = 0
    for line in f:
        if line.strip() == '':
            sums.append(sum)
            sum = 0
        else:
            sum += int(line.strip())

    print(f"Single max: {max(sums)}")

    sums.sort()
    print(f"Sorted sums {sums}")
    top3 = sums[-1] + sums[-2] + sums[-3]
    print(f"Top 3 summed {top3}")


star1()
