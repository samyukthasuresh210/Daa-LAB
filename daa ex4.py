import heapq

# Dijkstra's Algorithm
def dijkstra(graph, source):

    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n

    dist[source] = 0

    pq = [(0, source)]

    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


# Reconstruct Path
def reconstruct_path(prev, source, target):

    path = []

    while target is not None:
        path.append(target)
        target = prev[target]

    path.reverse()

    if path[0] == source:
        return path

    return []


# -------- School Locations --------

places = [
    "Main Gate",
    "Office",
    "Library",
    "Classroom",
    "Lab",
    "Canteen"
]

graph = {
    0: [(1, 4), (2, 2)],
    1: [(3, 5)],
    2: [(1, 1), (4, 4)],
    3: [(5, 3)],
    4: [(3, 2), (5, 5)],
    5: []
}

source = 0

distance, previous = dijkstra(graph, source)

print("Shortest Routes from Main Gate\n")

print(f'{"Place":<15}{"Distance":<10}Path')
print("-" * 50)

for i in range(len(places)):
    path = reconstruct_path(previous, source, i)
    path_names = " -> ".join(places[x] for x in path)

    print(f'{places[i]:<15}{distance[i]:<10}{path_names}')