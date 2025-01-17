# a = [0, 1, 2, 3, 2, 1, 2, 1, 2, 3, 3, 1, 4, 2, 3, 1, 3, 2, 2, 1, 2, 3, 5, 10]
a = [1, 2, 3, 3]
count = [0] * 7

for i in range(6):
    count[i] = a.count(i)
    print(f'{i}: {count[i]}')
