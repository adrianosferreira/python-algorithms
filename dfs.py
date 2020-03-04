class Node:

    def __init__(self, value):
        self.edges = []
        self.value = value
        self.visited = False

    def add_edge(self, val):
        self.edges.append(Node(val))


node = Node(1)
node.add_edge(2)
node.add_edge(3)
node.edges[0].add_edge(4)
node.edges[0].add_edge(5)
node.edges[0].edges[1].add_edge(10)


def dfs(tree):
    s = [tree]
    c = tree

    while c:

        if len(s) == 0:
            break

        c = s.pop()

        print(c.value)

        for edge in c.edges:
            if edge.visited:
                continue

            edge.visited = True
            s.append(edge)


print(dfs(node))
