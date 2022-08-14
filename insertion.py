def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        val = A[i]
        j = i - 1
        while j >= 0 and A[j] > val:
            A[j+1] = A[j]
            A[j] = val
            j -= 1

#######################################

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
    insertionSort(arr)
    print(arr == test_arr)
