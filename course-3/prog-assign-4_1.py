# In this programming problem and the next you'll code up the knapsack algorithm
# from lecture. Let's start with a warm-up. Download the text file below.
# knapsack1.txt This file describes a knapsack instance, and it has the
# following format: [knapsack_size][number_of_items]  [value_1] [weight_1]
# [value_2] [weight_2]  ... For example, the third line of the file is "50074
# 659", indicating that the second item has value 50074 and size 659,
# respectively.  You can assume that all numbers are positive. You should assume
# that item weights and the knapsack capacity are integers.  In the box below,
# type in the value of the optimal solution.  ADVICE: If you're not getting the
# correct answer, try debugging your algorithm using some small test cases. And
# then post them to the discussion forum!

with open("knapsack1.txt") as f:
    content = f.readlines()

ks, numOfItems = map(int, content.pop(0).split())
items = []
for l in content:
    v, w = map(int, l.split())
    items.append([v, w])

dp = []
for i in range(numOfItems+1):
    dp.append([])
    for s in range(ks+1):
        dp[i].append(-1)

for i in range(numOfItems+1):
    dp[i][0] = 0

for s in range(ks+1):
    dp[0][s] = 0

for i in range(1, numOfItems+1):
    v, w = items[i-1]
    for s in range(1, ks+1):
        if s-w >= 0:
            dp[i][s] = max(dp[i-1][s], dp[i-1][s-w]+v)
        else:
            dp[i][s] = dp[i-1][s]

print(dp[numOfItems][ks])
