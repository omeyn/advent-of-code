import os

os.chdir('2022/10')

def render_screen(screen):
    line = ""
    for i, pixel in enumerate(screen):
        line = line + pixel
        if (i+1) % 40 == 0:
            print(line)
            line = ""

def star1(filename):
    f = open(filename, 'r')
    cycle = 1
    x = 1
    power_sum = 0
    for raw in f:
        line = raw.strip()
        if line.startswith('#'):
            continue
        parsed = line.split(" ")
        # print(f"checking {parsed}")
        if parsed[0] == "noop":
            cycle += 1
        else:
            if cycle % 40 == 19:
                print(f"After cycle {cycle+1} x is {x}, power is {(cycle+1)*x}")
                power_sum += (cycle+1)*x
            cycle += 2
            x += int(parsed[1])
        if cycle % 40 == 20:
            print(f"After cycle {cycle} x is {x}, power is {cycle*x}")
            power_sum += cycle*x

    print(f"star 1 result {power_sum}")

def update_screen(pixel_pos, x, cycle, screen):
    pos = pixel_pos - (cycle // 40)*40
    print(f"updating pos {pos} for pixel_pos {pixel_pos} in cycle {cycle}")
    if pos >= x-1 and pos <= x+1:
        screen[pixel_pos] = '#'

def star2(filename):
    f = open(filename, 'r')
    cycle = 1
    x = 1
    screen = ['.' for i in range(240)]
    pixel_pos = -1
    for raw in f:
        line = raw.strip()
        if line.startswith('#'):
            continue
        parsed = line.split(" ")
        pixel_pos += 1
        if parsed[0] == "noop":
            cycle += 1
            update_screen(pixel_pos, x, cycle, screen)
        else:
            update_screen(pixel_pos, x, cycle, screen)
            pixel_pos += 1
            update_screen(pixel_pos, x, cycle+1, screen)
            cycle += 2
            x += int(parsed[1])

    render_screen(screen)

filename = "10.input"
# filename = "10-test.input"
# star1(filename)
star2(filename)
