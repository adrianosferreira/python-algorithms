from queue import *

t = [
    's...',
    '##..',
    '#...',
    '#.#.',
    '#..e',
]


def dungeon_problem():
    start = None
    for row in t:
        for column in row:
            tst = 1


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


dungeon_problem()
