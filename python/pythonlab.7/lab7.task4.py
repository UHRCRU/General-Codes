def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str
tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str = convertTuple(tuple)
print(str)
item = tuple[3]
item1 = tuple[-4]
print("the 4th element: ", item)
print("the 4th element from last: ", item1)
