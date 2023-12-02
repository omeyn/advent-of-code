import os
import re

os.chdir('2023/1')

def star1(input_file):
    f = open(input_file, "r")

    pattern = '/\D+'

    sum = 0
    for line in f:
        # print(line)
        digits = re.sub('\D', '', line)
        # print(digits)
        result = int(digits[0])*10 + int(digits[len(digits)-1])
        # print(result)
        sum += result

    print(sum)

input = "1-test.input"
input = "1.input"
star1(input)
