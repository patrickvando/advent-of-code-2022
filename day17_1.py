filename = "day17_input.txt"
file = open(filename, 'r')
line = file.readlines()[0].strip()
dirs = [-1 if c == '<' else 1 for c in line]

class rock:
    def __init__(self, body, length, height):
        self.body = body
        self.length = length
        self.height = height
        self.offset_y = float("-inf")
        self.offset_x = float("-inf") 

    def check_rock(self, occupied):
        for py, px in self.body:
            if (py + self.offset_y, px + self.offset_x) in occupied:
                return False
        if self.offset_y + (self.height - 1) > 0:
            return False
        if self.offset_x < 0 or self.offset_x + self.length > 7:
            return False
        return True

    def add_rock(self, occupied):
        for py, px in self.body:
            occupied.add((py + self.offset_y, px + self.offset_x))
        return occupied

    def __str__(self):
        res = []
        for py, px in self.body:
            res.append("({},{})".format(py + self.offset_y, px + self.offset_x))
        return ",".join(res)

def visualize(occupied):
    if not occupied:
        return ""
    tallest = min([py for py, px in occupied])
    grid = [['.' for c in range(7)] for rows in range(-tallest + 1)]
    for py, px in occupied:
        grid[py - tallest][px] = '#'
    return "\n".join("".join(row) for row in grid)
     

rocks = {}
rocks[0] = rock([(0, 0), (0, 1), (0, 2), (0, 3)], 4, 1)
rocks[1] = rock([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)], 3,  3)
rocks[2] = rock([(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)], 3, 3)
rocks[3] = rock([(0, 0), (1, 0), (2, 0), (3, 0)], 1, 4)
rocks[4] = rock([(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2) 

occupied = set([])
bottom_most = 0
dir_ind = 0
rock_ind = 0
rocks[rock_ind].offset_y = -2  - rocks[rock_ind].height
rocks[rock_ind].offset_x = 2
fallen_rocks = 0
while fallen_rocks < 3:
    next_dir = dirs[dir_ind]
    current_rock = rocks[rock_ind]
    print(visualize(current_rock.add_rock(occupied.copy())))
    current_rock.offset_x += next_dir
    if not current_rock.check_rock(occupied):
        current_rock.offset_x -= next_dir
    dir_ind = (dir_ind + 1) % len(dirs)
    current_rock.offset_y += 1
    if not current_rock.check_rock(occupied):
        current_rock.offset_y -= 1
        fallen_rocks += 1
        current_rock.add_rock(occupied)
        bottom_most = min(bottom_most, current_rock.offset_y)
        rock_ind = (rock_ind + 1) % len(rocks)
        rocks[rock_ind].offset_x = 2
        rocks[rock_ind].offset_y = -2 - rocks[rock_ind].height + bottom_most - 1

tallest = min([py for py, px in occupied])
print(-tallest + 1) 


