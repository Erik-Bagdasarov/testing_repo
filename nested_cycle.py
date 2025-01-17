a = [
    [0, 2, 4, 6],
    [3, 4, 5, 1],
    [5, 4, 6, 4],
    [8, 6, 8, 5]
    ]

for i in a:
    a = 0
    for j in i:
        a += j
        # print(a, end='')
    print(f'sum of {i} is {a}')
