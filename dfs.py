g = {
    0: [1, 2],
    1: [0, 4],
    2: [0, 3],
    3: [2, 5],
    4: [1, 5, 6],
    5: [3, 4],
    6: [4, 7],
    7: [6],
}

visited = [False for x in g]


def dfs(at):
    if visited[at]:
        return

    visited[at] = True

    print(at)

    neighbours = g[at]
    for n in neighbours:
        dfs(n)


start_node = 0
dfs(start_node)
