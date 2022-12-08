from collections import defaultdict

filename = "day8_input.txt"
file = open(filename, 'r')
lines = file.readlines()
grid = [[int(c) for c in row.strip()] for row in lines]
visible = [[False for k in range(len(row))] for row in grid]

def calc_view(lst, should_reverse=False):
    res = [False] * len(lst)
    max_ = float("-inf")
    rang = range(len(lst))
    if should_reverse:
        rang = reversed(rang)
    for k in rang:
        if lst[k] > max_:
            res[k] = True
        max_ = max(max_, lst[k])
    return res

for r in range(len(grid)):
    view_left = calc_view(grid[r])
    view_right = calc_view(grid[r], True)
    for c in range(len(grid[0])):
        visible[r][c] = view_left[c] or view_right[c]
for c in range(len(grid[0])):
    col = [grid[r][c] for r in range(len(grid))]
    view_up = calc_view(col)
    view_down = calc_view(col, True)
    for r in range(len(grid)):
        visible[r][c] = visible[r][c] or view_up[r] or view_down[r]
    
print(sum([sum(row) for row in visible]))
    
