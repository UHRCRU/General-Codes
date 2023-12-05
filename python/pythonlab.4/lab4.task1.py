while True:
    a = float(input("enter the amount of point you take from exam"))
    if a > 100 or a < -10:
        print("please enter a valid value")
        continue

    elif a > 50:
        print("You passed the exam")
        break
    else:
        print("You failed the exam")
    exit()
