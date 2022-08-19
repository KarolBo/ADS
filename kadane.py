from re import A


def kadane(arr):
    max_so_far = 0
    cur_max = 0
    for a in arr:
        cur_max += a
        cur_max = max(cur_max, 0)
        max_so_far = max(max_so_far, cur_max)
    return max_so_far

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadane(arr))