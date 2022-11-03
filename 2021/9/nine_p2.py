import nine_p1
import os
import time

# os.chdir('2021/9')

def star2(filename):
    f = open(filename, "r")
    seafloor = []
    for line in f:
        row = list(line.strip())
        row = [int(x) for x in row]
        seafloor.append(row)

    basin_1 = 0
    basin_2 = 0
    basin_3 = 0

    width = len(seafloor[0])
    height = len(seafloor)

    checked = [[0 for x in range(width)] for y in range(height)]

    lows = nine_p1.star1(filename)
    for y in range(height):
        for x in range(width):
            if lows[y][x] > 0:
                print("checking low at y {} x {}".format(y, x))
                basin_size = build_basin(x, y, width, height, seafloor, checked, 0)
                basin_size = build_basin(x, y, width, height, seafloor, checked, basin_size)
                basin_size = build_basin(x, y, width, height, seafloor, checked, basin_size)
                basin_size = build_basin(x, y, width, height, seafloor, checked, basin_size)
                print("found basin of size {}".format(basin_size))
                if basin_size > basin_1:
                    basin_3 = basin_2
                    basin_2 = basin_1
                    basin_1 = basin_size
                elif basin_size > basin_2:
                    basin_3 = basin_2
                    basin_2 = basin_size
                elif basin_size > basin_3:
                    basin_3 = basin_size

    print("basin product: {}".format(basin_1*basin_2*basin_3))

def build_basin(x, y, width, height, seafloor, checked, basin_size):
    # print("build basin called with x={} y={}".format(x, y))
    # time.sleep(1)
    if x >= width or x < 0 or y >= height or y < 0:
        return basin_size

    if seafloor[y][x] == 9 or checked[y][x] == 1:
        return basin_size
    
    basin_size += 1
    checked[y][x] = 1

    basin_size = build_basin(x, y-1, width, height, seafloor, checked, basin_size)
    basin_size = build_basin(x, y+1, width, height, seafloor, checked, basin_size)
    basin_size = build_basin(x-1, y, width, height, seafloor, checked, basin_size)
    return build_basin(x+1, y, width, height, seafloor, checked, basin_size)

        # case "down":
        #     basin_size = build_basin(x, y-1, width, height, seafloor, basin_size, "down")
        #     # basin_size = build_basin(x, y+1, width, height, seafloor, basin_size, "up")
        #     basin_size = build_basin(x-1, y, width, height, seafloor, basin_size, "right")
        #     return build_basin(x+1, y, width, height, seafloor, basin_size, "left")
        # case "left":
        #     basin_size = build_basin(x, y-1, width, height, seafloor, basin_size, "down")
        #     basin_size = build_basin(x, y+1, width, height, seafloor, basin_size, "up")
        #     # return build_basin(x-1, y, width, height, seafloor, basin_size, "right")
        #     return build_basin(x+1, y, width, height, seafloor, basin_size, "left")
        # case "right":
        #     basin_size = build_basin(x, y-1, width, height, seafloor, basin_size, "down")
        #     basin_size = build_basin(x, y+1, width, height, seafloor, basin_size, "up")
        #     return build_basin(x-1, y, width, height, seafloor, basin_size, "right")
        #     # return build_basin(x+1, y, width, height, seafloor, basin_size, "left")
    
filename = "9.input"
# filename = "9-test.input"
star2(filename)