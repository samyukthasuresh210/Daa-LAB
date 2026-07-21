import heapq

# ---------- Union Find ----------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True


# ---------- Kruskal ----------
def kruskal(n, edges):
    edges.sort()

    uf = UnionFind(n)
    mst = []
    total = 0

    for cost, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, cost))
            total += cost

    return mst, total


# ---------- Prim ----------
def prim(n, graph):
    visited = [False] * n
    pq = [(0, 0, -1)]

    mst = []
    total = 0

    while pq:
        cost, node, parent = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True

        if parent != -1:
            mst.append((parent, node, cost))
            total += cost

        for neighbour, weight in graph[node]:
            if not visited[neighbour]:
                heapq.heappush(pq, (weight, neighbour, node))

    return mst, total


# ---------- Houses ----------
houses = ["House A", "House B", "House C", "House D", "House E"]

edges = [
    (4, 0, 1),
    (2, 0, 2),
    (5, 1, 2),
    (3, 1, 3),
    (6, 2, 4),
    (1, 3, 4)
]

n = len(houses)

graph = {i: [] for i in range(n)}

for cost, u, v in edges:
    graph[u].append((v, cost))
    graph[v].append((u, cost))


# ---------- Output ----------
mst1, cost1 = kruskal(n, edges.copy())

print("Kruskal's Algorithm")
for u, v, cost in mst1:
    print(houses[u], "-", houses[v], "Cost =", cost)
print("Total Cost =", cost1)

print()

mst2, cost2 = prim(n, graph)

print("Prim's Algorithm")
for u, v, cost in mst2:
    print(houses[u], "-", houses[v], "Cost =", cost)
print("Total Cost =", cost2)