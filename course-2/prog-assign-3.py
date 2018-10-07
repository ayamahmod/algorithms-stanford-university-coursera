# The goal of this problem is to implement the "Median Maintenance" algorithm
# (covered in the Week 3 lecture on heap applications). The text file contains a
# list of the integers from 1 to 10000 in unsorted order; you should treat this
# as a stream of numbers, arriving one by one. Letting x_i denote the ith
# number of the file, the kth median m_k, k is defined as the median of the
# numbers x_1,...,x_k. (So, if k is odd, then m_k ​is ((k+1)/2)((k+1)/2)th
# smallest number among x_1,...,x_k; if k is even, then m_k is the (k/2)th
# smallest number among x_1,...,x_k.)
# In the box below you should type the sum of these 10000 medians, modulo 10000
# (i.e., only the last 4 digits). That is, you should compute (m_1+m_2+m_3 +
# ...+ m_{10000}) mod 10000.
# OPTIONAL EXERCISE: Compare the performance achieved by heap-based and
# search-tree-based implementations of the algorithm.

import heapq

NUMBERS_COUNT = 10000

def addNumber(x, lowers, highers):
    if len(lowers) == 0 or x < -lowers[0]:
        heapq.heappush(lowers, -x)
    else:
        heapq.heappush(highers, x)

def rebalance(lowers, highers):
    biggerHeap = lowers if len(lowers) > len(highers) else highers
    smallerHeap = highers if len(lowers) > len(highers) else lowers
    if len(biggerHeap) - len(smallerHeap) >= 2:
        heapq.heappush(smallerHeap, -heapq.heappop(biggerHeap))

def getMedian(lowers, highers):
    if len(lowers) == len(highers):
        return -lowers[0]
    biggerHeap = lowers if len(lowers) > len(highers) else highers
    smallerHeap = highers if len(lowers) > len(highers) else lowers
    return biggerHeap[0] if biggerHeap[0] > 0 else -biggerHeap[0]

with open("Median.txt") as f:
    content = f.readlines()
lowers = [] # for the bigger half
highers = [] # for the smaller half
medians = []
for l in content:
    x = int(l.strip())
    addNumber(x, lowers, highers)
    rebalance(lowers, highers)
    medians.append(getMedian(lowers, highers))

sumOfMedians = 0
for x in medians:   sumOfMedians += x
print(sumOfMedians % 10000)
