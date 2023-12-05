
l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
l3= []
[l3.append(x) for x in l1 if x in l2]
if len(l3) > 1:
    print(True)
else:
    print(False)

l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]
l3= []
[l3.append(x) for x in l1 if x in l2]
if len(l3) > 1:
    print(True)
else:
    print(False)
