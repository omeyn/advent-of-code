import os
os.chdir('2023/9')

def get_pattern(readings):
    pattern = []
    for i in range(1, len(readings)):
        pattern.append(readings[i]-readings[i-1])

    return pattern

def all_zeroes(readings):
    zeroes = True
    for r in readings:
        zeroes = zeroes and r == 0
    return zeroes


def star1(input_file):
    f = open(input_file, "r")
    prediction_sum = 0
    for l in f:
        print('')
        # print(l)
        patterns = []
        reading = [int(x) for x in l.strip().split(' ')]
        patterns.append(reading)
        print(f'reading {reading}')
        prediction = reading[-1]
        while not all_zeroes(reading):
            reading = get_pattern(reading)
            patterns.append(reading)
            print(f'pattern {reading}')
            prediction += reading[-1]
        print(f'prediction for this reading is {prediction}')
        prediction_sum += prediction
        # prediction = 0
        # for i in range(len(patterns), 1, -1):
        #     prediction = prediction + patterns[i][len(patterns[i])]
        #     print(f'building prediction {prediction}')

    print(f'prediction sum is {prediction_sum}')

input = "9-test.input"
input = "9.input"
star1(input)