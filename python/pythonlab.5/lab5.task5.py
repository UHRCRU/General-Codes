l1 = [1,3,6,78,35,24,55]
l2 = [12,24,35,24,88,120,155]
print("The original lists are (l1, l2) : ", l1,l2)
l3= []
[l3.append(x) for x in l1 if x in l2]
print ("common items(l3) : "+ str(l3))
l4 = list(set(l1) & set(l2))
print ("common items(l4) : "+ str(l4))
