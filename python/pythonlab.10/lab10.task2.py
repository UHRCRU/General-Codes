from datetime import date
day = input("enter day")
month = input("enter month")
year = input("enter year")
intday = int(day)
intmonth = int(month)
intyear = int(year)
"""
today = datetime.date.today(year, month, day)
endofyear = datetime.date(year, 12, 31)
diff = endofyear - today
print(diff.days)"""

d0 = date(intyear, intmonth, intday)
d1 = date(intyear, 12, 31)
delta = d1 - d0
print("remaining days until end of the year:")
print(delta.days)

