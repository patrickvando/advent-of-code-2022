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
reverse = {}
for valve in graph:
    bit_memo[valve] = 2 ** activated_bit
    reverse[activated_bit] = valve
    activated_bit += 1

def check_valves(bits):
    total = 0
    for activated_bit in range(len(graph)):
        if bits & (2 ** activated_bit):
            total += costs[reverse[activated_bit]]
    print(total)

total_minutes = 26
table = defaultdict(list)
table[("AA", 0, "AA", 0, 0)] = [(0, 0)]
table[("AA", 1, "AA", 1, 0)] = [(0, 0)]
for minute in range(total_minutes):
    print(minute)
    for human_node in graph:
        for elephant_node in graph:
            for human_opening in [0, 1]:
                for elephant_opening in [0, 1]:
                    best = (float("-inf"), 0)
                    shortest_human = node_to_shortest[human_node]
                    shortest_elephant = node_to_shortest[elephant_node]
                    for prev_human_node in graph:
                        for prev_elephant_node in graph:
                            for prev_human_opening in [0, 1]:
                                for prev_elephant_opening in [0, 1]:
                                    prev_mins = max(shortest_human[prev_human_node] + human_opening, shortest_elephant[prev_elephant_node] + elephant_opening)
                                    for flow, bits in table[(prev_human_node, prev_human_opening, prev_elephant_node, prev_elephant_opening, minute - prev_mins)]:
                                        total_flow = flow
                                        if (bits & bit_memo[human_node]) == 0 and human_opening:
                                            bits = bits | bit_memo[human_node]
                                            total_flow += (total_minutes - minute) * costs[human_node] 
                                        if (bits & bit_memo[elephant_node]) == 0 and elephant_opening:
                                            bits = bits | bit_memo[elephant_node]
                                            total_flow += (total_minutes - minute) * costs[elephant_node] 
                                        #print("here", prev_human_node, prev_elephant_node, human_node, elephant_node, total_flow)
                                        best = max(best, (total_flow, bits))
                    table[(human_node, human_opening, elephant_node, elephant_opening, minute)].append(best)
best = (float("-inf"), 0)
for human_node in graph:
    for elephant_node in graph:
        for human_opening in [0, 1]:
            for elephant_opening in [0, 1]:
                for flow, bits in table[(human_node, human_opening, elephant_node, elephant_opening, total_minutes - 1)]:
                    best = max(best, (flow, bits))
best_flow, best_bits = best
print(best_flow, bin(best_bits))
print(check_valves(best_bits))