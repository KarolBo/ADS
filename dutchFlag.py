def dutchFlag(arr):
    l = 0
    r = len(arr) - 1
    p = 0
    while p <= r:
        if arr[p] == 1:
            arr[l], arr[p] = arr[p], arr[l]
            l += 1
            p += 1
        elif arr[p] == 3:
            arr[r], arr[p] = arr[p], arr[r]
            r -= 1
        else:
            p += 1
            

################################################

arr1 = [1, 2, 3, 3, 1, 1, 2, 2, 1, 2, 3, 2, 1]
arr2 = [2, 3, 1, 2, 3, 1, 2, 3, 1]
arr3 = [3, 2, 1, 3, 2, 1, 2, 3, 1, 1, 2]
dutchFlag(arr1)
dutchFlag(arr2)
dutchFlag(arr3)
print(arr1)
print(arr2)
print(arr3)