from queue import *

t = [
    's.....',
    '.####e',
    '.##...',
    '..#.##',
    '#.....',
    'e.....',
]

nr = 6
nc = 6
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def dungeon_problem():
    start = None
    for r, row in enumerate(t):
        for c, col in enumerate(row):
            if col == 's':
                start = [r, c]

        if start:
            break

    return bfs(start)


def get_key(r, c):
    return nc * r + c


def bfs(n):
    q = Queue()
    q.put(n)
    visited = [False for x in range(nr*nc)]
    visited[get_key(n[0], n[1])] = True
    # ct = {get_key(n[0], n[1]): 0}
    count = 1
    nodes_found = 0
    nodes_left = 1

    while not q.empty():
        c = q.get()
        row = c[0]
        col = c[1]

        for x in range(4):
            cr = row + dr[x]
            cc = col + dc[x]

            if cr < 0 or cc < 0 or cr >= nr or cc >= nc:
                continue

            if visited[get_key(cr, cc)]:
                continue

            visited[get_key(cr, cc)] = True
            # ct[get_key(cr, cc)] = ct[get_key(row, col)] + 1

            if t[cr][cc] == '#':
                continue

            if t[cr][cc] == 'e':
                # return ct[get_key(cr, cc)]
                return count

            nodes_found += 1
            q.put([cr, cc])

        nodes_left -= 1
        if nodes_left == 0:
            count += 1
            nodes_left = nodes_found
            nodes_found = 0

    return -1


print(dungeon_problem())
