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

class Range:
    def __init__(self, source_range_start: int, dest_range_start: int, range_size: int):
        self.source_range_start = source_range_start
        self.dest_range_start = dest_range_start
        self.range_size = range_size

    def is_in_range(self, source):
        return source >= self.source_range_start and source <= self.source_range_start + self.range_size
    
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


def star1(input_file):
    f = open(input_file, "r")
    raw_seeds = [int(x) for x in f.readline().split(':')[1].strip().split(' ')]
    seed_sets = []
    for i in range(0, len(raw_seeds), 2):
        seed_sets.append([raw_seeds[i], raw_seeds[i+1]])

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
                new_range = Range(source_range_start=nums[1], dest_range_start=nums[0], range_size=nums[2])
                ranged_lookup.add_range(new_range)

    # print(lookups)
    min_location = sys.maxsize
    for seed_set in seed_sets:
        for i in range(seed_set[1]):
            seed = seed_set[0] + i
            soil = lookups['seed-to-soil'].find_dest_for_source(seed)
            fert = lookups['soil-to-fertilizer'].find_dest_for_source(soil)
            water = lookups['fertilizer-to-water'].find_dest_for_source(fert)
            light = lookups['water-to-light'].find_dest_for_source(water)
            temp = lookups['light-to-temperature'].find_dest_for_source(light)
            humid = lookups['temperature-to-humidity'].find_dest_for_source(temp)
            location = lookups['humidity-to-location'].find_dest_for_source(humid)
        #     print(f"seed {seed} soil {soil} fert {fert} water {water} light {light} temp {temp} humid {humid} location {location}")
            if location < min_location:
                print(f'got new min location {location}')
                min_location = location

    print(f'min location is {min_location}')


input = "5-test.input"
input = "5.input"
star1(input)