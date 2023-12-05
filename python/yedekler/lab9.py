#task1
items = [111,100011,011,1010,10101010]
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))


#task2
s = input("Suehas 124 cats and 2 dogs")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

#task3
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def print_hist(h):
    for c in h:
        print c, h[c]
#task4
def isValid(password):
 
    if (len(password) < 8 or len(password) > 15):
        return False
 
    # to check space
    if (" " in password):
        return False
 
    if (True):
        count = 0
 
        # check digits from 0 to 9
        arr = ['0', '1', '2', '3',
        '4', '5', '6', '7', '8', '9']
 
        for i in password:
            if i in arr:
                count = 1
                break
 
        if count == 0:
            return False
 
    # for special characters
    if True:
        count = 0
 
        arr = ['@', '#','!','~','$','%','^',
                '&','*','(',',','-','+','/',
                ':','.',',','<','>','?','|']
 
        for i in password:
            if i in arr:
                count = 1
                break
        if count == 0:
            return False
 
    if True:
        count = 0
 
        # checking capital letters
        for i in range(65, 91):
 
            if chr(i) in password:
                count = 1
 
        if (count == 0):
            return False
 
    if (True):
        count = 0
 
        # checking small letters
        for i in range(97, 123):
 
            if chr(i) in password:
                count = 1
 
        if (count == 0):
            return False
 
    # if all conditions fails
    return True
 
# Driver code
password1 = input("password is:", password1)
 
if (isValid([i for i in password1])):
    print("Valid Password")
else:
    print("Invalid Password!!!")
 
password2 = "Geek$ForGeeks7"
if (isValid([i for i in password2])):
    print("Valid Password")
else:
    print("Invalid Password!!!")


#task5
    
import random
import math
# Taking Inputs
lower = 1

# Taking Inputs
upper = 9


x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")


#task6 ? :((





    
