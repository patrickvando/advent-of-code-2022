

loses = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}
wins = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}
scoring = {
   'A': 1,
   'B': 2,
   'C': 3,
}

def star2(filename):
    with open(filename, 'r') as f:
        score = 0
        for line in f:
            opponent, you = line.strip().split(" ")
            if you == 'X':
                score += scoring[wins[opponent]] 
            elif you == 'Y':
                score += scoring[opponent] + 3
            elif you == 'Z':
                score += scoring[loses[opponent]] + 6
        return score

filename = "day2_input.txt"
print(star2(filename))