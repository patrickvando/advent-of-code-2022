filename = "day22_input.txt"
with open(filename) as f:
    lines = f.readlines()
lines = [line.rstrip() for line in lines]

grid = {} 

def parse_path(path):
    res = []
    current = ""
    for c in path:
        if c in 'LR':
            res.append(int(current))
            current = ""
            res.append(c)
        else:
            current += c
    if current:
        res.append(int(current))
    return res

path = parse_path(lines.pop())

lines.pop()
start_pos = (None, None)
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == ".":
            if start_pos == (None, None):
                start_pos = (r, c)
            grid[(r, c)] = "."
        elif lines[r][c] == "#":
            grid[(r, c)] = "#"

def display_lines(lines, visited):
    rows = [] 
    for r in range(len(lines)):
        row = []
        for c in range(len(lines[r])):
            if (r, c) in visited:
                row.append('x')
            else:
                row.append(lines[r][c])
        rows.append(row)
    for row in rows:
        print("".join(row))

visited = set([])
def move(pos, dir, dist):
    y, x = pos
    dy, dx = dirs[dir] 
    for k in range(dist):
        visited.add((y, x))
        ny, nx = y + dy, x + dx
        if (ny, nx) not in grid:
            while (ny - dy, nx - dx) in grid:
                ny, nx = ny - dy, nx - dx
        if grid[(ny, nx)] == "#":
            return y, x
        y, x = ny, nx
    return (ny, nx)


        
dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
current_dir = 0 
current_pos = start_pos 
for k in range(len(path)):
    if path[k] == 'R':
        current_dir = (current_dir + 1) % len(dirs)
    elif path[k] == 'L':
        current_dir = (current_dir - 1) % len(dirs)
    else:
        current_pos = move(current_pos, current_dir, path[k])

y, x = current_pos
print((y + 1) * 1000 + 4 * (x + 1) + current_dir)