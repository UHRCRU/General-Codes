list = []
Total = 0
while True:
    try:
        a = int(input("Enter a value, please: "))
        list.append(int(a))
        if a > 100:
            print("your value is higher than 100")
            exit()
        elif a < -10:
            print("your value is lower than -10")
            exit()
        """elif a == a ?:
            print("your value is same")
            exit()"""
        #i guess i need to use lists but i dunno how to implement that so im gonna ask to the lecturer
        Total += a
    except ValueError:
        print("Please Enter a valid value (int)")

    if Total > 100:
        print("The end. Total sum = ", Total)
    else:
        continue


