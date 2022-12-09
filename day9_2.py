from collections import defaultdict

def visualize(locs):
    min_y, min_x, max_y, max_x = 0, 0, 0, 0
    for y, x in locs:
        min_y, min_x = min(y, min_y), min(x, min_x)
        max_y, max_x = max(y, max_y), max(x, max_x)
    grid = [['.' for k in range(max_x - min_x + 1)] for j in range(max_y - min_y + 1)]
    grid[-min_y][-min_x] = 's'
    for k in range(len(locs)):
        y, x = locs[k]
        if k == 0:
            grid[y - min_y][x - min_x] = 'H'
        else:
            grid[y - min_y][x - min_x] = str(k)
    for row in grid:
        print("".join(row))
    print()

filename = "day9_input.txt"
file = open(filename, 'r')
lines = file.readlines()
seen = set([])
snake = [(0, 0)] * 10
for k in range(len(lines)):
    line = lines[k]
    dir, dist = line.strip().split()
    dist = int(dist)
    for k in range(dist):
        hy, hx = snake[0]
        if dir == 'D':
            hy += 1
        elif dir == 'U':
            hy -= 1
        elif dir == 'L':
            hx -= 1
        else:
            hx += 1
        snake[0] = (hy, hx)
        for j in range(1, len(snake)):
            hy, hx = snake[j - 1]
            ty, tx = snake[j]
            dy, dx = hy - ty, hx - tx
            if abs(dy) > 1 or abs(dx) > 1:
                if dy:
                    ty += int(abs(dy)/dy)
                if dx:
                    tx += int(abs(dx)/dx)
            snake[j] = (ty, tx)
        tail = snake[-1]
        seen.add(tail)
    visualize(snake) 
print(len(seen))