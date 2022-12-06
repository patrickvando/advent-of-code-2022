from collections import defaultdict

filename = "day6_input.txt"

with open(filename, 'r') as f:
    stacks = []
    st = ""
    for line in f:
        st += line
    seen = defaultdict(int) 
    for k in range(len(st)):
        seen[st[k]] += 1
        if k >= 14:
            seen[st[k - 14]] -= 1
            if seen[st[k - 14]] == 0:
                seen.pop(st[k - 14])
        if len(seen) == 14:
            break
    print(k + 1)
