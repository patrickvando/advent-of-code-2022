import re


filename = "day15_input.txt"
file = open(filename, 'r')
lines = file.readlines()

sensors_beacons = []
beacons = set([])
for line in lines:
    pattern = re.compile(r'-?[0-9]+')
    sx, sy, bx, by = [int(item) for item in re.findall(pattern, line)]
    sensors_beacons.append([sy, sx, by, bx])
    beacons.add((by, bx))

covered = set([])
target_row = 2000000
for sensor_beacon in sensors_beacons:
    sy, sx, by, bx = sensor_beacon
    dy = sy - by
    dx = sx - bx
    radius = abs(dy) + abs(dx)
    buffer = radius - abs(sy - target_row)
    for x in range(sx - buffer, sx + buffer + 1):
        if (target_row, x) not in beacons:
            covered.add((target_row, x))
print(len(covered))
