from queue import *

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def numberAmazonTreasureTrucks(rows, column, grid):
    components = {}
    category = 0
    visited = [False for x in range(rows * column)]

    for r, r_val in enumerate(grid):
        for c, c_val in enumerate(r_val):

            if visited[get_key(r, c, column)]:
                continue

            if c_val == 0:
                continue

            category += 1

            dfs_recursive([r, c], category, components, visited, column, rows, grid)

    return category


def get_key(r, c, nc):
    return nc * r + c


def dfs_recursive(node, category, components, visited, column, rows, grid):
    if node[0] < 0 or node[0] > rows - 1 or node[1] < 0 or node[1] > column - 1:
        return

    if grid[node[0]][node[1]] == 0:
        return

    if visited[get_key(node[0], node[1], column)]:
        return

    visited[get_key(node[0], node[1], column)] = True
    components[get_key(node[0], node[1], column)] = category

    for x in range(4):
        cr = node[0] + dr[x]
        cc = node[1] + dc[x]

        dfs_recursive([cr, cc], category, components, visited, column, rows, grid)


grid = [
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
]

# print(numberAmazonTreasureTrucks(5, 4, grid))


from collections import defaultdict


def criticalRouters(numRouters, numLinks, links):
    g1 = Graph(numRouters)

    for l in links:
        g1.addEdge(l[0], l[1])

    print(g1.get_critical_routers())


class Graph:

    def __init__(self, vertices):
        self.Vertices = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, Vertices):
        self.graph[u].append(Vertices)
        self.graph[Vertices].append(u)

    def verify_router_connections(self, u, visited, ap, parent, low, disc):

        children = 0
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self.graph[u]:

            #if v > len(visited) - 1:
             #   continue

            test = []

            if not visited[v]:
                parent[v] = u
                children += 1
                self.verify_router_connections(v, visited, ap, parent, low, disc)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def get_critical_routers(self):

        total = self.Vertices + 1
        visited = [False] * total
        disc = [float("Inf")] * total
        low = [float("Inf")] * total
        parent = [-1] * total
        ap = [False] * total

        for i in range(self.Vertices):
            if not visited[i]:
                self.verify_router_connections(i, visited, ap, parent, low, disc)

        res = []
        for index, value in enumerate(ap):
            if value:
                res.append(index)

        return res


#print(criticalRouters(7, 7, [[1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4, 5]]))

nums = [1,3,1,3,100]

def something(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n <= 2:
        return max(nums)

    rob1 = nums[:-1]
    rob2 = nums[1:]

    for i in range(1, len(rob1)):
        if i == 1:
            rob1[i] = max(rob1[0], rob1[1])
            rob2[i] = max(rob2[0], rob2[1])

            continue

        rob1[i] = max(rob1[i - 1], rob1[i] + rob1[i - 2])
        rob2[i] = max(rob2[i - 1], rob2[i] + rob2[i - 2])

    return max(max(rob1), max(rob2))

print(something(nums))