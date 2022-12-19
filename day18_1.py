filename = "day18_input.txt"
file = open(filename, 'r')
lines = file.readlines()
blocks = set([])
for line in lines:
    [x, y, z] = [int(c) for c in line.strip().split(",")]
    blocks.add((x, y, z))

neighbors = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
surface_area = 0
for x, y, z in blocks:
    for dx, dy, dz in neighbors:
        nx, ny, nz = x + dx, y + dy, z + dz
        if (nx, ny, nz) not in blocks:
            surface_area += 1
print(surface_area)
