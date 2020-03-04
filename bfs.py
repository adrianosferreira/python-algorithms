from queue import *

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


def bfs(tree):
    q = Queue()
    q.put(tree)

    while q.empty() is False:
        current = q.get()

        print(current.value)

        for edge in current.edges:
            if edge.visited:
                continue

            q.put(edge)


print(bfs(node))
