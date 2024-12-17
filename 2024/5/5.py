import os
import re
import numpy as np

os.chdir('2024/5')

def star1(input_file):
    f = open(input_file, "r")
    rules = {}

    in_pages = False
    sum = 0
    for line in f:
        if line.strip() == "":
            in_pages = True
            continue

        if in_pages:
            page = [int(x) for x in line.strip().split(",")]
            print(page)
            is_valid = True
            for i, p in enumerate(page):
                print(f"p: {p} has {page[:i]} in front of it")
                if len(page[:i]) > 0:
                    for pre in page[:i]:
                        if rules.get(p) and pre in rules.get(p):
                            print(f"got bad page: {p} in page {page}, violates rule {p} before {rules.get(p)}")
                            is_valid = False
            
            if is_valid:
                middle_page = page[len(page) // 2]
                sum += int(middle_page)
                print(f"middle page: {middle_page} for valid book: {page}")

        if not in_pages:
            rule = line.strip().split("|")
            key = int(rule[0])
            print(f"key: {key}")
            print(f"rules: {rules}")
            if key in rules:
                rules[key].add(int(rule[1]))
            else:
                rules[key] = {int(rule[1])}

    print(f"Final sum: {sum}")

def star2(input_file):
    f = open(input_file, "r")
    rules = {}

    in_pages = False
    sum = 0
    for line in f:
        if line.strip() == "":
            in_pages = True
            continue

        if in_pages:
            page = [int(x) for x in line.strip().split(",")]
            is_valid, bad_page = validate_page(page, rules)
            
            if not is_valid:
                while not is_valid:
                    a = page[bad_page]
                    b = page[bad_page-1]
                    page[bad_page] = b
                    page[bad_page-1] = a

                    is_valid, bad_page = validate_page(page, rules)

                p = page[len(page) // 2]
                sum += int(p)
                print(f"middle page: {p} for newly valid book: {page}")

        if not in_pages:
            rule = line.strip().split("|")
            key = int(rule[0])
            # print(f"key: {key}")
            # print(f"rules: {rules}")
            if key in rules:
                rules[key].add(int(rule[1]))
            else:
                rules[key] = {int(rule[1])}

    print(f"Final sum: {sum}")


def validate_page(page, rules):
    is_valid = True
    for i, p in enumerate(page):
        # print(f"p: {p} has {page[:i]} in front of it")
        if len(page[:i]) > 0:
            for pre in page[:i]:
                if rules.get(p) and pre in rules.get(p):
                    print(f"got bad page: {p} in page {page}, violates rule {p} before {rules.get(p)}")
                    is_valid = False
                    return False, i

    return True, None

input = "5-test.input"
input = "5.input"
# star1(input)
star2(input)