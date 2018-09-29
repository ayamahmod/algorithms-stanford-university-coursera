# This file contains all of the 100,000 integers between 1 and 100,000
# (inclusive) in some order, with no integer repeated.  Your task is to compute
# the number of inversions in the file given, where the i^{th}i  th row of the
# file indicates the i^{th}i  th entry of an array.  Because of the large size
# of this array, you should implement the fast divide-and-conquer algorithm
# covered in the video lectures.  The numeric answer for the given input file
# should be typed in the space below.  So if your answer is 1198233847, then
# just type 1198233847 in the space provided without any space / commas / any
# other punctuation marks. You can make up to 5 attempts, and we'll use the best
# one for grading.  (We do not require you to submit your code, so feel free to
# use any programming language you want --- just type the final numeric answer
# in the following space.)  [TIP: before submitting, first test the correctness
# of your program on some small test files or your own devising. Then post your
# best test cases to the discussion forums to help your fellow students!] 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0 , n1):
        L[i] = arr[l + i]

    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]

    i = j = num_of_inv = 0
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            num_of_inv += n1 - i
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return num_of_inv

def mergeSort(arr, l, r):
    if(l == r): return 0
    if(l < r):
        m = int((l + (r-1))/2)
        inv_count = mergeSort(arr, l, m)
        inv_count += mergeSort(arr, m+1, r)
        inv_count += merge(arr, l, m, r)
        return inv_count
    return 0

#print(mergeSort([1,20,6,4,5], 0, 4))

with open("IntegerArray-week2.txt") as f:
    content = f.readlines()
content = [int(l.strip()) for l in content]
print(mergeSort(content, 0, len(content)-1))
