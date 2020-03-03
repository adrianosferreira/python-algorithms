class Node:

    def __init__(self, value):
        self.edges = []
        self.value = value

    def add_edge(self, val):
        self.edges.append(Node(val))


node = Node(1)
node.add_edge(2)
node.add_edge(3)
node.edges[0].add_edge(4)
node.edges[0].add_edge(5)
node.edges[1].add_edge(10)
node.edges[1].add_edge(11)


def bfs(tree, k):

    stack = [tree]

    while stack:
        current = stack.pop()

        if current.value == k:
            return True

        for edge in current.edges:
            stack.append(edge)

    return False


print(bfs(node, 12))
