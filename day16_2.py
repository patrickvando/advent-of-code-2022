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
    graph[valve] = neighbors + [valve]

for line in lines:
    parse_line(line)

activated_bit = 0
bit_memo = {}
reverse = {}
for valve in graph:
    bit_memo[valve] = 2 ** activated_bit
    reverse[activated_bit] = valve
    activated_bit += 1

def check_valves(bits):
    total = 0
    on = []
    for activated_bit in range(len(graph)):
        if bits & (2 ** activated_bit):
            on.append(reverse[activated_bit])
            total += costs[reverse[activated_bit]]
    print(",".join(on))
    print(total)

total_minutes = 26 
table = defaultdict(lambda: defaultdict(int))
table[("AA", "AA", 0)] = {0: 0}
for minute in range(total_minutes):
    print(minute)
    for human_node in graph:
        for elephant_node in graph:
            for next_human_node in graph[human_node]:
                for next_elephant_node in graph[elephant_node]:
                    if (human_node == next_human_node and costs[next_human_node] == 0) or (elephant_node == next_elephant_node and costs[next_elephant_node] == 0):
                        continue
                    for bits, flow in table[(human_node, elephant_node, minute)].items():
                        if not (bits & bit_memo[human_node]) and next_human_node == human_node:
                            bits = bits | bit_memo[human_node]
                            flow += (total_minutes - (minute + 1)) * costs[human_node] 
                        if not (bits & bit_memo[elephant_node]) and next_elephant_node == elephant_node:
                            bits = bits | bit_memo[elephant_node]
                            flow += (total_minutes - (minute + 1)) * costs[elephant_node] 
                        table[(next_human_node, next_elephant_node, minute + 1)][bits] = max(table[(next_human_node, next_elephant_node, minute + 1)][bits], flow)


best = (float("-inf"), 0)
for human_node in graph:
    for elephant_node in graph:
        flow = max(table[(human_node, elephant_node, total_minutes - 1)].values())
        best = max(best, (flow, bits))
best_flow, best_bits = best
check_valves(best_bits)
print(best_flow)