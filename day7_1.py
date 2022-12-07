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

def dfs(current):
    cumulative = 0
    total = 0
    for item in current:
        if item == "..":
            continue
        if isinstance(current[item], dict):
            t, c = dfs(current[item])
            cumulative += c
            total += t
        else:
            total += current[item]
    if total <= 100000:
        cumulative += total
    return total, cumulative
print(dfs(home))
    
