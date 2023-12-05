"""def checkKey(dict, key):

    if dict.a(key)==b(key):
        print("Present, value =", dict[key])
    else:
        print("Not present")

# Driver Function
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = input("please enter input")
checkKey(dict, key)

key = 'w'
checkKey(dict, key)
"""
"""
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
b = input("enter the key:)")
if dic.get(b) == None:
  print("key is not in dictionay")
else:
  print("Key is in dictionary")
"""
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")
