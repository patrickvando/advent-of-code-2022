filename = "day4_input.txt"
with open(filename, 'r') as f:
    score = 0
    for line in f:
        range1, range2 = line.strip().split(",")
        s1, e1 = [int(k) for k in range1.split("-")]
        s2, e2 = [int(k) for k in range2.split("-")]
        if s2 < s1:
            s1, e1, s2, e2 = s2, e2, s1, e1
        if e1 >= s2:
            score += 1
    print(score) 
