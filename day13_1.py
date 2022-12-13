filename = "day13_input.txt"
file = open(filename, 'r')
lines = file.readlines()

def parse_list(line):
    line = line.strip()
    stack = [[]]
    current = None
    for k in range(len(line)):
        c = line[k]
        current = stack[-1]
        if c == '[':
            next_ = []
            current.append(next_)
            stack.append(next_)
        elif c == ']':
            stack.pop()
        elif c.isnumeric():
            current_num = c
            while line[k + 1].isnumeric():
                k += 1
                current_num += line[k]
            current.append(int(current_num))
    return stack[-1] 

correct = "correct"
unknown = "unknown"
incorrect = "incorrect"
def compare(left, right, left_ind, right_ind):
    if left_ind == len(left) and right_ind == len(right):
        return unknown 
    elif left_ind == len(left):
        return correct
    elif right_ind == len(right):
        return incorrect

    l = left[left_ind]
    r = right[right_ind]
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return "correct" 
        elif l > r:
            return "incorrect"
        else:
            return compare(left, right, left_ind + 1, right_ind + 1)
    elif isinstance(l, list) and isinstance(r, list):
        inner = compare(l, r, 0, 0)
        if inner == correct:
            return correct
        elif inner == incorrect:
            return incorrect
        else:
            return compare(left, right, left_ind + 1, right_ind + 1)
    elif isinstance(l, int):
        left[left_ind] = [left[left_ind]]
        return compare(left, right, left_ind, right_ind)
    elif isinstance(r, int):
        right[right_ind] = [right[right_ind]]
        return compare(left, right, left_ind, right_ind)
    else:
        print("error")



res = 0
for k in range(0, len(lines), 3):
    left = parse_list(lines[k])
    right = parse_list(lines[k + 1]) 
    if compare(left, right, 0, 0) == correct:
        res += (k // 3) + 1
print(res)