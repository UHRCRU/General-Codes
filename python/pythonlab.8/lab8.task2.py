def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        return True
    else:
        return False
s1 = input("please enter your first string value: ")
s2 = input("please enter your second string value: ")
print(check(s1, s2))
