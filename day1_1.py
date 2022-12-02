filename = "day1_input.txt"
with open(filename, 'r') as f:
    elves = []
    current = 0
    for line in f:
        if line.strip() == "":
            elves.append(current)
            current = 0
        else:
            current += int(line)
    elves.append(current)
    print(max(elves))