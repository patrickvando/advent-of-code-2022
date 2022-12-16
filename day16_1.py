from collections import defaultdict, deque
from heapq import heappop, heappush 


filename = "day16_input.txt"
file = open(filename, 'r')
lines = file.readlines()

graph = {}
costs = {}
def parse_line(line):
    line = line.strip().replace("Valve ", "")
    valve = line[:2]
    line = line[2:].replace(" has flow rate=", "")
    flow_rate, line = line.split(";")
    line = line.replace(" tunnels lead to valves ", "")
    line = line.replace(" tunnel leads to valve ", "")
    neighbors = line.split(", ")
    costs[valve] = int(flow_rate)
    graph[valve] = neighbors

def shortest_paths(start):
    shortest = {}
    queue = deque([(start, 0)])
    while queue:
        current, dist = queue.popleft() 
        shortest[current] = dist
        for neighbor in graph[current]:
            if neighbor not in shortest:
                queue.append((neighbor, dist + 1))
    return shortest 


for line in lines:
    parse_line(line)

node_to_shortest = {}
for node in graph:
    node_to_shortest[node] = shortest_paths(node)

activated_bit = 0
bit_memo = {}
for valve in graph:
    bit_memo[valve] = 2 ** activated_bit
    activated_bit += 1

total_minutes = 30
table = defaultdict(list)
table[("AA", 0)] = [(0, 0)]
for min in range(total_minutes):
    for node in graph:
        best = (float("-inf"), 0)
        shortest = node_to_shortest[node]
        for prev_node in graph:
            prev_mins = shortest[prev_node] + 1
            for flow, bits in table[(prev_node, min - prev_mins)]:
                if (bits & bit_memo[node]) == 0:
                    #print("here", prev_node, node, flow, (total_minutes - min) * costs[node],  (flow + (total_minutes - min) * costs[node]))
                    best = max(best, (flow + (total_minutes - min) * costs[node], bits | bit_memo[node]))
                else:
                    best = max(best, (flow, bits))
        table[(node, min)].append(best)
print(table)
best = (float("-inf"), 0)
for node in graph:
    for flow, bits in table[(node, total_minutes - 1)]:
        best = max(best, (flow, bits))
best_flow, best_bits = best
print(best_flow, bin(best_bits))