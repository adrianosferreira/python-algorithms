from queue import *

g = {
    0: [1, 2],
    1: [0, 6],
    2: [3, 0],
    3: [2, 4, 5],
    4: [3],
    5: [3, 6],
    6: [1, 5]
}


def bfs(n):
    q = Queue()
    q.put(n)
    visited = [False for x in g]
    visited[n] = True

    while not q.empty():
        c = q.get()
        print(c)

        for edge in g[c]:
            if visited[edge]:
                continue

            visited[edge] = True
            q.put(edge)


bfs(0)
