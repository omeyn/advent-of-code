import os
import copy
import math

os.chdir('2021/14')

########### 
# Failed attempt at frequency analysis - works for 10 steps, but not 40. Counts are off, don't know why
##########

def incr_term(counts, term, increment):
    if term in counts:
        counts[term] += increment
    else:
        counts[term] = increment

def count_letters(counts):
    letter_counts = {}
    # print(f"about to count {counts}")
    for term in counts:
        for letter in term:
            if letter in letter_counts:
                letter_counts[letter] += counts[term]
            else:
                letter_counts[letter] = counts[term]
    # print(f"pre divide letter counts: {letter_counts}")
    for letter in letter_counts:
        letter_counts[letter] = math.ceil(letter_counts[letter] / 2.0)
    # print(f"post divide letter counts: {letter_counts}")

    return letter_counts

def star1(filename):
    subs = {}
    f = open(filename, "r")
    for line in f:
        if line.startswith("#") or len(line.strip()) == 0:
            continue
        line = line.strip()
        if "->" in line:
            raw = line.split('->')
            key = raw[0].strip()
            rep = raw[1].strip()
            subs[key] = [key[0]+rep, rep+key[1]]
        else:
            template = line
    print(template)
    print(subs)
    counts = {}

    # this is the first "loop"
    for i in range(len(template)-1):
        cut = template[i:i+2]
        if cut in subs:
            terms = subs[cut]
            print(f"subbing {cut} for {terms}")
            incr_term(counts, terms[0], 1)
            incr_term(counts, terms[1], 1)

    print(f"starting counts {counts}")
    loops = 39
    for i in range(1, loops):
        new_counts = {}
        for term in counts:
            if term in subs:
                terms = subs[term]
                incr_term(new_counts, terms[0], counts[term])
                incr_term(new_counts, terms[1], counts[term])
        # print(new_counts)
        counts = new_counts
        # print(f"Counts after loop {i+1}: \n{counts}")
        letter_counts = count_letters(counts)
        # print(letter_counts)

    letter_counts = count_letters(counts)
    # print(letter_counts)

    max_count = 0
    min_count = 10000
    for letter in letter_counts:
        if letter_counts[letter] > max_count:
            max_count = letter_counts[letter]
        if letter_counts[letter] < min_count:
            min_count = letter_counts[letter]
    print(f"max - min counts gives {max_count-min_count}")

# after 1 step should have NCNBCHB
# so NC 1 CN 1 NB 1 BC 1 CH 1 HB 1
# letter count N 2 C 2 B 2 H 1

# after 2 it's NBCCNBBBCBHCB
# so NB 2 BC 2 CC 1 CN 1 BB 2 CB 2 BH 1 HC 1
# letter count N 2 B 6 C 4 H 1

# 4290332661591 is too high

filename = "14.input"
# filename = "14-test.input"
star1(filename)