

from collections import defaultdict
import sys


filename = "day22_input.txt"
EDGE_LENGTH = 50 

with open(filename) as f:
    lines = f.readlines()
lines = [line.rstrip() for line in lines]

# ----------------------------- PARSE THE PATH
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

# ----------------------------- PARSE THE FACES
def rotate(grid):
    grid = [row[:] for row in grid] 
    for y in range(EDGE_LENGTH):
        for x in range(EDGE_LENGTH // 2):
            grid[y][x], grid[y][EDGE_LENGTH - 1 - x] = grid[y][EDGE_LENGTH - 1 - x], grid[y][x]
    for y in range(EDGE_LENGTH):
        for x in range(EDGE_LENGTH - y):
            grid[y][x], grid[EDGE_LENGTH - 1 - x][EDGE_LENGTH - 1 - y] = grid[EDGE_LENGTH - 1 - x][EDGE_LENGTH - 1 - y], grid[y][x]
    return grid

class face:
    def __init__(self):
        self.grid = [[None for c in range(EDGE_LENGTH)] for r in range(EDGE_LENGTH)]
        self.orientation = None
        self.label = None
        self.face_coords = None
        self.original_orientation = None

    def orient(self, prev_dir, prev_label):
        turns = 0
        while self.orientation[invert_dir(prev_dir)] != prev_label:
            self.orientation = [self.orientation[-1]] + self.orientation[:-1]
            self.grid = rotate(self.grid)
            turns += 1
        return turns

    def display(self):
        for row in self.grid:
            print("".join(row))

start_pos = (None, None)
start_face = (None, None)
unlabelled_faces = defaultdict(lambda: face())
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == ".":
            if start_pos == (None, None):
                start_pos = (r % EDGE_LENGTH, c % EDGE_LENGTH)
                start_face = (r // EDGE_LENGTH, c // EDGE_LENGTH)
        if lines[r][c] in ".#":
            unlabelled_faces[(r // EDGE_LENGTH, c // EDGE_LENGTH)].grid[r % EDGE_LENGTH][c % EDGE_LENGTH] = lines[r][c]
            unlabelled_faces[(r // EDGE_LENGTH, c // EDGE_LENGTH)].face_coords = (r // EDGE_LENGTH, c // EDGE_LENGTH)            

orientations = {
    'A': ['D', 'F', 'C', 'E'],
    'B': ['D', 'E', 'C', 'F'],
    'C': ['A', 'F', 'B', 'E'],
    'D': ['B', 'F', 'A', 'E'],
    'E': ['D', 'A', 'C', 'B'],
    'F': ['D', 'B', 'C', 'A'],
}

dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
def invert_dir(dir):
    return (dir + 2) % 4

def rotate_orientation(label, prev_dir, prev_label):
    neighboring = orientations[label]
    while neighboring[invert_dir(prev_dir)] != prev_label:
        neighboring = [neighboring[-1]] + neighboring[:-1]
    return neighboring 

def map_neighbors(face, prev_dir, prev_label, seen):
    y, x = face
    current = unlabelled_faces[face]
    neighboring = orientations[current.label]
    if prev_label:
        neighboring = rotate_orientation(current.label, prev_dir, prev_label)
    current.orientation = neighboring
    current.original_orientation = neighboring[:]
    for dir in dirs:
        dy, dx = dirs[dir]
        neighbor_face = y + dy, x + dx
        if neighbor_face in seen or neighbor_face not in unlabelled_faces:
            continue
        seen.add(neighbor_face)
        neighbor = unlabelled_faces[neighbor_face]
        neighbor.label = neighboring[dir]
        map_neighbors(neighbor_face, dir, current.label, seen)

unlabelled_faces[start_face].label = 'A'
map_neighbors(start_face, None, None, set([start_face]))

labelled_faces = {}
for face in unlabelled_faces:
    labelled_faces[unlabelled_faces[face].label] = unlabelled_faces[face]

# ----------------------------- TRAVEL THE MAZE 
def move(face, pos, dir, dist):
    y, x = pos
    dy, dx = dirs[dir] 
    for k in range(dist):
        ny, nx = y + dy, x + dx
        next_face = face
        if ny == EDGE_LENGTH or nx == EDGE_LENGTH or ny < 0 or nx < 0:
            next_face = labelled_faces[face.orientation[dir]]
            next_face.orient(dir, face.label)
        if ny == EDGE_LENGTH:
            ny = 0
        elif ny == -1:
            ny = EDGE_LENGTH - 1
        elif nx == EDGE_LENGTH:
            nx = 0
        elif nx == -1:
            nx = EDGE_LENGTH - 1
        if next_face.grid[ny][nx] == "#":
            return face, (y, x)
        y, x = ny, nx
        face = next_face
    return  face, (y, x)

dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
current_dir = 0 
current_pos = start_pos 
face = labelled_faces['A']
for k in range(len(path)):
    if path[k] == 'R':
        current_dir = (current_dir + 1) % len(dirs)
    elif path[k] == 'L':
        current_dir = (current_dir - 1) % len(dirs)
    else:
        face, current_pos = move(face, current_pos, current_dir, path[k])

y, x = current_pos
face.grid[y][x] = 'x'
turns = face.orient(invert_dir(0), face.original_orientation[0])
current_dir = (current_dir + turns) % 4
face_y, face_x = face.face_coords
offset_y, offset_x = face_y * EDGE_LENGTH, face_x * EDGE_LENGTH
for y in range(EDGE_LENGTH):
    for x in range(EDGE_LENGTH):
        if face.grid[y][x] == 'x':
            print((y + offset_y + 1) * 1000 + 4 * (x + offset_x + 1) + current_dir)
            sys.exit(0)
