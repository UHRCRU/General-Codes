import math
day = int(input("please enter the day of the month"))
month = int(input("please enter the month in integer"))
year = int(input("please enter the year"))
#1. reduce the month number by 2
month = month - 2
#2. if the month is less or equal zero, increase the month by 12, and decrease the year by 1
if month <= 0:
    month = month + 12
    year = year - 1
#3. take the number of the month, multiply it by 83 and divide it by 32
month = (month * 83)/32
#4. add the number of the day in the month to the result obtained
obtained = month + day
#5. add the year to the result obtained
obtained = year + obtained
#6. add (year / 4) to the result obtained
#7. subtract the (year / 100) from the result obtained
#8. add the (year / 400) to your result
#9. divide the result by 7 and find the rest
obtained = (obtained + (year / 4) - (year / 100) + (year / 400)) % 7
obtained = math.floor(obtained)
if obtained == 0:
    print("sunday")
elif obtained == 1:
    print("monday")
elif obtained == 2:
    print("tuesday")
elif obtained == 3:
    print("wednesday")
elif obtained == 4:
    print("thursday")
elif obtained == 5:
    print("friday")
elif obtained == 6:
    print("saturday")
else:
    print("something is wrong")
