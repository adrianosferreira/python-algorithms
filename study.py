adjacent_list = {
    1: [2, 5],
    2: [1, 3],
    3: [6, 4, 2],
    4: [5, 3],
    5: [1, 4],
    6: [3, 7],
    7: [6, 8, 9],
    8: [7],
    9: [7],
}


def find_articulation_points():
    visited = [False for x in range(len(adjacent_list) + 1)]
    dt = [0 for x in range(len(adjacent_list) + 1)]
    low_link = [0 for x in range(len(adjacent_list) + 1)]
    ap = [False for x in range(len(adjacent_list) + 1)]
    helper(1, visited, low_link, dt, -1, ap)

    for i in range(len(ap)):
        if ap[i]:
            print(f"AP: %s" % i)


def helper(node, visited, low_link, dt, parent, ap):
    id = max(dt) + 1
    dt[node] = low_link[node] = id
    visited[node] = True
    children = 0

    for neighbour in adjacent_list[node]:

        if not visited[neighbour]:
            children += 1
            helper(neighbour, visited, low_link, dt, node, ap)
            low_link[node] = min(low_link[node], low_link[neighbour])

            if parent != -1 and low_link[neighbour] >= dt[node]:
                ap[node] = True

            if parent == -1 and children > 1:
                ap[node] = True
        else:
            low_link[node] = min(low_link[node], dt[neighbour])


find_articulation_points()
