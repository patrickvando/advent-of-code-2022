filename = "day18_input.txt"
file = open(filename, 'r')
lines = file.readlines()
blocks = set([])
for line in lines:
    [x, y, z] = [int(c) for c in line.strip().split(",")]
    blocks.add((x, y, z))

x_only = [x for x, y, z in blocks]
y_only = [y for x, y, z in blocks]
z_only = [z for x, y, z in blocks]

min_x, max_x = min(x_only), max(x_only)
min_y, max_y = min(y_only), max(y_only)
min_z, max_z = min(z_only), max(z_only)

neighbors = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def check_valid(x, y, z):
    if x >= min_x - 1 and x <= max_x + 1 and y >= min_y - 1 and y <= max_y + 1 and z >= min_z - 1 and z <= max_z + 1:
        return True
    return False

total = 0
stack = [(min_x - 1, min_y - 1, min_z - 1)]
visited = set([])
while stack:
    x, y, z = stack.pop()
    for dx, dy, dz in neighbors:
        nx, ny, nz = x + dx, y + dy, z + dz
        if (nx, ny, nz) in blocks:
            total += 1
        elif (nx, ny, nz) not in visited and x >= min_x - 1 and x <= max_x + 1 and\
            y >= min_y - 1 and y <= max_y + 1 and\
                z >= min_z - 1 and z <= max_z + 1:
            visited.add((nx, ny, nz))
            stack.append((nx, ny, nz))
print(total)