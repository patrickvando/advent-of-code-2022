filename = "day14_input.txt"
file = open(filename, 'r')
lines = file.readlines()

rock = set([]) 
for line in lines:
    points = [[int(num) for num in item.split(",")] for item in "".join(line.split()).split("->")]
    for k in range(1, len(points)):
        px, py = points[k - 1]
        cx, cy = points[k]
        if px == cx:
            if py > cy:
                py, cy = cy, py
            for y in range(py, cy + 1):
                rock.add((y, cx)) 
        if py == cy:
            if px > cx:
                px, cx = cx, px
            for x in range(px, cx + 1):
                rock.add((cy, x))


rock_y = [item[0] for item in rock]
max_y = max(rock_y)

def simulate(y, x):
    if y == 1 + max_y:
        rock.add((y, x)) 
    elif (y + 1, x) not in rock:
        return simulate(y + 1, x)
    elif (y + 1, x - 1) not in rock:
        return simulate(y + 1, x - 1)
    elif (y + 1, x + 1) not in rock:
        return simulate(y + 1, x + 1)
    else:
        rock.add((y, x))

counter = 0
while((0, 500) not in rock):
    simulate(0, 500)
    counter += 1
print(counter)