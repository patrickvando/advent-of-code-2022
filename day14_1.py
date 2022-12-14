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
rock_x = [item[1] for item in rock]

max_y = max(rock_y)
max_x = max(rock_x)
min_y = min(rock_y)
min_x = min(rock_x)

def simulate(y, x):
    if y == max_y:
        return False 
    if (y + 1, x) not in rock:
        return simulate(y + 1, x)
    if x == 0:
        return False 
    if (y + 1, x - 1) not in rock:
        return simulate(y + 1, x - 1)
    if x == max_x:
        return False 
    if (y + 1, x + 1) not in rock:
        return simulate(y + 1, x + 1)
    rock.add((y, x))
    return True 

counter = 0
while(simulate(0, 500)):
    counter += 1
print(counter)