filename = "day3_input.txt"

scores = {}
for k in range(26):
    scores[chr(ord('a') + k)] = k + 1
    scores[chr(ord('A') + k)] = k + 27
with open(filename, 'r') as f:
    score = 0
    bags = []
    for line in f:
        bag = line.strip()
        bags.append(set(bag))
        if len(bags) == 3:
            badge = bags[0].intersection(bags[1]).intersection(bags[2])
            score += scores[badge.pop()]
            bags = []
    print(score) 
