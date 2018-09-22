import random

def noOfVertices(edges):
    vertices = set()
    for v1, v2 in edges:
        vertices.add(v1)
        vertices.add(v2)
    return len(vertices)

def contract(edges, a, b):
    for f,s in edges[:]:
        if f == b:
            edges.remove((f, s))
            edges.append((a, s))
        if s == b:
            edges.remove((f, s))
            edges.append((f, a))

def removeLoops(edges):
    for f,s in edges[:]:
        if f == s:
            edges.remove((f,s))

def removeOneEdge(edges):
    rEdge = random.choice(edges)
    edges.remove(rEdge)
    contract(edges, rEdge[0], rEdge[1])
    removeLoops(edges)

def minCut(edges):
    while noOfVertices(edges) > 2:
        removeOneEdge(edges)
    return len(edges)

with open("AdjList-week4.txt") as f:
    content = f.readlines()
edges = []
for l in content:
    row = list(map(int, l.split()))
    fst = row[0]
    for vertex in row[1:]:
        snd = vertex
        if (snd, fst) not in edges:
            edges.append((fst, snd))
cuts = [minCut(edges[:]) for i in range(0,200)]
print(min(cuts))
# print(minCut(edges[:]))
