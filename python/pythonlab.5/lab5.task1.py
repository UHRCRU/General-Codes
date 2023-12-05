"""
l = [0, 3, 12, 8, 2]
for x in l:

print()
"""
q = [0, 3, 12, 8, 2]

mult = q[0]
for n in q[1:]:
    mult = sum(mult for _ in range(n))
print(mult)


