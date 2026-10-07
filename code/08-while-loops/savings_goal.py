goal = float(input("How much do you want to save? "))
weekly = float(input("How much can you save each week? "))

saved = 0
week = 0
while saved < goal:
    week += 1
    saved += weekly
    print(f"Week {week}: saved {saved:.2f}")

print(f"You reach your goal of {goal:.2f} after {week} weeks.")

answer = ""
while answer != "yes" and answer != "no":
    answer = input("Want to save the same again? (yes/no) ").strip().lower()

if answer == "yes":
    print(f"That's {goal * 2:.2f} after {week * 2} weeks.")
else:
    print("Enjoy your purchase!")
