year = int(input("please enter the year"))
def IsLeapYear(year):
    leap = False
    if (year % 400 == 0) and (year % 100 == 0):
        leap = True
    elif (year % 4 ==0) and (year % 100 != 0):
        leap = True
    else:      
        pass
    return leap
print(IsLeapYear (year))
