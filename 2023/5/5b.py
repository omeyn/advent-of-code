import os
import sys

os.chdir('2023/5')

# tried the dumb way and didn't work, took 12 hrs?
# got new min location 1852510996
# got new min location 662918194
# got new min location 350004378
# got new min location 201731623
# got new min location 47238415
# got new min location 24261546
# min location is 24261546

# cheating, result should be 24261545 (OFF BY FUCKING ONE!)

class Range:
    def __init__(self, source_range_start: int, dest_range_start: int, range_size: int):
        self.source_range_start = source_range_start
        self.dest_range_start = dest_range_start
        self.range_size = range_size

    def is_in_range(self, source):
        return source >= self.source_range_start and source < self.source_range_start + self.range_size
    
    def find_dest(self, source):
        return self.dest_range_start + (source - self.source_range_start)

class RangedLookup:
    def __init__(self, name: str):
        self.name = name
        self.ranges = []

    def add_range(self, r: Range):
        self.ranges.append(r)

    def find_dest_for_source(self, source: int):
        for r in self.ranges:
            if r.is_in_range(source):
                return r.find_dest(source)
        
        # not in any ranges, return source as the dest
        return source

def is_valid_seed(seed, seed_sets):
    for seed_set in seed_sets:
        if seed in range(seed_set[0], seed_set[0]+seed_set[1]):
            return True
        
    return False

def star1(input_file):
    f = open(input_file, "r")
    raw_seeds = [int(x) for x in f.readline().split(':')[1].strip().split(' ')]
    seed_sets = []
    min_seed = 50000000000
    max_seed = 0
    for i in range(0, len(raw_seeds), 2):
        if raw_seeds[i] < min_seed:
            min_seed = raw_seeds[i]
        if raw_seeds[i] + raw_seeds[i+1] > max_seed:
            max_seed = raw_seeds[i] + raw_seeds[i+1]
        seed_sets.append([raw_seeds[i], raw_seeds[i+1]])

    # print(f'min seed {min_seed} max seed {max_seed}')
    print(seed_sets)

    f.readline()
    lookups = {}
    for line in f:
        if len(line.strip()) > 0:
            if 'map:' in line:
                map_name = line.split(' ')[0].strip()
                ranged_lookup = RangedLookup(map_name)
                print(f"new lookup {map_name}")
                lookups[map_name] = ranged_lookup
            else:
                nums = [int(x) for x in line.strip().split(' ')]
                new_range = Range(source_range_start=nums[0], dest_range_start=nums[1], range_size=nums[2])
                ranged_lookup.add_range(new_range)

    # print(lookups)
    min_location = sys.maxsize
    location = 24000000
    while True:
        location += 1
        if location % 500000 == 0:
            print(f'checked {location} locations')
        humid = lookups['humidity-to-location'].find_dest_for_source(location)
        temp = lookups['temperature-to-humidity'].find_dest_for_source(humid)
        light = lookups['light-to-temperature'].find_dest_for_source(temp)
        water = lookups['water-to-light'].find_dest_for_source(light)
        fert = lookups['fertilizer-to-water'].find_dest_for_source(water)
        soil = lookups['soil-to-fertilizer'].find_dest_for_source(fert)
        seed = lookups['seed-to-soil'].find_dest_for_source(soil)
        
        # print(f"seed {seed} soil {soil} fert {fert} water {water} light {light} temp {temp} humid {humid} location {location}")

        if is_valid_seed(seed, seed_sets):
            print(f'got valid seed at location {location} - thats our min!')
            print(f"seed {seed} soil {soil} fert {fert} water {water} light {light} temp {temp} humid {humid} location {location}")
            break


def test():
    seed_sets = [[0, 10], [15,5], [79,14]]
    seed = 0
    print(f'seed {seed} is {is_valid_seed(seed, seed_sets)}')
    seed = 5
    print(f'seed {seed} is {is_valid_seed(seed, seed_sets)}')
    seed = 10
    print(f'seed {seed} is {is_valid_seed(seed, seed_sets)}')
    seed = 11
    print(f'seed {seed} is {is_valid_seed(seed, seed_sets)}')
    seed = 15
    print(f'seed {seed} is {is_valid_seed(seed, seed_sets)}')
    seed = 19
    print(f'seed {seed} is {is_valid_seed(seed, seed_sets)}')
    seed = 20
    print(f'seed {seed} is {is_valid_seed(seed, seed_sets)}')
    seed = 21
    print(f'seed {seed} is {is_valid_seed(seed, seed_sets)}')
    seed = 92
    print(f'seed {seed} is {is_valid_seed(seed, seed_sets)}')
    seed = 93
    print(f'seed {seed} is {is_valid_seed(seed, seed_sets)}')

# test()

# input = "5-test.input"
# input = "5-test2.input"
input = "5.input"
star1(input)