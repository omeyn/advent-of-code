import os

os.chdir('2021/10b')

def star1(filename):

    points = { ")": 3, "]" : 57, "}" : 1197, ">" : 25137 }
    score = 0

    f = open(filename, "r")
    for line in f:
        if line.startswith("#"):
            continue
        line = line.strip()
        result = parse(line)
        if result == "valid":
            print("Valid line: {}".format(line))
        elif result == "incomplete":
            print("Incomplete line: {}".format(line))
        else:
            score += points[result]
            print("Corrupt line: {}".format(line))
    
    print("final score: {}".format(score))

def parse(line):
    stack = []
    pairs = [ ['[', ']'], ['{','}'], ['<','>'], ['(',')'] ]
    matching_open = { "]" : "[", "}" : "{", ">" : "<", ")" : "("}
    opens = [pair[0] for pair in pairs]
    for char in line:
        # print("current stack {}".format(stack))
        # print("checking char {}".format(char))
        if char in opens:
            stack.append(char)
        elif matching_open[char] == stack[-1]:
            stack.pop(-1)
        else:
            # we're corrupt
            return char

    # print("remaining stack {}".format(stack))
    if len(stack) == 0:
        return "valid"
    else:
        return "incomplete"

def star2(filename):
    points = { "(": 1, "[" : 2, "{" : 3, "<" : 4 }
    scores = []

    f = open(filename, "r")
    for line in f:
        if line.startswith("#"):
            continue
        score = 0
        line = line.strip()
        result = complete(line)
        if len(result) > 0:
            for char in result:
                score = score * 5 + points[char]
            scores.append(score)

    scores.sort()
    # print(scores)
    score = scores[int(len(scores)/2)]
    print("final score: {}".format(score))

def complete(line):
    stack = []
    pairs = [ ['[', ']'], ['{','}'], ['<','>'], ['(',')'] ]
    matching_open = { "]" : "[", "}" : "{", ">" : "<", ")" : "("}
    opens = [pair[0] for pair in pairs]
    for char in line:
        # print("current stack {}".format(stack))
        # print("checking char {}".format(char))
        if char in opens:
            stack.append(char)
        elif matching_open[char] == stack[-1]:
            stack.pop(-1)
        else:
            # we're corrupt
            return []

    # print("remaining stack {}".format(stack))
    if len(stack) == 0:
        return []
    else:
        # return the reversed stack
        return stack[::-1]

filename = "10.input"
# filename = "10-test.input"
# filename = "10-simple.input"
# star1(filename)
star2(filename)