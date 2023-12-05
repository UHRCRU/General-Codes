"""while True:
    while True:
        try:
            n = int(input("Enter a number: "))
            if 0 < n < 101:
                break
            print("The number must be between 1 (included) and 100 (included)")
            print(sum(range(1+n + 1)))
        except:
            print("Enter a valid number!")
 """
Total = 0
while True:
    try:
        a = int(input("Enter a value, please: "))
        Total += a
    except ValueError:
        print("Please Enter a valid value (int)")

    if Total > 100:
        print("The end. Total sum = ", Total)
    else:
        continue
