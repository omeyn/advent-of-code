import os

os.chdir('2021/1')

def star1():
    f = open("1.input", "r")
    prev = None
    count = 0
    for line in f:
        num = int(line)
        if (prev):
            if (num - prev) > 0:
                count = count + 1
        prev = num

    print("Day 1 Star 1: " + str(count))

def star2():
    f = open("1.input", "r")
    count = 0
    nums = []
    for line in f:
        # print(line)
        nums.append(int(line))

    for i in range(len(nums)):
        if (i - 3 >= 0):
            sum_a = nums[i-1] + nums[i-2] + nums[i-3]
            sum_b = nums[i] + nums[i-1] + nums[i-2]
            # print(str(sum_a) + ' vs ' + str(sum_b))
            if (sum_b - sum_a > 0):
                # print('hit')
                count = count + 1

    print("Day 1 Star 2: " + str(count))

star1()
star2()