a = [42, 3, 4, 765, 34, 56, 42, 3]
duble_count = 0
b = []

for i in a:
    if i not in b:
        b.append(i)
        if a.count(i) > 1:
            duble_count += 1

print(f'Unique values: {b}')
print(f'Count of dubbed values: {duble_count}')

