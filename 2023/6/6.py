import os

os.chdir('2023/6')

def star1(input_file):
    f = open(input_file, "r")

    times = []
    for time in f.readline().split(':')[1].strip().split(' '):
        if len(time.strip()) > 0:
            times.append(int(time.strip()))
    print(times)

    dists = []
    for dist in f.readline().split(':')[1].strip().split(' '):
        if len(dist.strip()) > 0:
            dists.append(int(dist.strip()))
    print(dists)
    
    wins = {}
    for idx, time in enumerate(times):
        winners = 0
        for s in range(1, time):
            print(f"race {time} at button held for {s} gives distance {distance_for_time(s, time)} compared to record {dists[idx]}")
            if distance_for_time(s, time) > dists[idx]:
                winners += 1
        wins[idx] = winners

    print(wins)
    print(f"result {wins[0] * wins[1] * wins[2] * wins[3]}")

def distance_for_time(button_time, race_time):
    return (race_time - button_time) * button_time

input = "6-test.input"
input = "6.input"
star1(input)
