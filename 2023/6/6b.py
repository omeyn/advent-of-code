import os

os.chdir('2023/6')

def star1(input_file):
    f = open(input_file, "r")

    times = []
    for time in f.readline().split(':')[1].strip().split(' '):
        if len(time.strip()) > 0:
            times.append(time.strip())
    time = int(''.join(times))
    # print(time)

    dists = []
    for dist in f.readline().split(':')[1].strip().split(' '):
        if len(dist.strip()) > 0:
            dists.append(dist.strip())
    dist = int(''.join(dists))
    # print(dist)
    
    winners = 0
    for s in range(1, time):
        # print(f"race {time} at button held for {s} gives distance {distance_for_time(s, time)} compared to record {dists[idx]}")
        if distance_for_time(s, time) > dist:
            winners += 1

    print(winners)

def distance_for_time(button_time, race_time):
    return (race_time - button_time) * button_time

# input = "6-test.input"
input = "6.input"
star1(input)
