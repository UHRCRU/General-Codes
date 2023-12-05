days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = int(input("year"))
month = int(input("month"))
day = int(input("day"))
def dayOfYear(day, month, year):
    if (month > 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        day += 1
        month -= 1
    while (month > 1):
        day = day + days[month - 1]
        month -= 1
    return day

if __name__ == '__main__':
    print(dayOfYear(day, month, year))
