def rod_cut(n, price):
    solutions = (n+1) * [-float('inf')]
    solutions[0] = 0
    for rod_len in range(1, n+1):
        money = -float('inf')
        for cut in range(rod_len):
            if price[cut] + solutions[rod_len - cut - 1] > money:
                money = price[cut] + solutions[rod_len - cut - 1]
        solutions[rod_len] = money
    return solutions[n]


###################################################################

price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
max_money = rod_cut(11, price)
print(max_money)