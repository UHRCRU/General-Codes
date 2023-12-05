import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):
	if(re.fullmatch(regex, email)):
		print("Valid Email")
	else:
		print("Invalid Email")
if __name__ == '__main__' :

    email = input("please your enter e-mail:")
    check(email)
