g = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3],
    5: [6],
    6: [5, 7],
    7: [6, 8],
    8: [7]
}


def dfs_recursive(node, category, components, visited):
    if visited[node]:
        return

    visited[node] = True
    components[node] = category
    neighbours = g[node]

    for neighbour in neighbours:
        dfs_recursive(neighbour, category, components, visited)


def graph_components():
    components = {}
    category = 0
    visited = [False for x in g]

    for node in g:
        if visited[node]:
            continue

        category += 1
        dfs_recursive(node, category, components, visited)

    return components


graph_components()
