l1 = [2, 58, 4, 12, 6, 8, 7, 9]
l2 = [12, 9, 25, 8, 64, 58]
print("The original lists are (l1, l2) : ", l1,l2)
l3= []
[l3.append(x) for x in l1 if x not in l2]
print ("l3 : "+ str(l3))
l4= []
[l4.append(x) for x in l2 if x not in l1]
print ("l4 : "+ str(l4))
l5 = list(set(l1) ^ set(l2))
print("l5(xor): ",l5)


