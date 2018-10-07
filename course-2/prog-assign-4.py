# The goal of this problem is to implement a variant of the 2-SUM algorithm
# covered in this week's lectures.
#
# The file contains 1 million integers, both positive and negative (there might be
# some repetitions!).This is your array of integers, with the i^{th}i  th row of
# the file specifying the i^{th}i  th entry of the array.
#
# Your task is to compute the number of target values t in the interval
# [-10000,10000] (inclusive) such that there are distinct numbers x,y in the
# input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a
# one-line addition to the algorithm from lecture.)
#
# Write your numeric answer (an integer between 0 and 20001) in the space
# provided.
#
# OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your
# own hash table for it. For example, you could compare performance under the
# chaining and open addressing approaches to resolving collisions.

def findPair(hashTable, t):
    for x in hashTable:
        y = t - x
        if y in hashTable and y != x:
            return True
    return False

LOWER = -10000
UPPER = 10000

with open("algo1-programming_prob-2sum.txt") as f:
    content = f.readlines()
hashTable = dict()
for l in content:
    x = int(l.strip())
    if x not in hashTable:
        hashTable[x] = 1
    else:
        hashTable[x] += 1
count = 0
for i in range(LOWER, UPPER+1):
    print(i)
    if findPair(hashTable, i):
        count += 1
print(count)
