def merge(M, l, m, r) -> list:
    A = M[l:m+1]
    B = M[m+1:r+1]
    len_a = len(A)
    len_b = len(B)
    a = b = 0
    m = l

    while a < len_a and b < len_b:
        if A[a] < B[b]:
            M[m] = A[a]
            a += 1
        else:
            M[m] = B[b]
            b += 1
        m += 1

    while a < len_a:
        M[m] = A[a]
        a += 1
        m += 1

    while b < len_b:
        M[m] = B[b]
        b += 1
        m += 1

    return M

def mergeSort(A, l, r):
    if l >= r:
        return
    m = (l + r) // 2
    mergeSort(A, l, m)
    mergeSort(A, m+1, r)
    merge(A, l, m, r)

###################################################


A = [-1, 3, 5, 7, 9, 100, 2, 4, 6, 8, 10]
print(merge(A, 0, 5, len(A)-1))

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
    mergeSort(arr, 0, len(arr)-1)
    print(arr == test_arr)