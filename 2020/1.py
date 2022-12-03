import os

os.chdir('2020')

def star1(filename):
    nums = {}
    f = open(filename, "r")
    for line in f:
        clean = line.strip()
        num = int(clean)
        nums[num] = 2020 - num

    for key in nums:
        if nums[key] in nums:
            # print(f"got result {key} and {nums[key]}")
            # print(f"star 1 product is {nums[key] * key}")
            break

    # every key points to a value that is 2020 - key. So we need two other keys that sum to that value
    for key in nums:
        target = nums[key]
        for key2 in nums:
            if key != key2:
                inner_target = target - key2
                if inner_target in nums:
                    print(f"got hit {key} {key2} {inner_target}")
                    print(f"star 2 product {key * key2 * inner_target}")
                    return


filename = "1.input"
# filename = "1-test.input"
star1(filename)