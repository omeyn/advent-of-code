import os

os.chdir('2022/7')

def debug(filename):
    f = open(filename, "r")
    f.readline()
    sum = 0
    for raw in f:
        line = raw.strip()
        parts = line.split(' ')
        if parts[0].isnumeric():
            print(f"adding {parts[0]} from line {line}")
            sum += int(parts[0])

    print(f"final filesize sum {sum}")


def visualize(filename):
    f = open(filename, "r")
    f.readline()
    print("- / (dir)")
    indent = 0
    for raw in f:
        line = raw.strip()
        if line.startswith('$ cd'):
            fields = line.split(' ')
            if fields[2] == '..':
                indent -= 2
            else:
                indent += 2
                print(f"{(indent)*' '} - {fields[2]} (dir)")
        elif line == ('$ ls'):
            continue
        else:
            fields = line.split(' ')
            if fields[0] == 'dir':
                continue
            else:
                print(f"{(indent+2)*' '} - {fields[1]} (file, size={fields[0]})")
            

filename = "7.input"
# filename = "7-test2.input"
# filename = "7-test.input"

# debug(filename)
visualize(filename)