# The file contains the edges of a directed graph. Vertices are labeled as
# positive integers from 1 to 875714. Every row indicates an edge, the vertex
# label in first column is the tail and the vertex label in second column is the
# head (recall the graph is directed, and the edges are directed from the first
# column vertex to the second column vertex). So for example, the 11^{th}11 th
# row looks liks : "2 47646". This just means that the vertex with label 2 has
# an outgoing edge to the vertex with label 47646 # Your task is to code up the
# algorithm from the video lectures for computing strongly connected components
# (SCCs), and to run this algorithm on the given graph. # Output Format: You
# should output the sizes of the 5 largest SCCs in the given graph, in
# decreasing order of sizes, separated by commas (avoid any spaces). So if your
# algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200
# and 100, then your answer should be "500,400,300,200,100" (without the
# quotes). If your algorithm finds less than 5 SCCs, then write 0 for the
# remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are
# 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the
# quotes). (Note also that your answer should not have any spaces in it.) #
# WARNING: This is the most challenging programming assignment of the course.
# Because of the size of the graph you may have to manage memory carefully. The
# best way to do this depends on your programming language and environment, and
# we strongly suggest that you exchange tips for doing this on the discussion
# forums. #
import sys

def DFS(adjList, visited, finished, vIdx, st):
    if visited[vIdx]:
        return
    mySt = [vIdx]
    while len(mySt) > 0:
        top = mySt.pop()
        if not visited[top]:
            visited[top] = True
            mySt.append(top)
            for v in adjList[top]:
                if not visited[v]:
                    mySt.append(v)
        else:
            if not finished[top]:
                finished[top] = True
                st.append(top)
    return

def transposeG(adjList):
    transposedG = [[] for i in range(len(adjList))]
    for v in range(len(adjList)):
        for vNeib in adjList[v]:
            transposedG[vNeib].append(v)
    return transposedG


VERTICES_COUNT = 875714

with open("SCC.txt") as f:
    content = f.readlines()

adjList = [[] for i in range(VERTICES_COUNT)]

for l in content:
    edge = list(map(int, l.split()))
    # create transposed graph
    adjList[edge[1]-1].append(edge[0]-1)

visited = [False for i in range(VERTICES_COUNT)]
finished = [False for i in range(VERTICES_COUNT)]
st = []

for v in range(len(adjList)):
    if not visited[v]:
        DFS(adjList, visited, finished, v, st)

transposedG = transposeG(adjList)
adjList = []

visited = [False for i in range(VERTICES_COUNT)]
finished = [False for i in range(VERTICES_COUNT)]
biggest5 = []
while len(st) > 0:
    v = st.pop()
    if not visited[v]:
        scc = []
        DFS(transposedG, visited, finished, v, scc)
        biggest5.append(len(scc))
        if len(biggest5) > 5:
            biggest5.sort(reverse = True)
            biggest5.pop()
print(biggest5)
