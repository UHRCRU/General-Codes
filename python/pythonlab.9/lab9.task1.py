items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x % 5:
        items.append(p)
        print(int(p, 2), end=' ')
print(','.join(items))
