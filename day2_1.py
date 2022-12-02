

loses = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}
ties = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}
scoring = {
   'X': 1,
   'Y': 2,
   'Z': 3,
}

def star1(filename):
    with open(filename, 'r') as f:
        score = 0
        for line in f:
            opponent, you = line.strip().split(" ")
            score += scoring[you]
            if loses[opponent] == you:
                score += 6
            elif ties[opponent] == you:
                score += 3
        return score

filename = "day2_input.txt"
print(star1(filename))