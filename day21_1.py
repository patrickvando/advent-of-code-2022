filename = "day21_input.txt"
file = open(filename, 'r')
lines = file.readlines()
graph = {}

class Node:
    def __init__(self, line, graph):
        line = "".join(line.split()) 
        self.name, expression = line.split(":")
        if expression.isnumeric():
            self.evaluate = lambda: int(expression)
        else:
            self.evaluated = False
            self.value = None
            if '+' in expression:
                left, right = expression.split("+")
                self.evaluate = lambda: graph[left].evaluate() + graph[right].evaluate()
            elif '-' in expression:
                left, right = expression.split("-")
                self.evaluate = lambda: graph[left].evaluate() - graph[right].evaluate()
            elif '*' in expression:
                left, right = expression.split("*")
                self.evaluate = lambda: graph[left].evaluate() * graph[right].evaluate()
            elif '/' in expression:
                left, right = expression.split("/")
                self.evaluate = lambda: int(graph[left].evaluate() / graph[right].evaluate())

for line in lines:
    n = Node(line, graph)
    graph[n.name] = n

print(graph["root"].evaluate())