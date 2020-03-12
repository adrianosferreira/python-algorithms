from queue import *

g = {
    0: [
        {
            'd': 1,
            'n': 1
        },
        {
            'd': 1,
            'n': 6
        },
        {
            'd': 1,
            'n': 2
        }
    ],
    1: [
        {
            'd': 1,
            'n': 0
        },
        {
            'd': 10,
            'n': 3
        },
    ],
    2: [
        {
            'd': 1,
            'n': 0
        },
        {
            'd': 2,
            'n': 4
        },
    ],
    3: [
        {
            'd': 10,
            'n': 1
        },
        {
            'd': 3,
            'n': 5
        },
        {
            'd': 2,
            'n': 4
        }
    ],
    4: [
        {
            'd': 2,
            'n': 2
        },
        {
            'd': 3,
            'n': 5
        },
        {
            'd': 2,
            'n': 3
        }
    ],
    5: [
        {
            'd': 3,
            'n': 3
        },
        {
            'd': 3,
            'n': 4
        },
        {
            'd': 1,
            'n': 6
        }
    ],
    6: [
        {
            'd': 1,
            'n': 0
        },
        {
            'd': 1,
            'n': 5
        },
    ],
}


def shortest_distance(s, e):
    visited = [False for x in g]
    visited[s] = True
    q = Queue()
    q.put(s)
    distance_table = [None for x in g]
    distance_table[s] = 0

    while not q.empty():
        curr = q.get()

        for edge in g[curr]:
            distance = distance_table[curr] + edge['d']
            if distance_table[edge['n']] is None or distance < distance_table[edge['n']]:
                distance_table[edge['n']] = distance

            if visited[edge['n']]:
                continue

            visited[edge['n']] = True
            q.put(edge['n'])

    return distance_table[e]


print(shortest_distance(0, 3))
