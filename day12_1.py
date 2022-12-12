from heapq import heappush, heappop

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

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def neighbors(current):
    y, x = current
    res = []
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if ny >= 0 and ny < len(grid) and nx >= 0 and nx < len(grid[0]) and grid[ny][nx] <= grid[y][x] + 1:
            res.append((ny, nx))
    return res

visited = set([]) 
heap = [(manhattan(start, target), start, 0)]

while heap:
    dist, next_, travelled = heappop(heap)
    visited.add((next_, travelled))
    if next_ == target:
        print(travelled)
        break
    for neighbor in neighbors(next_):
        vals = (travelled + 1 + manhattan(neighbor, target), neighbor, travelled + 1)
        if (neighbor, travelled + 1) not in visited:
            heappush(heap, vals)
        visited.add((neighbor, travelled + 1))