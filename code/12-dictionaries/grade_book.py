grades = {"Maya": 88, "Leo": 72, "Sam": 95}

grades["Ana"] = 64
grades["Leo"] = 78
del grades["Sam"]

print(f"Students: {len(grades)}")
for name, score in grades.items():
    if score >= 80:
        result = "great"
    elif score >= 65:
        result = "pass"
    else:
        result = "needs help"
    print(f"{name}: {score} ({result})")

average = sum(grades.values()) / len(grades)
print(f"Class average: {average:.1f}")

lookup = input("Look up a student: ").strip().title()
print(f"{lookup}: {grades.get(lookup, 'not found')}")
