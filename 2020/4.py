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
                # print(f"invalid passport {passport}")
                print(f"missing fields {required_fields - passport.keys()}")
            passport = {}
        else:
            fields = clean.split(" ")
            for field in fields:
                parts = field.split(":")
                passport[parts[0]] = parts[1]
    print(f"valid passports {valid}")

def is_year_in(letters, start, end):
    if letters.isnumeric:
        year = int(letters)
        return year >= start and year <= end

    return False

def star2(filename):
    f = open(filename, "r")
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    passport = {}
    invalid_passports = []
    valid_count = 0
    for line in f:
        clean = line.strip()
        if len(clean) == 0: # this passport is done            
            if set(required_fields).issubset(set(passport.keys())):
                valid = True
                print(f"checking passport {passport}")
                valid = valid and is_year_in(passport['byr'], 1920, 2002)
                print(f"valid after byr {valid}")
                valid = valid and is_year_in(passport['iyr'], 2010, 2020)
                print(f"valid after iyr {valid}")
                valid = valid and is_year_in(passport['eyr'], 2020, 2030)
                print(f"valid after eyr {valid}")
                height = passport['hgt']
                if height.endswith('cm'):
                    val = int(height.split('c')[0])
                    if val < 150 or val > 193:
                        valid = False
                elif height.endswith('in'):
                    val = int(height.split('i')[0])
                    if val < 59 or val > 76:
                        valid = False
                else:
                    valid = False
                print(f"valid after hgt {valid}")
                valid = valid and passport['hcl'].startswith('#') and len(passport['hcl']) == 7
                print(f"valid after hcl {valid}")
                valid = valid and passport['ecl'] in valid_eyes
                print(f"valid after ecl {valid}")
                valid = valid and passport['pid'].isnumeric and len(passport['pid']) == 9
                print(f"valid after pid {valid}")
                if valid:
                    print("incr valid")
                    valid_count += 1
                else:
                    invalid_passports.append(passport)
            # else:
                # print(f"invalid passport {passport}")
                # print(f"missing fields {required_fields - passport.keys()}")
            passport = {}
        else:
            fields = clean.split(" ")
            for field in fields:
                parts = field.split(":")
                passport[parts[0]] = parts[1].strip()

    print(f"valid passports {valid_count}")


filename = "4.input"
# filename = "4-test.input"
# star1(filename)
star2(filename)