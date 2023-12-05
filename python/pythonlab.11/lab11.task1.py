import random
name = input("What is your name? ")
print("Good Luck ! ", name)
words = ['history', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'digital', 'game', 'retro', "love", "feel"]
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 8
while turns > 0:
	failed = 0
	for char in word:
		if char in guesses:
			print(char, end=" ")
		else:
			print("_", end=" ")
			failed += 1
	if failed == 0:
		print("You Win")
		print("The word is: ", word)
		break

	print()
	guess = input("guess a character:")
	guesses += guess
	if guess not in word:
		turns -= 1
		print("Wrong")
		print("You have", + turns, 'more guesses')
		if turns == 0:
			print("You Loose")
