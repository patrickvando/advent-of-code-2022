filename = "day5_input.txt"

def get_letter(st):
    res = ""
    for c in st:
        if c.isalpha():
            res += c
    return res
with open(filename, 'r') as f:
    stacks = []
    for line in f:
        if line.strip()[0] != "[":
            break
        for k in range(0, len(line), 4):
            if k // 4 >= len(stacks):
                stacks.append([])
            box = line[k:k + 4].strip()
            if box:
                stacks[k // 4].append(get_letter(box))
    stacks = [stack[::-1] for stack in stacks]
    for line in f:
        if line[:4] != 'move':
            continue
        num_boxes, from_, to = [int(num) for num in line.split() if num.isnumeric()]
        from_ -= 1
        to -= 1

        stacks[to] = stacks[to] + stacks[from_][len(stacks[from_]) - num_boxes:]
        stacks[from_] = stacks[from_][:len(stacks[from_]) - num_boxes]
    res = ""
    for stack in stacks:
        if stack:
            res += stack[-1]
        else:
            res += " "
    print(res)
