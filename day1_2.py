from heapq import heappush, heappop

def heap3push(heap, num):
    heappush(heap, num)
    if len(heap) > 3:
        heappop(heap)

filename = "day1_input.txt"
with open(filename, 'r') as f:
    elves = [] 
    current = 0
    for line in f:
        if line.strip() == "":
            heap3push(elves, current)
            current = 0
        else:
            current += int(line)
    heap3push(elves, current)
    print(sum(elves))





    