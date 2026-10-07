shopping = ["milk", "eggs", "bread"]
prices = [1.20, 2.50, 1.80]

shopping.append("apples")
prices.append(3.10)
shopping.insert(0, "coffee")
prices.insert(0, 4.75)

shopping.remove("bread")
prices.pop(3)

print(f"You need {len(shopping)} items:")
for i in range(len(shopping)):
    print(f"{i + 1}. {shopping[i]} - {prices[i]:.2f}")

print(f"Total: {sum(prices):.2f}")
print(f"Cheapest item costs {min(prices):.2f}, dearest {max(prices):.2f}")

if "milk" in shopping:
    print("Don't forget the milk!")

shopping.sort()
print(f"Sorted for the shop: {shopping}")
