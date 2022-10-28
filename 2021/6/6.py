import os

os.chdir('2021/6')

def part1(day_count):
    f = open("6.input", "r")
    # f = open("6-test.input", "r")
    fish = [int(x) for x in f.readline().split(',')]
    # print(fish)
    # part 2 wants 256 days, but that won't complete
    # day_count = 80
    for d in range(day_count):
        day = d+1
        new_fishes = 0
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6;
                new_fishes += 1
            else:
                fish[i] -= 1
        for f in range(new_fishes):
            fish.append(8)
        # print("After day {}\n{}".format(day, fish))
        # print("finished day {}".format(day))
    
    print("fish count: {}".format(len(fish)))


def part2(day_count):
    f = open("6.input", "r")
    # f = open("6-test.input", "r")
    fish = [int(x) for x in f.readline().split(',')]
    fish_map = dict.fromkeys([0,1,2,3,4,5,6,7,8], 0)
    for f in fish:
        fish_map[f] += 1

    for d in range(day_count):
        new_map = {}
        born = fish_map[0]
        # ages 1 to 8 just move down one
        for age in range(8):
            new_map[age] = fish_map[age+1]
        new_map[8] = born
        new_map[6] += born
        # print("fish {}".format(fish_map))
        # print("new  {}".format(new_map))
        fish_map = new_map
    
    fish_count = 0
    for value in fish_map.values():
        fish_count += value
    print("fish count: {}".format(fish_count))



# part1(80)
part2(256)