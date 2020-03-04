from queue import *


class Node:

    def __init__(self, value):
        self.edges = []
        self.value = value
        self.visited = False

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_edges(self, edges):
        for edge in edges:
            self.edges.append(edge)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.add_edges([node2, node3])
node2.add_edges([node1, node4, node5])
node3.add_edges([node1])
node4.add_edges([node2])
node5.add_edges([node2])


def bfs(node):
    q = Queue()
    q.put(node)
    node.visited = True

    while not q.empty():
        current = q.get()

        print(current.value)

        for edge in current.edges:
            if edge.visited:
                continue

            edge.visited = True
            q.put(edge)


print(bfs(node1))
