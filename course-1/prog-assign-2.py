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
