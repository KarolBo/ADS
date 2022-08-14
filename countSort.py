def countSort(A):
    # init values
    n = len(A)
    B = [0] * n
    min_val = float('inf')
    max_val = -float('inf')
    for a in A:
        min_val = min(min_val, a)
        max_val = max(max_val, a)
    r = max_val - min_val + 1
    C = [0] * r

    # histogram
    for a in A:
        idx = a - min_val
        C[idx] += 1

    # prefix sum
    for i in range(1, r):
        C[i] += C[i-1]

    # collect sorted array B
    for i in range(n):
        val = A[i]
        reduced_val = val-min_val
        sorted_pos = C[reduced_val] - 1
        B[sorted_pos] = val
        C[reduced_val] -= 1

    return B

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
    arr = countSort(arr)
    print(arr == test_arr)