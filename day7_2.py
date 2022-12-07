from collections import defaultdict

filename = "day7_input.txt"
file = open(filename, 'r')
lines = file.readlines()
home = {'/': {}}
current = home 
k = 0
while k < len(lines):
    line = lines[k].strip()
    if line[0:5] == "$ cd ":
        dir = line[5:] 
        current = current[dir]
        k += 1
    elif line[0:4] == "$ ls":
        k += 1
        line = lines[k].strip()
        while line[0] != "$":
            if line[0:4] == "dir ":
                current[line[4:]] = {'..': current}
            else:
                size, file_ = line.split(" ")
                current[file_] = int(size)
            k += 1
            if k == len(lines):
                break
            line = lines[k].strip()

def sum_(current):
    total = 0
    for item in current:
        if item == "..":
            continue
        if isinstance(current[item], dict):
            total += sum_(current[item])
        else:
            total += current[item]
    return total

def find_free(current, needed_space):
    total = 0
    best = float("inf")
    for item in current:
        if item == "..":
            continue
        if isinstance(current[item], dict):
            t, b = find_free(current[item], needed_space)
            total += t
            best = min(b, best)
        else:
            total += current[item]
    if total >= needed_space:
        best = min(best, total)
    return total, best

used_space = sum_(home)
needed_space = 30000000 - (70000000 - used_space)
_, found = find_free(home, needed_space)
print(found)
    
