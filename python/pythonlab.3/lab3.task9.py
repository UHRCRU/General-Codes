import math
while True:
    try:
        x = int(input("please choose to use which calculation ? (1, 2 or 3) for exit press 0"))
        """if x != 1 or 2 or 3 or 0:
            print("Just enter a valid input in INTEGER and just one of these for numbers to progress: 1, 2, 3 or 0")"""
    except ValueError:
        print("please enter a valid number of calculation (1, 2 or 3) and from this point if you enter any wrong input the program wont respond")
        continue
    if x == 1:
        #nr1
        a = float(input("Please, enter a value: "))
        #3x^3 - 2x^2 +3x - 1
        result1 = (3*(a**3))-(2*(a**2))+(3*a)-1
        print(result1)
    elif x == 2:
        #nr2
        b = float(input("Please, enter a value: "))
        result2 = ((b*b)/(math.pi*math.pi)*((b*b) + (1/2)))*(1+(b*b/((math.pi*math.pi)*(((b*b)-(1/2))*((b*b)-(1/2))))))
        print(result2)
        #i tried to make it but its not giving the same results from the lab.3.pdf i dunno why
    elif x == 3:
        #nr3
        c = float(input("Please, enter a value: "))
        result3 = 1/(c+(1/(c+(1/(c+(1/c))))))
        print(result3)
    elif x==0:
        print("leaving from the program, I AM THE PROGRAM")
        break
