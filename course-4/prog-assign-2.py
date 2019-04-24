# In this assignment you will implement one or more algorithms for the traveling
# salesman problem, such as the dynamic programming algorithm covered in the
# video lectures. Here is a data file describing a TSP instance.
# tsp.txt
# The first line indicates the number of cities. Each city is a point in the
# plane, and each subsequent line indicates the x- and y-coordinates of a single
# city.
# The distance between two cities is defined as the Euclidean distance --- that
# is, two cities at locations (x,y)(x,y) and (z,w)(z,w) have distance
# sqrt{(x-z)^2 + (y-w)^2} between them.
# In the box below, type in the minimum cost of a traveling salesman tour for
# this instance, rounded down to the nearest integer.
# OPTIONAL: If you want bigger data sets to play with, check out the TSP
# instances from around the world here. The smallest data set (Western Sahara)
# has 29 cities, and most of the data sets are much bigger than that. What's the
# largest of these data sets that you're able to solve --- using dynamic
# programming or, if you like, a completely different method?
# HINT: You might experiment with ways to reduce the data set size. For example,
# trying plotting the points. Can you infer any structure of the optimal
# solution? Can you use that structure to speed up your algorithm?
import math
import numpy as np

f = open("tsp.txt")
nCities = int(f.readline())
lines = f.readlines()
f.close()
cities = []
for line in lines:
    x, y = map(float, line.split())
    cities.append([x, y])
mtrx = []
for c1 in cities:
    row = []
    for c2 in cities:
        a = c1[0] - c2[0]
        b = c1[1] - c2[1]
        row.append(math.sqrt(a*a + b*b))
    mtrx.append(row)

dp = np.full([1 << (nCities), nCities], -1.0)
dp[1, 0] = 0
for i in range(1, 1 << nCities): # states
    print(i)
    for j in range(nCities): # current state
        if dp[i,j] == -1: continue
        for k in range(1, nCities): # cities to visit
            if (i & (1 << k)) != 0: continue
            p = (i | (1 << k)) # new state
            if dp[p][k] == -1:
                dp[p][k] = dp[i][j] + mtrx[j][k]
            dp[p][k] = min(dp[p][k], dp[i][j] + mtrx[j][k])
ans = float('inf')
for i in range(1, nCities):
    if dp[(1 << nCities)-1][i] != -1:
        ans = min(ans, dp[(1 << nCities)-1][i] + mtrx[i][0])

print(ans)
