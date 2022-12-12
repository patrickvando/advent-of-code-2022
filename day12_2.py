from collections import deque 

filename = "day12_input.txt"
file = open(filename, 'r')
lines = file.readlines()
grid = [[lines[r][c] for c in range(len(lines[0].strip()))] for r in range(len(lines))]

target = None 
start = None
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if lines[r][c] == 'E':
            target = (r, c)
            grid[r][c] = 25
        elif lines[r][c] == 'S':
            start = (r, c)
            grid[r][c] = 0
        else:
            grid[r][c] = ord(lines[r][c]) - ord('a')

def neighbors(current, visited):
    y, x = current
    res = []
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if (ny, nx) not in visited and ny >= 0 and ny < len(grid) and nx >= 0 and nx < len(grid[0]) and  grid[ny][nx] >= grid[y][x] - 1:
            res.append((ny, nx))
    return res

visited = set([target]) 
queue = deque([(target, 0)])
while queue:
    next_, travelled = queue.popleft()
    y, x = next_
    if grid[y][x] == 0: 
        print(travelled)
        break
    for neighbor in neighbors(next_, visited):
        vals = (neighbor, travelled + 1)
        visited.add(neighbor)
        queue.append(vals)