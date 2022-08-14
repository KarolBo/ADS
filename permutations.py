def stringPermute(string, i=0):
    if i == len(string):
        print(string)
        return
    for j in range(i, len(string)):
        string[i], string[j] = string[j], string[i]
        stringPermute(string, i+1)
        string[i], string[j] = string[j], string[i] # backtracking, unnecessary if string (immutable)

stringPermute(['A', 'B', 'C'])