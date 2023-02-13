def bucketSort(A):
    n = len(A)

    # normalize to 0 - n
    max_val = max(A)
    min_val = min(A)
    A = [(a - min_val) / (max_val - min_val) for a in A]
    hashList = [[] for _ in range(n)]

    for a in A:
        hashList[int(a) % n].append(a)
        if len(hashList[int(a) % n]) > 1: 
            hashList[int(a) % n].sort()
    
    i = 0
    for subList in hashList:
        for val in subList:
            A[i] = val * (max_val - min_val) + min_val # normalize back
            i += 1

    return A

def bucketSortInsert(A):
    n = len(A)

    # normalize to 0 - n
    max_val = max(A)
    min_val = min(A)
    A = [(a - min_val) / (max_val - min_val) for a in A]
    buckets = [[] for _ in range(n)]

    for a in A:
        b = round(a)
        buckets[b].append(a)
        i = len(buckets[b]) - 2
        while i >= 0 and buckets[b][i] > buckets[b][i+1]:
            buckets[b][i], buckets[b][i+1] = buckets[b][i+1], buckets[b][i]
            i -= 1
    
    i = 0
    for subList in buckets:
        for val in subList:
            A[i] = val * (max_val - min_val) + min_val # normalize back
            i += 1

    return A

###############################################################

array_list = []
array_list.append([3, 1, 5, 3])
array_list.append([1, 2, 3, 4, 5, 6])
array_list.append([45, 65, 34, 23, 67, 89, 34, 12, 34])
array_list.append([1, 2, 123, 123, 1, 2, 3])
array_list.append([1, 2, -1, 20, 20, 123, 123, 1, 20, 2, 3, 30])
array_list.append([-2, 2, -2, 2, 4, -2])
array_list.append([4, 5, -6, 10, -12, 1])
array_list.append([12, 5, 3, 2, 0, -3])
for arr in array_list:
    test_arr = arr.copy()
    test_arr.sort()
    arr = bucketSortInsert(arr)
    print(arr == test_arr)