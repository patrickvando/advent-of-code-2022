filename = "day21_input.txt"
file = open(filename, 'r')
lines = file.readlines()
graph = {}

class Node:
    def __init__(self, line, graph):
        line = "".join(line.split()) 
        self.name, expression = line.split(":")
        self.on_human_path = False
        if expression.isnumeric():
            self.evaluate = lambda: int(expression)
            self.left, self.right = None, None
        else:
            self.evaluated = False
            self.value = None
            if '+' in expression:
                self.left, self.right = expression.split("+")
                self.evaluate = lambda: graph[self.left].evaluate() + graph[self.right].evaluate()
                self.expect_left = lambda expected: graph[self.left].expect(expected - graph[self.right].evaluate(), graph)
                self.expect_right = lambda expected: graph[self.right].expect(expected - graph[self.left].evaluate(), graph)
            elif '-' in expression:
                self.left, self.right = expression.split("-")
                self.evaluate = lambda: graph[self.left].evaluate() - graph[self.right].evaluate()
                self.expect_left = lambda expected: graph[self.left].expect(expected + graph[self.right].evaluate(), graph)
                self.expect_right = lambda expected: graph[self.right].expect(graph[self.left].evaluate() - expected, graph)
            elif '*' in expression:
                self.left, self.right = expression.split("*")
                self.evaluate = lambda: graph[self.left].evaluate() * graph[self.right].evaluate()
                self.expect_left = lambda expected: graph[self.left].expect(int(expected / graph[self.right].evaluate()), graph)
                self.expect_right = lambda expected: graph[self.right].expect(int(expected / graph[self.left].evaluate()), graph)
            elif '/' in expression:
                self.left, self.right = expression.split("/")
                self.evaluate = lambda: int(graph[self.left].evaluate() / graph[self.right].evaluate())
                self.expect_left = lambda expected: graph[self.left].expect(expected * graph[self.right].evaluate(), graph)
                self.expect_right = lambda expected: graph[self.right].expect(int(graph[self.left].evaluate() / expected), graph)
   
    def expect(self, expected_val, graph):
        if self.name == "humn":
            return expected_val
        elif self.name == "root":
            if graph[self.left].on_human_path:
                return graph[self.left].expect(graph[self.right].evaluate(), graph)
            else:
                return graph[self.right].expect(graph[self.left].evaluate(), graph)
        else:
            if graph[self.left].on_human_path:
                return self.expect_left(expected_val)
            else:
                return self.expect_right(expected_val)

for line in lines:
    n = Node(line, graph)
    graph[n.name] = n

def mark_on_human_path(current_name, graph):
    if not current_name:
        return False 
    current = graph[current_name]
    if current.name == "humn":
        current.on_human_path = True
        return True
    left = mark_on_human_path(current.left, graph)
    right = mark_on_human_path(current.right, graph)
    if left or right:
        current.on_human_path = True
    return current.on_human_path

mark_on_human_path("root", graph)
print(graph["root"].expect(None, graph))