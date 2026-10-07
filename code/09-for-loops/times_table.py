number = int(input("Which times table? "))

print(f"The {number} times table:")
for i in range(1, 11):
    print(f"{i} x {number} = {i * number}")

total = 0
for i in range(1, 11):
    total += i * number
print(f"Sum of the table: {total}")

word = input("Type a word: ")
vowels = 0
for letter in word.lower():
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowels += 1
print(f"'{word}' has {len(word)} letters and {vowels} vowels.")

print("Countdown:")
for seconds in range(5, 0, -1):
    print(seconds)
print("Lift off!")
