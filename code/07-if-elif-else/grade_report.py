student = input("Student name: ")
score = int(input("Exam score (0-100): "))

if score < 0 or score > 100:
    print("That score isn't between 0 and 100.")
elif score >= 90:
    print(f"{student}: A - excellent work!")
elif score >= 80:
    print(f"{student}: B - very good.")
elif score >= 70:
    print(f"{student}: C - a solid pass.")
elif score >= 60:
    print(f"{student}: D - just passed.")
else:
    print(f"{student}: F - let's practise and try again.")

if 0 <= score < 60:
    print(f"{student} needs {60 - score} more points to pass.")
