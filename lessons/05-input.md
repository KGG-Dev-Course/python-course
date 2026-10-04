---
title: Getting User Input and Type Conversion
summary: Ask the user for values, turn their answers into numbers, and build small interactive calculators.
date: 2026-10-04
---

## Why this matters

A program that always prints the same thing isn't very useful. Once you can ask the user for values and do maths with them, you can build real tools: a tip calculator, a unit converter, a trip planner. The key is one small idea: everything the user types arrives as text.

## The concept, step by step

### input() always gives you a string

You used `input()` in lesson 1 to ask for a name. Here's the catch: it returns a `str`, even if the user types digits.

```python
age = input("How old are you? ")
print(type(age))
```

Output (after typing 17):

```text
How old are you? 17
<class 'str'>
```

So `age` holds the text `"17"`, not the number 17. As you saw in lesson 2, you can't do maths with text.

### Converting with int(), float() and str()

Python has a function named after each type that converts a value into that type:

```python
print(int("42") + 8)
print(float("3.5") * 2)
print(str(25) + " years")
```

Output:

```text
50
7.0
25 years
```

- `int()` turns text like `"42"` into a whole number.
- `float()` turns text like `"3.5"` into a decimal number.
- `str()` turns a number back into text.

`int()` also ignores spaces around the digits, so `int(" 12 ")` gives `12`.

### Converting the answer straight away

The usual pattern is to wrap `input()` in the conversion you need, so the variable holds a number from the start:

```python
price = float(input("Bill total: "))
tip_percent = int(input("Tip percent: "))

tip = price * tip_percent / 100
print(f"Tip: {tip:.2f}")
print(f"Total: {price + tip:.2f}")
```

Output (after typing 40 and 15):

```text
Bill total: 40
Tip percent: 15
Tip: 6.00
Total: 46.00
```

Python runs the inside first: `input()` gets the text, then `float()` converts it. Use `float()` when the user might type a decimal, and `int()` when only whole numbers make sense, like a count of people.

### Converting between numbers

The same functions work on numbers too:

```python
print(int(9.99))
print(round(9.99))
print(float(7))
```

Output:

```text
9
10
7.0
```

Be careful: `int()` doesn't round, it just chops off the decimal part. Use `round()` from lesson 3 if you want the nearest whole number.

## Common mistakes

### Doing maths on the raw input

```python
age = input("Age? ")
print(age + 1)
```

```text
TypeError: can only concatenate str (not "int") to str
```

`age` is still a string. Convert it first: `age = int(input("Age? "))`.

### Adding two inputs and getting them glued together

```python
first = input("First number: ")
second = input("Second number: ")
print(first + second)
```

If you type 7 and 3, you get:

```text
73
```

There's no error, which makes this one sneaky. `+` on two strings joins them. Convert both with `int()` and you'll get `10`.

### Using int() on a decimal or a word

```python
int("3.5")
```

```text
ValueError: invalid literal for int() with base 10: '3.5'
```

`int()` only accepts text that looks like a whole number. If the user might type a decimal, use `float()`. If they type a word like `ten`, you get the same `ValueError`, and the program stops. We'll learn how to catch that error and ask again in lesson 19.

## Putting it together

Here's a calculator that splits the fuel cost of a road trip between friends:

```python
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
```

Output (after typing porto, 320, 15, 1.85 and 3):

```text
Where are you going? porto
How many km is the round trip? 320
How many km does your car do per litre? 15
Price of fuel per litre? 1.85
How many people are sharing the cost? 3
Trip to Porto
Fuel needed: 21.3 litres
Total fuel cost: 39.47
Each person pays: 13.16
```

The destination stays a string, and the string methods from lesson 4 tidy it up. Every number is converted the moment it's read.

## Exercise

Write a script called `converter.py` that converts a temperature.

- Ask the user for their name and a temperature in Celsius.
- Convert it to Fahrenheit with the formula `celsius * 9 / 5 + 32`.
- Print a friendly message using their name, with the result to 1 decimal place, for example `Maya, 21.5 C is 70.7 F`.
- Then ask for a number of days and print how many weeks and leftover days that is.

Hint: Celsius can be a decimal, so use `float()`. Days are whole, so use `int()`, then reach for `//` and `%` from lesson 3.

## Recap

- `input()` always returns a string, even when the user types digits.
- `int()`, `float()` and `str()` convert values between types.
- Wrap the input straight away: `float(input("..."))`.
- `int()` chops off decimals instead of rounding.
- Converting text that doesn't look like a number raises a `ValueError`.

## Code for this lesson

The code for this lesson is in code/05-input/.
