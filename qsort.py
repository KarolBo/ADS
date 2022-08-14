import random

def partition(arr, left, right):
    pivot = random.randint(left, right)
    arr[pivot], arr[right] = arr[right], arr[pivot]  
    pivot = right
    right -= 1
    while left <= right:
        if left <= right and arr[left] <= arr[pivot]:
            left += 1
        if left <= right and arr[right] >= arr[pivot]:
            right -= 1

        if left < right and arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

    arr[pivot], arr[left] = arr[left], arr[pivot]
    return left

def qsort(arr, left, right):
    if left >= right:
        return
    pivot = partition(arr, left, right)
    qsort(arr, left, pivot - 1)
    qsort(arr, pivot + 1, right)


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
    qsort(arr, 0, len(arr) - 1)
    print(arr == test_arr)
