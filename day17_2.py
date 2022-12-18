from collections import defaultdict


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

    def add_rock(self, occupied, offset_reverse, rock_num):
        for py, px in self.body:
            occupied[(py + self.offset_y, px + self.offset_x)] = rock_num
        offset_reverse[rock_num] = (self.offset_y, self.offset_x)
        return occupied


def simulate(target_fallen, dir_ind, rock_ind, fallen_rocks, bottom_most):
    while fallen_rocks < target_fallen:
        next_dir = dirs[dir_ind]
        current_rock = rocks[rock_ind]
        current_rock.offset_x += next_dir
        if not current_rock.check_rock(occupied):
            current_rock.offset_x -= next_dir
        dir_ind = (dir_ind + 1) % len(dirs)
        current_rock.offset_y += 1
        if not current_rock.check_rock(occupied):
            current_rock.offset_y -= 1
            current_rock.add_rock(occupied, offset_reverse, fallen_rocks)
            fallen_rocks += 1
            bottom_most = min(bottom_most, current_rock.offset_y)
            rock_ind = (rock_ind + 1) % len(rocks)
            rocks[rock_ind].offset_x = 2
            rocks[rock_ind].offset_y = -3 - rocks[rock_ind].height + bottom_most 
    return dir_ind, rock_ind, fallen_rocks, bottom_most 

def find_pattern(offset_reverse, fallen_rocks):
    for pattern_size in range(10, fallen_rocks // 2):
        valid = True 
        for k in range(pattern_size):
            if offset_reverse[fallen_rocks - (k + 1)][1] != offset_reverse[fallen_rocks - (k + pattern_size + 1)][1]:
                valid = False
                break
        if valid:
            return pattern_size
    return None

rocks = {}
rocks[0] = rock([(0, 0), (0, 1), (0, 2), (0, 3)], 4, 1)
rocks[1] = rock([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)], 3,  3)
rocks[2] = rock([(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)], 3, 3)
rocks[3] = rock([(0, 0), (1, 0), (2, 0), (3, 0)], 1, 4)
rocks[4] = rock([(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2) 

occupied = {}
offset_reverse = {}

fallen_rocks = 0
dir_ind = 0
rock_ind = 0
bottom_most = 0

rocks[rock_ind].offset_y = -2 - rocks[rock_ind].height 
rocks[rock_ind].offset_x = 2

initial_fallen = 10000 
dir_ind, rock_ind, fallen_rocks, prev_height = simulate(initial_fallen, dir_ind, rock_ind, fallen_rocks, bottom_most)
initial_height = prev_height
pattern_length = find_pattern(offset_reverse, fallen_rocks)

dir_ind, rock_ind, fallen_rocks, next_height = simulate(fallen_rocks + pattern_length, dir_ind, rock_ind, fallen_rocks, prev_height)
pattern_height = prev_height - next_height
prev_height = next_height

total_target = 1000000000000
pattern_repeats_height = (total_target - initial_fallen) // pattern_length * pattern_height
remainder_to_fall = (total_target - initial_fallen) % pattern_length
dir_ind, rock_ind, fallen_rocks, next_height = simulate(fallen_rocks + remainder_to_fall, dir_ind, rock_ind, fallen_rocks, prev_height)
remainder_to_fall_height = prev_height - next_height

print("Expected height", remainder_to_fall_height - initial_height + pattern_repeats_height + 1)

# occupied = {}
# offset_reverse = {}
# occupied_reverse = defaultdict(list)
# fallen_rocks = 0
# dir_ind = 0
# rock_ind = 0
# bottom_most = 0
# rocks[rock_ind].offset_y = -2 - rocks[rock_ind].height + bottom_most 
# rocks[rock_ind].offset_x = 2
# dir_ind, rock_ind, fallen_rocks, next_height = simulate(total_target, dir_ind, rock_ind, fallen_rocks, bottom_most)
# print("Actual height", -min([py for py, px in occupied]) + 1)