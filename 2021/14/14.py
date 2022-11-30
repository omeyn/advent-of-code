import os

os.chdir('2021/14')

def do_subs(template, subs):
    new_template = []
    tl = list(template)
    for i in range(len(tl)-1):
        bit = f"{tl[i]}{tl[i+1]}"
        # print(f"checking {bit}")
        new_template.append(tl[i])
        if bit in subs:
            new_template.append(subs[bit])
    new_template.append(tl[-1])

    # return ''.join(new_template)
    return new_template

def star1(filename):
    subs = {}
    f = open(filename, "r")
    for line in f:
        if line.startswith("#") or len(line.strip()) == 0:
            continue
        line = line.strip()
        if "->" in line:
            raw = line.split('->')
            subs[raw[0].strip()] = raw[1].strip()
        else:
            template = line
    
    # print(f"Got template {template}")
    # for sub in subs:
    #     print(f"{sub}-{subs[sub]}")

    print(f"starting template {template}")
    for x in range(2):
        template = do_subs(template, subs)
        print(f"new template {template}")
        print(f"After step {x+1} template length is {len(template)}")

    counts = {}
    for letter in template:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    max_count = 0
    min_count = 10000
    for letter in counts:
        if counts[letter] > max_count:
            max_count = counts[letter]
        if counts[letter] < min_count:
            min_count = counts[letter]
    print(f"max - min counts gives {max_count-min_count}")

filename = "14.input"
filename = "14-test.input"
# filename = "14-simple.input"
star1(filename)