# In this question your task is again to run the clustering algorithm from
# lecture, but on a MUCH bigger graph. So big, in fact, that the distances
# (i.e., edge costs) are only defined implicitly, rather than being provided as
# an explicit list.  The data set is below.  clustering_big.txt
# The format is:  [# of nodes] [# of bits for each node's label]
# [first bit of node 1] ... [last bit of node 1]  [first bit of node 2] ...
# [last bit of node 2]  ...  For example, the third line of the file
# "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated
# with node #2.  The distance between two nodes u and v in this problem is
# defined as the Hamming distance--- the number of differing bits ---
# between the two nodes' labels. For example, the Hamming distance between the
# 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1
# 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).
# The question is: what is the largest value of k such that there is
# a k-clustering with spacing at least 3? That is, how many clusters are needed
# to ensure that no pair of nodes with all but 2 bits in common get split into
# different clusters?  NOTE: The graph implicitly defined by the data file is
# so big that you probably can't write it out explicitly, let alone sort the
# edges by cost. So you will have to be a little creative to complete this part
# of the question. For example, is there some way you can identify the smallest
# distances without explicitly looking at every pair of nodes?

def invert(b):
    if b == '0':
        return '1'
    return '0'

def getFriends(v):
    friends = []
    for i in range(len(v)):
        friend1 = v[:i]+invert(v[i])+v[i+1:]
        friends.append(friend1)
        for j in range(i+1, len(v)):
            friends.append(friend1[:j]+invert(friend1[j])+friend1[j+1:])
    return friends

def getParent(v, nodeCluster):
    head = nodeCluster[v]
    while head != nodeCluster[head]:
        head = nodeCluster[head]
    return head


def merge(v1, v2, nodeCluster):
    head1 = getParent(v1, nodeCluster)
    head2 = getParent(v2, nodeCluster)
    if head1 != head2:
        nodeCluster[head2] = head1
        return True
    return False

with open("clustering_big.txt") as f:
    content = f.readlines()

numOfNodes, numOfBits = map(int, content.pop(0).split())
nodeCluster = {}

for l in content:
    v = ''.join(l.split())
    nodeCluster[v] = v

numOfClusters = len(nodeCluster)
nodes = nodeCluster.keys()
cnt = 0
for v in nodes:
    print('processing node #', cnt, ', ', numOfClusters)
    friends = getFriends(v)
    for f in friends:
        if f in nodes:
            if merge(v, f, nodeCluster):
                numOfClusters -= 1
    cnt +=1

print(numOfClusters)
#6118
