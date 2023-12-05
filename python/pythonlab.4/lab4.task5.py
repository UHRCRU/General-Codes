while True:
      try:
            year = int(input("please enter a year between 1900 and 2099"))
      except ValueError:
            print("your value needs to be integer")
            continue
      if year < 1900:
            print("your value is lower than 1900 please enter again")
            continue
      elif year > 2099:
            print("your value is higher than 2099 please enter again")
            continue
      else:
            #divide the number of the year by 19 and find the rest as a
            a = year%19
            #divide the number of the year by 4 and find the rest as b
            b = year%4
            #divide the number of the year by 7 and find the rest as c
            c = year%7
            #multiply the rest a by 19, add 24 to the product, divide the sum by 30 and find the rest as d
            d = ((a*19)+24)%30
            #divide the sum of (2b + 4c + 6d + 5) by 7 and find the rest as e
            e = (2*b + 4*c + 6*d + 5)%7
            if d + e < 10:
                  easter = d+e+22 #of march
                  if easter > 31:
                        easter = easter-31
                        print(easter, "of april")
                  elif easter > 61:
                        easter = easter - 61
                        print(easter,"of may")
                  else:
                        print(easter, "of march")
            else:
                  easter = d+e-9 #of april
                  if easter > 30:
                        easter = easter-30
                        print(easter, "of may")
                  elif easter <= 0:
                        easter = (31-easter)
                        print(easter, "of march")
                  else:
                        print(easter, "of april")
