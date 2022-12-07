import os

os.chdir('2020')

def star1(filename):
    f = open(filename, "r")
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passport = {}
    valid = 0
    for line in f:
        clean = line.strip()
        if len(clean) == 0: # this passport is done            
            if set(required_fields).issubset(set(passport.keys())):
                valid += 1
            else:
                print(f"invalid passport {passport}")
                print(f"missing fields {required_fields - passport.keys()}")
            passport = {}
        else:
            fields = clean.split(" ")
            for field in fields:
                parts = field.split(":")
                passport[parts[0]] = parts[1]
    print(f"valid passports {valid}")


filename = "4.input"
# filename = "4-test.input"
star1(filename)
# star2(filename)