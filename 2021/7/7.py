import os

os.chdir('2021/7')

def star1():
    f = open("7.input", "r")
    # f = open("7-test.input", "r")
    crabs = [int(x) for x in f.readline().split(',')]
    max_h = max(crabs)
    min_h = min(crabs)
    min_cost = 1000000
    best_pos = -1
    # print(min_h, max_h)
    for diff in range(max_h - min_h + 1):
        pos = min_h + diff
        print("testing pos {}".format(pos))
        cost = 0
        for crab in crabs:
            cost += abs(crab - pos)
        # print("cost {}".format(cost))
        if cost < min_cost:
            # print("updating min_cost")
            min_cost = cost
            best_pos = pos

    print("best pos {} for cost {}".format(best_pos, min_cost))

def star2():
    f = open("7.input", "r")
    # f = open("7-test.input", "r")
    crabs = [int(x) for x in f.readline().split(',')]
    max_h = max(crabs)
    min_h = min(crabs)
    min_cost = 100000000000
    best_pos = -1
    # print(min_h, max_h)
    for diff in range(max_h - min_h + 1):
        pos = min_h + diff
        print("testing pos {}".format(pos))
        cost = 0
        for crab in crabs:
            # sum of ints proof gives s = n(n+1)/2
            n = abs(crab - pos)
            incr_cost = (n * (n+1))/2
            cost += incr_cost
        # print("cost {}".format(cost))
        if cost < min_cost:
            # print("updating min_cost")
            min_cost = cost
            best_pos = pos

    print("best pos {} for cost {}".format(best_pos, min_cost)) 

# star1()
star2()


# 1 = 1
# 2 = 3
# 3 = 6
# 4 = 10
# 5 = 15
# 6 = 21