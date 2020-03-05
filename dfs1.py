graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3],
    5: [6],
    6: [5, 7],
    7: [6, 8],
    8: []
}


def dfs(at, count, visited, components):
    visited[at] = True
    components.insert(at, count)

    for next in graph[at]:
        if not visited[next]:
            dfs(next, count, visited, components)


def find_components():
    visited = [False for x in graph]
    components = []
    count = 0
    for x in graph:
        if not visited[x]:
            count += 1
            dfs(x, count, visited, components)

    return count


print(find_components())
