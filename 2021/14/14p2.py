import os
import re
import secrets

os.chdir('2021/14')

def do_subs(template, subs2, subs4={}, subs8={}):
    new_template = ""
    i = 0
    while i < len(template)-1:
        # snippet = template[i:i+8]
        if template[i:i+8] in subs8:
            new_template += subs8[template[i:i+8]]
            i += 7
        elif template[i:i+4] in subs4:
            print("got 4 hit")
            new_template += subs4[template[i:i+4]]
            i += 3
        elif template[i:i+2] in subs2:
            # print(f"Checking snippet {template[i:i+2]}")
            if len(new_template) == 0:
                new_template = subs2[template[i:i+2]]
            else:
                new_template += subs2[template[i:i+2]][1:]
            i += 1
        else:
            if i < len(template)-1:
                new_template += template[i]
                i += 1
        # print(f"Building new template {new_template}")
    if i < len(template)-1:
        new_template += template[-1]


    # return ''.join(new_template)
    return new_template

def build_subs(size, letters, subs2):
    count = size * 10
    new_subs = {}
    for i in range(count):
        starter = ''.join(secrets.choice(letters) for _ in range(size))
        sub = do_subs(starter, subs2)
        new_subs[starter] = sub

    return new_subs


def star2(filename):
    subs2 = {}
    letter_set = set()
    f = open(filename, "r")
    for line in f:
        if line.startswith("#") or len(line.strip()) == 0:
            continue
        line = line.strip()
        if "->" in line:
            raw = line.split('->')
            # pattern = raw[0].strip()
            # replacement = pattern[0] + raw[1].strip()
            # subs[pattern] = replacement
            pattern = raw[0].strip()
            replacement = pattern[0] + raw[1].strip() + pattern[1]
            letter_set.add(pattern[0])
            letter_set.add(pattern[1])
            letter_set.add(raw[1].strip())
            subs2[pattern] = replacement
        else:
            template = line
    
    # print(f"Got template {template}")
    for sub in subs2:
        print(f"{sub}-{subs2[sub]}")

    letters = ''.join(l for l in letter_set)
    print(f"got unique letters {letters}")
    
    subs4 = build_subs(4, letters, subs2)

    # on test input we expect length 3073 after 10 steps
    print(f"starting template {template}")
    for x in range(3):
        new = do_subs(template, subs2, subs4, {})
        # subs[template] = new
        template = new
        print(f"new template {template}")
        print(f"After step {x+1} template length is {len(template)}")

    # counts = {}
    # for letter in template:
    #     if letter in counts:
    #         counts[letter] += 1
    #     else:
    #         counts[letter] = 1
    # max_count = 0
    # min_count = 10000
    # for letter in counts:
    #     if counts[letter] > max_count:
    #         max_count = counts[letter]
    #     if counts[letter] < min_count:
    #         min_count = counts[letter]
    # print(f"max - min counts gives {max_count-min_count}")

filename = "14.input"
filename = "14-test.input"
# filename = "14-simple.input"
star2(filename)