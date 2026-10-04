pizza_price = 18.50
drinks_price = 7.25
friends = 4
slices = 14

total = pizza_price + drinks_price
tip = total * 0.15
grand_total = total + tip
per_person = grand_total / friends

print(f"Food and drinks: {total}")
print(f"Tip (15%): {round(tip, 2)}")
print(f"Grand total: {round(grand_total, 2)}")
print(f"Each person pays: {round(per_person, 2)}")

# Floor division gives whole slices; % gives what's left over
print(f"Slices each: {slices // friends}")
print(f"Slices left over: {slices % friends}")
