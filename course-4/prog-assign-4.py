# In this assignment you will implement one or more algorithms for the all-pairs
# shortest-path problem. Here are data files describing three graphs:
# g1.txt g2.txt g3.txt
# The first line indicates the number of vertices and edges, respectively. Each
# subsequent line describes an edge (the first two numbers are its tail and
# head, respectively) and its length (the third number). NOTE: some of the edge
# lengths are negative. NOTE: These graphs may or may not have negative-cost
# cycles. Your task is to compute the "shortest shortest path". Precisely, you
# must first identify which, if any, of the three graphs have no negative
# cycles. For each such graph, you should compute all-pairs shortest paths and
# remember the smallest one (i.e., compute minu,v e Vd(u,v), where d(u,v)d(u,v)
# denotes the shortest-path distance from uu to vv).
# If each of the three graphs has a negative-cost cycle, then enter "NULL" in
# the box below. If exactly one graph has no negative-cost cycles, then enter
# the length of its shortest shortest path in the box below. If two or more of
# the graphs have no negative-cost cycles, then enter the smallest of the
# lengths of their shortest shortest paths in the box below.
# OPTIONAL: You can use whatever algorithm you like to solve this question. If
# you have extra time, try comparing the performance of different all-pairs
# shortest-path algorithms! OPTIONAL: Here is a bigger data set to play with.
# large.txt
# For fun, try computing the shortest shortest path of the graph in the file
# above.
import heapq

MAX_INT = float('Inf')

# Dijkstra algorithm
def dijkstra(adjList, verticesCount, src):
    shortestPaths = [MAX_INT for i in range(verticesCount)]
    visited = [False for i in range(verticesCount)]
    pq = [(0, src)]
    while len(pq) > 0:
        w, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        shortestPaths[u] = w
        for v, wt in adjList[u]:
            if not visited[v]:
                heapq.heappush(pq, (w+wt, v))
    return shortestPaths

# Bellmanford algorithm to calculate shortest distance from added from source
# to all other vertices
def bellmanford(edges, verticesCount):
    dest = [MAX_INT] * (verticesCount + 1)
    dest[verticesCount] = 0

    for i in range(verticesCount):
        edges.append([verticesCount, i, 0])

    for i in range(verticesCount):
        for v1, v2, w in edges:
            if((dest[v1] != MAX_INT) and (dest[v1] + w < dest[v2])):
                dest[v2] = dest[v1] + w

    # detect negative cycle
    hasNegCyc = False
    for v1, v2, w in edges:
        if((dest[v1] != MAX_INT) and (dest[v1] + w < dest[v2])):
            hasNegCyc = True
    return hasNegCyc, dest[0:verticesCount]


# Johnson’s algorithm
def johnson(adjList, edges, verticesCount):
    shortest = MAX_INT
    # add s and get vertices weights
    hasNegCyc, dest = bellmanford(edges, verticesCount)
    if hasNegCyc:
        return shortest

    # Reweighting the graph
    for i in range(verticesCount):
        for j in range(len(adjList[i])):
                v2, w = adjList[i][j]
                adjList[i][j][1] = (w + dest[i] - dest[v2])

    shortestDists = [[] for i in range(verticesCount)]
    # Run Dijkstra for every vertex
    for src in range(verticesCount):
        shortestDists[src] = dijkstra(adjList, verticesCount, src)

    # Reweight the distances and print the shortest one
    for i in range(verticesCount):
        for j in range(verticesCount): # vertices
            w = shortestDists[i][j]
            if w != MAX_INT:
                shortestDists[i][j] = w - (dest[i] - dest[j])
                shortest = min(shortest, shortestDists[i][j])
    return shortest

G_FILE_NAMES = ["large.txt"]

for fName in G_FILE_NAMES:
    f = open(fName)
    line = f.readline()
    verticesCount, edgesCount = map(int, line.split())
    lines = f.readlines()
    adjList = [[] for i in range(verticesCount)]
    edges = []
    for l in lines:
        v1, v2, w = map(int, l.split())
        v1 -= 1
        v2 -= 1
        adjList[v1].append([v2, w])
        edges.append([v1, v2, w])
    f.close()
    print(johnson(adjList, edges, verticesCount))
