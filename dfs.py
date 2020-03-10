from graphics import *

g = {
    0: [1, 2, 3],
    1: [0, 4, 5],
    2: [0, 6],
    3: [0],
    4: [1],
    5: [1],
    6: [2],
}

visited = [False for x in g]


def dfs_recursive(node):
    if visited[node]:
        return

    print(node)
    visited[node] = True
    neighbours = g[node]

    for neighbour in neighbours:
        dfs_recursive(neighbour)


dfs_recursive(0)
