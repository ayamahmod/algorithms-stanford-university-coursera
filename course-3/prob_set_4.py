import numpy as np

# calculate optimal binary search tree
def calOBS(freq, n):
    cost = []
    for i in range(n):
        cost.append([-1]*n)

    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n+1):
        for i in range(0, n-L+1):
            j = i+L-1
            cost[i][j] = -1
            for r in range(i, j+1):
               c = (cost[i][r-1] if (r > i) else 0) + (cost[r+1][j] if (r < j) else 0) + sum(freq[i:j+1])
               if cost[i][j] == -1 or c < cost[i][j]:
                  cost[i][j] = c
    return cost[0][n-1];

freq = [0.2,0.05,0.17,0.1,0.2,0.03,0.25]
print(calOBS(freq, 7))
