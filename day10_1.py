from collections import defaultdict

filename = "day10_input.txt"
file = open(filename, 'r')
lines = file.readlines()
target = 20
register = 1
buffer = 0
k = 0
signal = 0
delay = 0
pixels = ['.'] * 240
def visualize_sprite(ind):
    pixels = ['.'] * 40
    pixels[ind - 1: ind + 2] = '#' * 3
    print(''.join(pixels))
for clock in range(1, 241):
    if delay == 0 and k < len(lines):
        line = lines[k].strip()
        k += 1
        if line != 'noop':
            _, val = line.split()
            buffer = int(val)
            delay = 2
        else:
            delay = 1
    delay -= 1
    #visualize_sprite(register)
    if register - 1 <= (clock - 1) % 40 and (clock - 1) % 40 <= register + 1:
        pixels[clock - 1] = '#'
    if delay == 0:
        register += buffer
        buffer = 0
for k in range(6):
    print("".join(pixels[k * 40: (k + 1) * 40]))

    
