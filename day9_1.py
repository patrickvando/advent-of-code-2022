from collections import defaultdict

filename = "day9_input.txt"
file = open(filename, 'r')
lines = file.readlines()
hy, hx = 0, 0
ty, tx = 0, 0
seen = set([])
for k in range(len(lines)):
    line = lines[k]
    dir, dist = line.strip().split()
    dist = int(dist)
    for k in range(dist):
        if dir == 'D':
            hy += 1
        elif dir == 'U':
            hy -= 1
        elif dir == 'L':
            hx -= 1
        else:
            hx += 1
        dy, dx = hy - ty, hx - tx
        if abs(dy) > 1 or abs(dx) > 1:
            if dy:
                ty += int(abs(dy)/dy)
            if dx:
                tx += int(abs(dx)/dx)
        seen.add((ty, tx)) 

print(len(seen))

    
