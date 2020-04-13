from queue import *
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdges(self, u, vertices):
        self.graph[u].extend(vertices)


g = Graph()
g.addEdges('A', ['B', 'C', 'D'])
g.addEdges('B', ['A', 'C'])
g.addEdges('C', ['B', 'D'])
g.addEdges('D', ['A', 'E'])
g.addEdges('E', ['D', 'F', 'G'])
g.addEdges('F', ['E'])
g.addEdges('G', ['E'])


def make_graph_copy(g):
    g_clone = Graph()
    q = Queue()
    visited = {x: False for x in g.graph}
    q.put(next(iter(g.graph)))

    while not q.empty():
        c = q.get()

        for edge in g.graph[c]:
            g_clone.addEdges(c, [edge])

            if visited[edge]:
                continue

            visited[edge] = True
            q.put(edge)

    return g_clone


# print(make_graph_copy(g))


def make_dfs(g):
    n = next(iter(g.graph))
    visited = {x: False for x in g.graph}
    return helper_dfs(n, visited, g)


def helper_dfs(n, visited, g):
    if not visited[n]:
        visited[n] = True
        print(n)

        for edge in g.graph[n]:
            helper_dfs(edge, visited, g)


# print(make_dfs(g))

g2 = {
    'A': [
        {
            'n': 'B',
            'dist': 1,
        },
        {
            'n': 'C',
            'dist': 2,
        },
    ],
    'B': [
        {
            'n': 'A',
            'dist': 1,
        },
        {
            'n': 'C',
            'dist': 1,
        },
        {
            'n': 'D',
            'dist': 4,
        },
    ],
    'C': [
        {
            'n': 'A',
            'dist': 2,
        },
        {
            'n': 'B',
            'dist': 1,
        },
        {
            'n': 'F',
            'dist': 3,
        },
    ],
    'D': [
        {
            'n': 'B',
            'dist': 4,
        },
        {
            'n': 'E',
            'dist': 2,
        },
        {
            'n': 'G',
            'dist': 2,
        },
    ],
    'E': [
        {
            'n': 'D',
            'dist': 2,
        },
        {
            'n': 'F',
            'dist': 2,
        },
        {
            'n': 'G',
            'dist': 1,
        },
    ],
    'F': [
        {
            'n': 'C',
            'dist': 3,
        },
        {
            'n': 'E',
            'dist': 3,
        },
        {
            'n': 'G',
            'dist': 5,
        },
    ],
    'G': [
        {
            'n': 'D',
            'dist': 2,
        },
        {
            'n': 'E',
            'dist': 1,
        },
        {
            'n': 'F',
            'dist': 5,
        }
    ]
}


def shortest_path(g1, source, target):
    shortestTable = {x: float('inf') for x in g1}
    shortestTable[source] = 0
    visited = []
    c = source
    s = []

    while len(visited) < len(g1):
        bestDistance = float('inf')
        nextNode = None

        for edge in g1[c]:
            distance = shortestTable[c] + edge['dist']

            if distance < shortestTable[edge['n']]:
                shortestTable[edge['n']] = distance

            if edge['n'] in visited:
                continue

            if distance < bestDistance:
                bestDistance = distance
                nextNode = edge['n']

        if nextNode is None:
            nextNode = s.pop()

        if c not in visited:
            visited.append(c)
            s.append(c)

        c = nextNode

    return f"Best distance from {source} to {target} is {shortestTable[target]}"


print(shortest_path(g2, 'A', 'F'))
