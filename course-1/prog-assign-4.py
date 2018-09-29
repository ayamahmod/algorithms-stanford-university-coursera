# The file contains the adjacency list representation of a simple undirected
# graph. There are 200 vertices labeled 1 to 200. The first column in the file
# represents the vertex label, and the particular row (other entries except the
# first column) tells all the vertices that the vertex is adjacent to. So for
# example, the 6^{th}6  th row looks like : "6	155	56	52	120	......". This just
# means that the vertex with label 6 is adjacent to (i.e., shares an edge with)
# the vertices with labels 155,56,52,120,......,etc  Your task is to code up and
# run the randomized contraction algorithm for the min cut problem and use it on
# the above graph to compute the min cut. (HINT: Note that you'll have to figure
# out an implementation of edge contractions. Initially, you might want to do
# this naively, creating a new graph from the old every time there's an edge
# contraction. But you should also think about more efficient implementations.)
# (WARNING: As per the video lectures, please make sure to run the algorithm
# many times with different random seeds, and remember the smallest cut that you
# ever find.) Write your numeric answer in the space provided. So e.g., if your
# answer is 5, just type 5 in the space provided.

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
