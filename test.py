from queue import *

s = [0, 1]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
total_rows = 5
total_columns = 5


def solve_dungeon(d):
    visited = [False for x in range(total_rows * total_columns)]
    visited[get_key(s[0], s[1])] = True
    q = Queue()
    q.put([s[0], s[1]])
    end = False
    count = 0
    edges_next_layer = 0
    edges_left = 1

    while not q.empty():
        curr = q.get()
        r = curr[0]
        c = curr[1]

        for edge in range(len(dr)):
            edge_row = r + dr[edge]
            edge_col = c + dc[edge]

            if edge_row < 0 or edge_col < 0:
                continue

            if edge_row >= total_rows or edge_col >= total_columns:
                continue

            if visited[get_key(edge_row, edge_col)]:
                continue

            visited[get_key(edge_row, edge_col)] = True

            if d[edge_row][edge_col] == '#':
                continue

            if d[edge_row][edge_col] == 'e':
                end = True
                break

            edges_next_layer += 1
            q.put([edge_row, edge_col])

        edges_left -= 1
        if edges_left == 0:
            edges_left = edges_next_layer
            edges_next_layer = 0
            count += 1

        if end:
            return count

    return -1


def get_key(r, c):
    return total_columns * r + c


# solve_dungeon([
#     '.s...',
#     '####.',
#     '####.',
#     '####.',
#     'e....',
# ])
#


l = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 5],
    5: [4],
}


def dfs(s, visited):
    if visited[s]:
        return

    visited[s] = True
    print(s)

    for edge in l[s]:
        dfs(edge, visited)


dfs(0, [False for x in l])
