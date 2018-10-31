# In this programming problem and the next you'll code up the clustering
# algorithm from lecture for computing a max-spacing kk-clustering. This file
# describes a distance function (equivalently, a complete graph with edge
# costs). It has the following format:
# [number_of_nodes]
# [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
# [edge 2 node 1] [edge 2 node 2] [edge 2 cost]  ...
# There is one edge (i,j) for each choice of 1≤i<j≤n, where n is the number of
# nodes.  For example, the third line of the file is "1 3 5250",
# indicating that the distance between nodes 1 and 3 (equivalently,
# the cost of the edge (1,3)) is 5250. You can assume that distances are
# positive, but you should NOT assume that they are distinct.  Your task in this
# problem is to run the clustering algorithm from lecture on this data set,
# where the target number k of clusters is set to 4. What is the maximum
# spacing of a 4-clustering?  ADVICE: If you're not getting the correct answer,
# try debugging your algorithm using some small test cases. And then post them
# to the discussion forum!
def mergeClusters(c1, c2, clusters, nodeCluster):
    biggerC = c1 if len(clusters[c1]) > len(clusters[c2]) else c2
    smallerC = c2 if len(clusters[c1]) > len(clusters[c2]) else c1
    for node in clusters[smallerC]:
        clusters[biggerC].append(node)
        nodeCluster[node] = biggerC
    clusters.pop(smallerC)

k = 4

with open("clustering1.txt") as f:
    content = f.readlines()

numOfNodes = int(content.pop(0))
nodeCluster = [-1]*numOfNodes
clusters = {}
for i in range(numOfNodes):
    nodeCluster[i] = i
    clusters[i] = [i]

edges = []
for l in content:
    v1, v2, c = map(int, l.split())
    v1 -= 1
    v2 -= 1
    edges.append([v1, v2, c])

# sort the edges
edges.sort(key = lambda x: x[2])

while len(clusters) > k:
    edge = edges.pop(0)
    c1 = nodeCluster[edge[0]]
    c2 = nodeCluster[edge[1]]
    if c1 != c2:
        mergeClusters(c1, c2, clusters, nodeCluster)

maxSpacing = -1
while maxSpacing == -1:
    edge = edges.pop(0)
    c1 = nodeCluster[edge[0]]
    c2 = nodeCluster[edge[1]]
    if c1 != c2:
        maxSpacing = edge[2]
        break

print(maxSpacing)
#106
