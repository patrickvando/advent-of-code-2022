from collections import defaultdict

filename = "day8_input.txt"
file = open(filename, 'r')
lines = file.readlines()
grid = [[int(c) for c in row.strip()] for row in lines]
visible = [[1 for k in range(len(row))] for row in grid]

def calc_view(lst, should_reverse=False):
    res = [0] * len(lst)
    stack = []
    rang = range(len(lst))
    if should_reverse:
        rang = reversed(rang)
    for k in rang:
        while stack and lst[k] > lst[stack[-1]]:
            stack.pop()
        if stack:
            res[k] = abs(k - stack[-1])
        elif should_reverse:
            res[k] = len(lst) - 1 - k
        else:
            res[k] = k
        stack.append(k)
    return res

for r in range(len(grid)):
    view_left = calc_view(grid[r])
    view_right = calc_view(grid[r], True)
    for c in range(len(grid[0])):
        visible[r][c] *= view_left[c] * view_right[c]
for c in range(len(grid[0])):
    col = [grid[r][c] for r in range(len(grid))]
    view_up = calc_view(col)
    view_down = calc_view(col, True)
    for r in range(len(grid)):
        visible[r][c] *= view_up[r] * view_down[r]
    
print(max([max(row) for row in visible]))

    
