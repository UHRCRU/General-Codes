import re
password = input("please enter your password")
flag = 0
while True:
    if (len(password)<=6) and (len(password)<=12):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[#@$]" , password):
        flag = -1
        break
    elif re.search("\s" , password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password ")
#function returns true ? i am gonna ask you that
