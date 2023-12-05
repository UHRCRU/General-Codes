import random
"""
a = (input("range min: "))
b = (input("range max: "))
l = random.uniform(a, b)
print(l)
#
a = float(input("range min: "))
b = float(input("range max: "))
x = round(random.uniform(range(a, b), 10), 3)
y = [i/10 for i in x]
print("Random number list is : ", y)
"""
def get_float_list(start, stop, size):
    result = []
    unique_set = set()
    for i in range(size):
        x = round(random.uniform(start, stop),3)
        while x in unique_set:
            x = round(random.uniform(start, stop),3)
        unique_set.add(x)
        result.append(x)

    return result
a = float(input("range min: "))
b = float(input("range max: "))
print(get_float_list(a, b, 10))
