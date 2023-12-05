"""
count = 0
for i in range(3):
	number = int(input("Enter a number :"))
	count = count + 1
print("You have Entered",count,"number of times.")

my_list = []

for _ in range(6):
    try:
        my_list.append(int(input('Enter a number from 1 to 10: ')))
    except ValueError:
        print('The provided value is not an integer')

#if (my_list.append < 1) or (my_list.append > 10):
    print("your value is not between 1 and 10")
print(my_list)

lst = []

n = 6 #int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("please enter a number between 1 and 10: "))
    if ele < 1 or ele > 10:
        print("your value is not between 1 and 10")
        continue
    else:
        lst.append(ele)

print(lst)
"""
count = 0
for i in range(1, 7):
    try:
        a = int(input("Enter any number from 1 to 10: "))
    except ValueError:
        print("your value is not a valid value(integer). You have to restart the program")
        break
    if a < 1 or a > 10:
        print("your value is not between 1 and 10. You have to restart the program")
        break
    elif a == 5:
        count += 1
b = "The number 5 was entered {} times".format(count)
print(b)

