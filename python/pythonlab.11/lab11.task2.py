import random
num = random.randint(1000,9999)
def getDigits(num):
	return [int(i) for i in str(num)]
def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False
def numOfBullsCows(num,guess):
	bull_cow = [0,0]
	num_li = getDigits(num)
	guess_li = getDigits(guess)
	for i,j in zip(num_li,guess_li):
		if j in num_li:
			if j == i:
				bull_cow[0] += 1
			else:
				bull_cow[1] += 1
	return bull_cow
while True:
	guess = int(input("Enter your guess: "))
	if guess < 1000 or guess > 9999:
		print("Enter 4 digit number only. Try again.")
		continue
	bull_cow = numOfBullsCows(num,guess)
	print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
	if bull_cow[0] == 4:
		print("You guessed right!")
		break
