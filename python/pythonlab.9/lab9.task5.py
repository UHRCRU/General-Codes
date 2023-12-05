import random
import math
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
x = random.randint(lower, upper)
count = 0
while True:
	count += 1
	guess = int(input("Guess a number:- "))
	if x == guess:
		print("Congratulations you did it in ", count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")
