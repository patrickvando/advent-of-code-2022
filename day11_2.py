from collections import defaultdict
import re

filename = "day11_input.txt"
file = open(filename, 'r')
lines = file.readlines()

class Monkey:
    def __init__(self, lines):
        self.number = int(lines[0].strip().replace("Monkey ", '').replace(":", ''))
        self.items = [int(item) for item in lines[1].strip().replace("Starting items: ", '').split(", ")]
        self.next_items = []
        self.inspected = 0
        self.operation = self.parse_operation(lines[2])
        self.test = self.parse_test(lines[3])
        self.test_true = int(lines[4].strip().replace("If true: throw to monkey ", ''))
        self.test_false = int(lines[5].strip().replace("If false: throw to monkey ", ''))

    def parse_operation(self, line):
        line = line.strip().replace("Operation: ", '')
        if line == "new = old * old":
            return lambda x: x * x
        elif line.replace("new = old * ", '') != line:
            num = int(line.replace("new = old * ", ''))
            return lambda x: x * num
        elif line.replace("new = old + ", '') != line:
            num = int(line.replace("new = old + ", ''))
            return lambda x: x + num
        else:
            print("error unrecognized")
    
    def parse_test(self, line):
        num = int(line.strip().replace("Test: divisible by ", ''))
        self.test_num = num
        return lambda x: x % num == 0 

    def __str__(self):
        return f"MONKEY\nnumber: {self.number}\nitems: {self.items}\nnext_items: {self.next_items}\noperation: {self.operation}\ntest: {self.test}\ntest_true: {self.test_true}\ntest_false: {self.test_false}"

monkeys = {}
for k in range(0, len(lines), 7):
    mon = Monkey(lines[k:k + 6])
    monkeys[mon.number] = mon


def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)

div = monkeys[0].test_num
num = 1
for mon in monkeys:
    num *= monkeys[mon].test_num
    div = gcd(div, monkeys[mon].test_num)
gcd_num = num // div
print(gcd_num)

def process_items(monkey):
    for item in monkey.items:
        item = monkey.operation(item)
        monkey.inspected += 1
        item %= gcd_num
        if monkey.test(item):
            monkeys[monkey.test_true].items.append(item)
        else:
            monkeys[monkey.test_false].items.append(item)
    monkey.items = []

for k in range(10000):
    for mon in range(len(monkeys)):
        process_items(monkeys[mon])

inspected = [monkeys[mon].inspected for mon in monkeys]
max_ = max(inspected)
max_2 = max(inspected, key = lambda x: float("-inf") if x == max_ else x)
print(max_ * max_2)