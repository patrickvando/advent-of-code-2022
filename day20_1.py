import math
from sortedcontainers import SortedList

filename = "day20_input.txt"
file = open(filename, 'r')
lines = file.readlines()

nums = []
for line in lines:
    nums.append(int(line.strip()))

def check_ranks(ranked):
    print(",".join([str(rank_to_num[rank]) for rank in ranked]))

ranked = SortedList()
num_to_rank = {}
rank_to_num = {}

for k in range(len(nums)):
    rank_with_space = k * (2 ** len(nums))
    ranked.add(rank_with_space)
    num_to_rank[nums[k]] = rank_with_space
    rank_to_num[rank_with_space] = nums[k]

for k in range(len(nums)):
    #check_ranks(ranked)
    current_pos = ranked.index(num_to_rank[nums[k]])
    current_rank = ranked[current_pos]
    move = nums[k]
    if move == 0:
        continue
    if move >= 0:
        target_rank = ranked[(current_pos + move) % len(nums)]
    else:
        target_rank = ranked[(current_pos + move - 1) % len(nums)]

    updated_rank = target_rank + 2 ** (len(nums) - k - 1) 
    if move == 0:
        print(bin(target_rank), bin(current_rank), bin(updated_rank), [bin(r) for r in ranked])
    ranked.remove(current_rank)
    ranked.add(updated_rank)
    rank_to_num.pop(current_rank)
    num_to_rank[nums[k]] = updated_rank
    rank_to_num[updated_rank] = nums[k]
check_ranks(ranked)

offset = ranked.index(num_to_rank[0])
a = rank_to_num[ranked[(offset + 1000) % len(ranked)]]
b = rank_to_num[ranked[(offset + 2000) % len(ranked)]]
c = rank_to_num[ranked[(offset + 3000) % len(ranked)]]
print(a, b, c)
print(a + b + c)