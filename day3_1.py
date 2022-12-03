filename = "day3_input.txt"

scores = {}
for k in range(26):
    scores[chr(ord('a') + k)] = k + 1
    scores[chr(ord('A') + k)] = k + 27
with open(filename, 'r') as f:
    score = 0
    for line in f:
        bags = line.strip()
        bag1, bag2 = bags[:len(bags) // 2], bags[len(bags) // 2:]
        bag1 = set(bag1)
        bag2 = set(bag2)
        for letter in bag1.intersection(bag2):
            score += scores[letter] 
    print(score) 
