import numpy as np
# You are given as input an unsorted array of n distinct numbers, where n is a power of 2.
# Give an algorithm that identifies the second-largest number in the array,
# and that uses at most n + log_2 n - 2 comparisons.
def dict_key_values(dict, key, val):
    if key in dict:
        dict[key].append(val)
    else:
        dict[key] = [val]

def pairwise_comp(arr, dict):
    idx = 0
    newArr = []
    while idx < len(arr):
        bigger = arr[idx+1]
        smaller = arr[idx]
        if arr[idx] > arr[idx+1]:
            bigger = arr[idx]
            smaller = arr[idx+1]
        dict_key_values(dict, bigger, smaller)
        idx += 2
        newArr.append(bigger)
    return newArr

def prob1(arr):
    dict = {}
    while len(arr) > 1:
        arr = pairwise_comp(arr, dict)
    arr = dict[arr[0]]
    return max(arr)


# You are a given a unimodal array of n distinct elements,
# meaning that its entries are in increasing order up until its maximum element,
# after which its elements are in decreasing order.
# Give an algorithm to compute the maximum element that runs in O(log n) time.
def recursive_find(arr, l, r):
    if(r == l):
        return arr[r]

    if(r == l+1 & arr[r] > arr[l]):
        return arr[r]
    if(r == l+1 & arr[r] < arr[l]):
        return arr[l]

    mid = (l + (r-l))/2
    if(arr[mid-1] < arr[mid] & arr[mid+1] < arr[mid]):
        return arr[mid]
    if(arr[mid-1] < arr[mid]):
        return recursive_find(arr, mid+1, r)
    if(arr[mid+1] < arr[mid]):
        return recursive_find(arr, l, mid-1)

def prob2(arr):
    return recursive_find(arr, 0, len(arr)-1)

# You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive,
# negative, or zero. You want to decide whether or not there is an index i such that A[i] = i.
# Design the fastest algorithm that you can for solving this problem.
def binary_search(arr, l, r):
    if(r < l):
        return False
    if(r == l):
        if(arr[l] == l):
            return True
        return False
    mid = (l + (r-l))/2
    if(arr[mid] == mid):
        return True
    if(arr[mid] > mid):
        return binary_search(arr, l, mid-1)
    return binary_search(arr, mid+1, r)

def prob3(arr):
    return binary_search(arr, 0, len(arr)-1)

# You are given an n by n grid of distinct numbers.
# A number is a local minimum if it is smaller than all of its neighbors.
# (A neighbor of a number is one immediately above, below, to the left, or the right.
# Most numbers have four neighbors; numbers on the side have three; the four corners have two.)
# Use the divide-and-conquer algorithm design paradigm to compute a local minimum with only O(n) comparisons
# between pairs of numbers. (Note: since there are n^2 numbers in the input,
# you cannot afford to look at all of them.
# Hint: Think about what types of recurrences would give you the desired upper bound.)

def max_2_2(mat):
    max1 = min(np.array(mat[0,:]).flatten())
    max2 = min(np.array(mat[1,:]).flatten())
    return min(max1, max2)

def min_window(mat, n):
    min_elem = mat[0, 0]
    min_r = 0
    min_c = 0
    for i in range(0, n):
        for j in [0, n/2, n-1]:
            if mat[i, j] < min_elem:
                min_elem = mat[i, j]
                min_r = i
                min_c = j
    for i in [0, n/2, n-1]:
        for j in range(0, n):
            if mat[i, j] < min_elem:
                min_elem = mat[i, j]
                min_r = i
                min_c = j
    return (min_elem, min_r, min_c)

def quarter_search(mat, n):
    if (n == 1):
        return mat[0, 0]
    if (n == 2):
        return max_2_2(mat)
    (min_elem, min_r, min_c) = min_window(mat, n)
    top = down = left = right = True
    if(min_r > 0 & mat[min_r-1, min_c] < min_elem):
        top = False
    elif(min_r < n-1):
        if(mat[min_r+1, min_c] < min_elem): down = False
    elif(min_c > 0 & mat[min_r, min_c-1] < min_elem):
        left = False
    elif(min_c < n-1):
        if(mat[min_r, min_c+1] < min_elem): right = False
    if(top & down & left & right):  return min_elem
    # which quad to recurse in?
    return min_elem


def prob4(mat, n):
    return quad_search(mat, n)

def main():
    print(prob4(np.matrix("1 2 3; 4 5 6; -1 0 -8"), 3))

if __name__ == "__main__":
    main()
