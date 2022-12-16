from collections import deque
import re
import sys


filename = "day15_input.txt"
file = open(filename, 'r')
lines = file.readlines()

sensor_radii = []
for line in lines:
    pattern = re.compile(r'-?[0-9]+')
    sx, sy, bx, by = [int(item) for item in re.findall(pattern, line)]
    radius = abs(bx - sx) + abs(by - sy)
    sensor_radii.append([sy, sx, radius])
sensor_radii.sort(key=lambda x: x[-1])

def check_point(point_y, point_x):
    if point_y < 0 or point_y > limit or point_x < 0 or point_x > limit:
        return False
    valid = True
    for sensor_beacon_radius in sensor_radii:
        sy, sx, compare_radius = sensor_beacon_radius
        if abs(point_y - sy) + abs(point_x - sx) <= compare_radius:
            valid = False
            break
    return valid

def check_circumference(center_y, center_x, radius):
    tr_y, tr_x = center_y + radius, center_x
    tl_y, tl_x = center_y + radius, center_x
    br_y, br_x = center_y - radius, center_x
    bl_y, bl_x = center_y - radius, center_x
    for _ in range(radius):
        for y, x in [(tr_y, tr_x), (tl_y, tl_x), (br_y, br_x), (bl_y, bl_x)]:
            if check_point(y, x):
                print(x * 4000000 + y)
                sys.exit(0)
        tr_y -= 1
        tr_x += 1
        tl_y -= 1
        tl_x -= 1
        br_y += 1
        br_x += 1
        bl_y -= 1
        bl_x -= 1


visited = set([])
limit = 4000000 
for sensor_radius in sensor_radii:
    center_y, center_x, radius = sensor_radius 
    check_circumference(center_y, center_x, radius + 1)



