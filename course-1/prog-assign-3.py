def firstElemPivot(arr, l, r):
    i = l + 1
    for j in range(l + 1, r):
        if(arr[j] < arr[l]):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i-1


def lastElemPivot(arr, l, r):
    arr[l], arr[r-1] = arr[r-1], arr[l]
    return firstElemPivot(arr, l, r)

def medianOf3Pivot(arr, l, r):
    if (r-l) == 1:
        return firstElemPivot(arr, l, r)
    mid = int((r-l)/2) + l
    mid += 0 if (r-l) % 2 else -1
    candidates = [arr[l], arr[mid], arr[r-1]]
    candidates.sort()
    median = l
    if arr[mid] == candidates[1]:
        median = mid
    elif arr[r-1] == candidates[1]:
        median = r-1
    arr[l], arr[median] = arr[median], arr[l]
    return firstElemPivot(arr, l, r)


def QuickSort(arr, l, r):
    if(l >= r):
        return 0
    m = r - l -1
    pivotIdx = medianOf3Pivot(arr, l, r)
    m += QuickSort(arr, l, pivotIdx)
    m += QuickSort(arr, pivotIdx+1, r)
    return m

with open("IntegerArray-week3.txt") as f:
    content = f.readlines()
content = [int(l.strip()) for l in content]
# content = [8, 2, 4, 5, 7, 1]
print(QuickSort(content, 0, len(content)))
# for x in content:
#     print(x)
