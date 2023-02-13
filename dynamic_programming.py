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


def matrix_multiplication(sizes):
    n = len(sizes)
    m = [[float('inf') for _ in range(n)] for _ in range(n)]
    s = [[None for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        m[i][i] = 0

    for l in range(2, n+1):
        for i in range(0, n-l+1):
            j = i + l - 1
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + sizes[i-1] * sizes[k] * sizes[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    _get_parens(s, 1, n-1)
    print()
    return m[1][-1]

def _get_parens(s, i, j):
    if i == j:
        print(chr(ord('A') - 1 + i), end='')
    else:
        print('(', end='')
        _get_parens(s, i, s[i][j])
        _get_parens(s, s[i][j]+1, j)
        print(')', end='')




###################################################################

price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
max_money = rod_cut(5, price)
print(max_money)

test_inputs = [
    [40, 20, 30, 10, 30],
    [1, 2, 3, 4, 3],
    [30, 35, 15, 5, 10, 20, 25],
]
test_results = [26000, 30, 15125]
for input, expected in zip(test_inputs, test_results):
    output = matrix_multiplication(input)
    print(output, expected)