---
title: Variables and Data Types
summary: Store values in well-named variables and tell apart text, whole numbers, decimals and True/False values.
date: 2026-10-04
---

## Why this matters

Every program you'll ever write needs to remember things: a player's score, the items in a cart, today's temperature. Variables are how Python remembers, and data types tell Python what kind of thing it's holding. Get these two ideas right and the rest of the course gets much easier.

## The concept, step by step

### Creating a variable

In lesson 1 you stored a name with `input()`. You can also store a value directly:

```python
city = "Lisbon"
print(city)
```

Output:

```text
Lisbon
```

The `=` sign means "store the value on the right in the name on the left". It is not "equals" like in maths. Think of a variable as a label you stick on a value so you can find it again later.

### Changing a variable

A variable can be given a new value at any time. The old value is simply replaced:

```python
score = 10
print(score)
score = 15
print(score)
```

Output:

```text
10
15
```

Python runs your code top to bottom, so `score` holds whatever was stored in it most recently.

### The four basic data types

Every value in Python has a **type**. These four are the ones you'll use constantly:

```python
city = "Lisbon"      # str: text, always in quotes
humidity = 68        # int: a whole number
temperature = 21.5   # float: a number with a decimal point
is_raining = False   # bool: either True or False
```

- **str** (string) is text. Single or double quotes both work.
- **int** (integer) is a whole number, with no quotes.
- **float** is a number with a decimal point.
- **bool** (boolean) is `True` or `False`, written with a capital letter and no quotes.

### Checking a type with type()

If you're ever unsure what type a value is, ask Python with `type()`:

```python
print(type("12"), type(12), type(12.0), type(True))
```

Output:

```text
<class 'str'> <class 'int'> <class 'float'> <class 'bool'>
```

Notice that `"12"` is a string, not a number, because of the quotes. That one detail causes a lot of beginner bugs, as you'll see below.

### Naming your variables

Variable names can use letters, digits and underscores, but they can't start with a digit. Python's style is lowercase words joined by underscores, called *snake_case*:

```python
first_name = "Ana"
items_in_cart = 3
```

Pick names that say what the value means. `items_in_cart` tells you far more than `x` or `n`.

## Common mistakes

### Mixing text and numbers

```python
print("5" + 3)
```

```text
TypeError: can only concatenate str (not "int") to str
```

`"5"` is text, and Python won't add text to a number. If you meant the number five, drop the quotes: `print(5 + 3)`. To put a number inside a sentence, use an f-string like `f"Total: {3}"`. We'll cover converting between types in lesson 5.

### Using a variable before creating it

```python
print(score)
score = 10
```

```text
NameError: name 'score' is not defined
```

Python reads top to bottom, so `score` doesn't exist yet on the first line. Create the variable first, then use it.

### Getting the capitals wrong

```python
Score = 10
print(score)
```

```text
NameError: name 'score' is not defined. Did you mean: 'Score'?
```

Names are case-sensitive: `Score` and `score` are two different variables. Stick to lowercase and you'll avoid this.

### Starting a name with a digit

```python
2nd_place = "Ana"
```

```text
SyntaxError: invalid decimal literal
```

Names can't start with a digit. Use `second_place` instead.

## Putting it together

Here's a small weather report that uses all four types and updates two of the values:

```python
city = "Lisbon"
temperature = 21.5
humidity = 68
is_raining = False

print(f"Weather report for {city}")
print(f"Temperature: {temperature} C")
print(f"Humidity: {humidity}%")
print(f"Raining: {is_raining}")

# The afternoon update changes two values
temperature = 24.0
is_raining = True

print("Afternoon update:")
print(f"Temperature: {temperature} C")
print(f"Raining: {is_raining}")

print(type(city), type(temperature), type(humidity), type(is_raining))
```

Output:

```text
Weather report for Lisbon
Temperature: 21.5 C
Humidity: 68%
Raining: False
Afternoon update:
Temperature: 24.0 C
Raining: True
<class 'str'> <class 'float'> <class 'int'> <class 'bool'>
```

## Exercise

Write a script called `profile.py` that describes a book you like.

- Create five variables: the title (str), the author (str), the year it was published (int), your rating out of 5 (float) and whether you'd recommend it (bool).
- Print each one on its own line using f-strings, like `Title: Dune`.
- Change your rating to a new value and print it again.
- Finish by printing the type of every variable.

Hint: look at how the weather report above is laid out, and copy its shape.

## Recap

- `name = value` stores a value in a variable; assigning again replaces it.
- The four basic types are `str`, `int`, `float` and `bool`.
- Quotes make a string, so `"12"` is text, not a number.
- `type()` tells you what type a value is.
- Use clear snake_case names that don't start with a digit.

## Code for this lesson

The code for this lesson is in code/02-variables/.
