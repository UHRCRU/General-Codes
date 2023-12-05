litres = float(input("How many litres did the car use? "))
kilometres= float(input("How many kilometres has the car travelled? "))
price= float(input("How much was a litre of fuel? "))
#somehow i need to turn my input to x/100 ratio or percentage
consumption = (litres/kilometres)*100
cost1km = price / (kilometres/litres)
print("Average fuel consumption:", consumption, "l/100km")
print("The cost of one kilometre:", cost1km,"PLN")
