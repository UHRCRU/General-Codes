while True:
      try:
            a = float(input("Enter the amount of pure alcohol (mL)"))
            if a < 0:
                  print("please enter a valid value")
                  continue
            b = float(input("Enter your weight (kg)"))
            if b < 0:
                  print("please enter a valid value")
                  continue
            c = str(input("Enter m for man and enter w for woman"))
            #i guess i could make a boolean for gender input to make things easy but its working for now :D
            break
      except ValueError:
            print("please enter a valid value")
            continue
#3.174603174603175(woman)3.174603174603175
A = (a*(2/5))*(4/5)
if c == str("m"):
      K = 0.7
elif c==str("w"):
      K=0.6
else:
      print("Enter m for man and enter w for woman")
W = b

P: float = A/(K*W)

print("content of blood alcohol in per mille: ",round(P,2))
