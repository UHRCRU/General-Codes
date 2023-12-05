string = input("Enter string: ")

def ispalindrome(string):
    if string == string[::-1]:
        return "the string is Palindrome."
    else:
        return "The string is not a palindrome."
print(ispalindrome(string))
