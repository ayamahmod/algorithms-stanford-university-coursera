# In this programming problem and the next you'll code up the greedy algorithm
# from the lectures on Huffman coding.  Download the text file below.
# huffman.txt This file describes an instance of the problem. It has the
# following format:
# [number_of_symbols]
# [weight of symbol #1]
# [weight of symbol #2]
# ...
# For example, the third line of the file is "6852892,"
# indicating that the weight of the second symbol of the alphabet is 6852892.
# (We're using weights instead of frequencies, like in the "A More Complex
# Example" video.)  Your task in this problem is to run the Huffman coding
# algorithm from lecture on this data set. What is the maximum length of a
# codeword in the resulting Huffman code?  ADVICE: If you're not getting the
# correct answer, try debugging your algorithm using some small test cases. And
# then post them to the discussion forum!
import heapq

class Tree(object):
    def __init__(self):
        self.minL = -1
        self.maxL = -1

with open("huffman.txt") as f:
    content = f.readlines()

numOfSymbols = int(content.pop(0))
weights = []
for l in content:
    leaf = Tree()
    leaf.minL = 0
    leaf.maxL = 0
    heapq.heappush(weights, (int(l), leaf))

while len(weights) > 1:
    w1, v1 = heapq.heappop(weights)
    w2, v2 = heapq.heappop(weights)
    node = Tree()
    node.minL = min(v1.minL, v2.minL) + 1
    node.maxL = max(v1.maxL, v2.maxL) + 1
    heapq.heappush(weights, (w1+ w2, node))

totalW, head = heapq.heappop(weights)
print(head.minL)
print(head.maxL)
