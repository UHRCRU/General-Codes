l = input("Input: ").split()
l = [int(item) for item in l]
a = l[0]
b = l[1]
c = l[2]
def checktriangle (a, b, c) :
    if a+b >= c and b+c >= a and c+a >= b:
        return True
    else:
        return False
if checktriangle (a, b, c) :
    print('Triangle is Valid.')
    if (a*a+b*b == c*c) or (c*c+b*b == a*a) or (a*a+c*c == b*b):
        print("The triangle is right-angled.")
    else:
        print("The triangle is not right-angled.")
else:
    print('Triangle is Invalid.')
