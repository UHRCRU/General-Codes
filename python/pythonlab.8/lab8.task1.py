string = input("Enter string: ")

def ispalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
print(ispalindrome(string))
