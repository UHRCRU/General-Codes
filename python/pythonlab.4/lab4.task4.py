a = float(input("Enter your income (zloty)"))


if a < 85528:
    b = (a * (18/100)) - 556.02
    print("tax is taking from you is(zloty):", round(b))
elif a > 85528:
    b = ((a-85528) * (32/100)) + 14839.02
    print("tax is taking from you is(zloty):", round(b))
else:
    print("please enter a valid value")
