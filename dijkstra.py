from queue import PriorityQueue

g2 = {
    'A': [
        {
            'n': 'B',
            'dist': 1,
        },
        {
            'n': 'C',
            'dist': 1,
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
            'dist': 1,
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
    visited = {x: False for x in g1}
    dist = {x: float('inf') for x in g1}
    previous = {x: None for x in g1}
    dist[source] = 0
    pq = PriorityQueue()
    pq.put((0, source))

    while pq.qsize() > 0:
        c = pq.get()
        priority, index = c

        if index == target:
            break

        visited[c] = True

        for edge in g1[index]:
            if visited[edge['n']]:
                continue

            distance = dist[index] + edge['dist']

            if distance < dist[edge['n']]:
                dist[edge['n']] = distance
                previous[edge['n']] = index
                pq.put((distance, edge['n']))

    path = [target]
    c = previous[target]

    while c:
        path.append(c)
        c = previous[c]

    path.reverse()
    print(' > '.join(path))

    return f"Best distance from {source} to {target} is {dist[target]}"


print(shortest_path(g2, 'A', 'E'))
