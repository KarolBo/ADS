from itertools import count
from math import log10, ceil

def getDigit(val, d, base=10):
    digit = abs(val) // base**d % base
    if val < 0:
        digit *= -1
    return digit

def countSort(A, d, base):
    # init values
    n = len(A)
    B = [0] * n
    C = [0] * (2 * base - 1) # twice size to consider negative numbers

    # histogram
    for a in A:
        if abs(a) < base**d - 1:
            idx = base - 1
        else:
            idx = getDigit(a, d, base) + base - 1
        C[idx] += 1

    # prefix sum
    for i in range(1, 2 * base - 1):
        C[i] += C[i-1]

    # collect sorted array B, reversed to be stable
    for i in reversed(range(0, n)): 
        idx = getDigit(A[i], d, base) + base - 1
        sorted_pos = C[idx] - 1
        B[sorted_pos] = A[i]
        C[idx] -= 1

    return B

def radixSort(A, base=10):
    max_abs = max([abs(a) for a in A]) + 1 # +1 in case that even power of 10
    digits = ceil(log10(max_abs))
    for i in range(digits):
        A = countSort(A, i, base)
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
    arr = radixSort(arr)
    print(arr == test_arr)