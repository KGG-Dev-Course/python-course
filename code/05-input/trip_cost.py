destination = input("Where are you going? ")
distance = float(input("How many km is the round trip? "))
efficiency = float(input("How many km does your car do per litre? "))
fuel_price = float(input("Price of fuel per litre? "))
people = int(input("How many people are sharing the cost? "))

litres = distance / efficiency
cost = litres * fuel_price
share = cost / people

print(f"Trip to {destination.strip().title()}")
print(f"Fuel needed: {litres:.1f} litres")
print(f"Total fuel cost: {cost:.2f}")
print(f"Each person pays: {share:.2f}")
