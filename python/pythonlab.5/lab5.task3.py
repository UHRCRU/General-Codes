"""
l = [2, 6, 7, 1, 34, 64, 2, 7, 35, 1]
print("Original List: ", l)
res = [*set(l)]
print("List after removing duplicate elements: ", res)
"""
test_list = [2, 6, 7, 1, 34, 64, 2, 7, 35, 1]
print("The original list is : "+ str(test_list))
res = []
[res.append(x) for x in test_list if x not in res]
print ("The list after removing duplicates : "+ str(res))
