import os

os.chdir('2022/9')

def test_touching():
    assert touching( (0,0), (0,0) )
    assert touching( (0,0), (0,1) )
    assert touching( (0,0), (1,1) )
    assert touching( (0,0), (1,0) )
    assert touching( (0,0), (0,-1) )
    assert touching( (0,0), (-1,-1) )
    assert touching( (0,0), (-1,0) )
    assert not touching( (0,0), (0,2))

def touching(h, t):
    if (t[0] == h[0]+1 or t[0] == h[0]-1 or t[0] == h[0]) and (t[1] == h[1]+1 or t[1] == h[1]-1 or t[1] == h[1]):
        return True

    return False

def viz(h, t):
    max_x = max(int(h[0]), int(t[0]))
    # min_x = min(int(h[0]), int(t[0]))
    max_y = max(int(h[1]), int(t[1]))
    # min_y = min(int(h[1]), int(t[1]))
    # print(h)
    # print(t)
    # grid = [['.' for x in range(max_x +5 - min_x)] for y in range(max_y + 5 - min_y)]
    grid = [['.' for x in range(max_x +5)] for y in range(max_y + 5)]
    # h_x = int(h[0])-min_x
    # h_y = int(h[1])-min_y
    # t_x = int(t[0])-min_x
    # t_y = int(t[1])-min_y
    h_x = int(h[0])
    h_y = int(h[1])
    t_x = int(t[0])
    t_y = int(t[1])
    print(h_x)
    print(h_y)
    grid[h_x][h_y] = 'H' 
    grid[t_x][t_y] = 'T' 
    for y in range(len(grid)):  
        print(''.join(grid[y]))



def move(t, h, fields, t_visits):
    if touching(h, t):
        return t

    diff_x = h[0] - t[0]
    diff_y = h[1] - t[1]
    if diff_x != 0 and diff_y != 0:
        print(f"fields {fields} with diffx {diff_x} and diffy {diff_y}")
        assert abs(diff_x) == 1 or abs(diff_y) == 1
        # need diagonal
        if abs(diff_x) == 1:
            if diff_y > 0:
                t = (h[0], t[1]+1)
            else:
                t = (h[0], t[1]-1)
        else:
            if diff_x > 0:
                t = (t[0]+1, h[1])
            else:
                t = (t[0]-1, h[1])
        print(f"diagonal move for t to {t}")
        t_visits.add(t)

    if touching(h, t):
        return t

    diff_x = h[0] - t[0]
    diff_y = h[1] - t[1]
    print(f"new diffx {diff_x} diffy {diff_y}")
    if diff_x == 0:
        # move in y
        if diff_y > 0:
            for x in range(diff_y-1):
                t = (t[0], t[1]+1)
                t_visits.add(t)
        else:
            for x in range(abs(diff_y)-1):
                t = (t[0], t[1]-1)
                t_visits.add(t)
        print(f"vert move for t to {t}")
    else: # diff_y == 0
        # move in x
        if diff_x > 0:
            for x in range(diff_x-1):
                t = (t[0]+1, t[1])
                t_visits.add(t)
        else:
            for x in range(abs(diff_x)-1):
                t = (t[0]-1, t[1])
                t_visits.add(t)
        print(f"horiz move for t to {t}")
    return t

def star2(filename):
    f = open(filename, 'r')
    # (x, y)
    h = (100,100)
    t = (100,100)
    t_visits = set(t)
    for raw in f:
        line = raw.strip()
        if line.startswith('#'):
            continue

        fields = line.split(' ')
        print(f"{fields[0]} {fields[1]}")
        match fields[0]:
            case 'R':
                h = (h[0] + int(fields[1]), h[1])
            case 'L':
                h = (h[0] - int(fields[1]), h[1])
            case 'U':
                h = (h[0], h[1] + int(fields[1]))
            case 'D':
                h = (h[0], h[1] - int(fields[1]))
        print(f"moved H to {h}")
        # viz(h,t)
        t = move(t, h, fields, t_visits)
        print(f"moved T to {t}")
        # viz(h,t)
        assert touching(h,t)
        print(f"T move count {len(t_visits)}")


    print(f"star 1 result {len(t_visits)}")

# 5312 too low
# 6091 too high
# 6090 is right - pure guess. Off by one somewhere!

filename = "9.input"
filename = "9-test2.input"
filename = "9-test.input"
# star1(filename)
star2(filename)

# test_touching()
# h = (10,10)
# t = (11,11)
# viz(h,t)