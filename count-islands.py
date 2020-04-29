g = [
    [1, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 0, 0, 1, 1, 0],
]


def count_islands(g, rows, columns):
    count = 0
    visited = {}

    for r, row in enumerate(g):
        for c, col in enumerate(row):
            if str(r) + str(c) in visited or g[r][c] == 0:
                continue

            count += 1
            helper(g, visited, r, c, rows, columns)

    return count


def helper(g, visited, row, col, nrows, ncolumns):
    if str(row) + str(col) in visited:
        return

    if g[row][col] == 0:
        return

    visited[str(row) + str(col)] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for step in range(4):
        nextR = row + dr[step]
        nextC = col + dc[step]

        if nextR > nrows - 1 or nextR < 0 or nextC > ncolumns - 1 or nextC < 0:
            continue

        helper(g, visited, nextR, nextC, nrows, ncolumns)


print(count_islands(g, 13, 6))
