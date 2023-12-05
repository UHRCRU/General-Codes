year = int(input("year"))
month = input("month in string(June, January e.t.c.)")

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def DaysInMonth(month, year):
    if month in ['September', 'April', 'June', 'November']:
        print(30)
    elif month in ['January', 'March', 'May', 'July', 'August','October','December']:
        print(31)
    elif month == 'February' and is_leap_year(year) == True:
        print(29)
    elif month == 'February' and is_leap_year(year) == False:
        print(28)
    else:
        return None
DaysInMonth(month, year)
