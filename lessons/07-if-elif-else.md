---
title: If, Elif, Else
summary: Make your programs choose what to do with if, elif and else, and handle several possible cases cleanly.
date: 2026-10-04
---

## Why this matters

So far your programs have run every line, top to bottom, every time. Real programs react: show a warning when the battery is low, give a discount to members, print a different grade for each score. `if` statements are how a program makes those choices, using the booleans you learned in lesson 6.

## The concept, step by step

### The if statement

An `if` runs a block of code only when its condition is `True`:

```python
cart_total = 42.50
if cart_total >= 50:
    print("Free delivery!")
print("Thanks for shopping.")
```

Output:

```text
Thanks for shopping.
```

Three details matter:

- The line ends with a colon `:`.
- The code that belongs to the `if` is **indented** by 4 spaces. That indented block is the only part that's skipped.
- The last line isn't indented, so it always runs.

Change `cart_total` to `60` and both lines will print.

### Adding else

`else` gives the program something to do when the condition is `False`:

```python
temperature = 12
if temperature >= 20:
    print("T-shirt weather.")
else:
    print("Bring a jacket.")
```

Output:

```text
Bring a jacket.
```

Exactly one of the two blocks runs, never both and never neither. `else` has no condition of its own, and it lines up with its `if`.

### Several choices with elif

When there are more than two possibilities, add `elif` (short for "else if"):

```python
battery = 35
if battery >= 80:
    print("Battery full.")
elif battery >= 20:
    print("Battery OK.")
else:
    print("Battery low, plug in soon!")
```

Output:

```text
Battery OK.
```

Python checks each condition from top to bottom and runs the **first** block whose condition is `True`. Then it skips the rest. You can have as many `elif` branches as you like, and the `else` at the end is optional.

### Combining conditions

Any boolean expression from lesson 6 can be a condition, including `and`, `or`, `not` and chained comparisons:

```python
age = 15
has_permission = True
if age >= 16 or has_permission:
    print("You can join the climbing trip.")
```

Output:

```text
You can join the climbing trip.
```

You can also put an `if` inside another `if` by indenting it further, but combining conditions with `and` is usually easier to read.

## Common mistakes

### Forgetting the colon

```python
if score > 50
    print("Pass")
```

```text
SyntaxError: expected ':'
```

Every `if`, `elif` and `else` line ends with a colon.

### Forgetting to indent

```python
if True:
print("Hello")
```

```text
IndentationError: expected an indented block after 'if' statement on line 1
```

Python uses indentation to know which lines belong to the `if`. Indent them by 4 spaces. Most editors do this for you when you press Enter after a colon.

### Indenting inconsistently

```python
if True:
    print("One")
      print("Two")
```

```text
IndentationError: unexpected indent
```

All lines in the same block must line up exactly. Stick to 4 spaces everywhere.

### Putting the conditions in the wrong order

```python
score = 85
if score >= 70:
    print("Pass")
elif score >= 80:
    print("Merit")
```

```text
Pass
```

85 deserved "Merit", but `score >= 70` was checked first, was `True`, and the rest was skipped. When ranges overlap, check the strictest condition first: `>= 80` before `>= 70`.

## Putting it together

A grade report that reads a score from the user, checks it's valid, picks a grade and tells a failing student how far they are from passing:

```python
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
```

Output (after typing Maya and 48):

```text
Student name: Maya
Exam score (0-100): 48
Maya: F - let's practise and try again.
Maya needs 12 more points to pass.
```

Output (after typing Maya and 95):

```text
Student name: Maya
Exam score (0-100): 95
Maya: A - excellent work!
```

The second `if` is separate from the first chain, so it's checked on its own. The invalid-score check comes first, so a score like 120 never gets an "A".

## Exercise

Write a script called `ticket_price.py` for a cinema.

- Ask the user for their age, and whether they're a student (they type `yes` or `no`).
- Children under 12 pay 6.00, people 65 and over pay 7.00, and everyone else pays 11.00.
- Students who aren't children or seniors get 3.00 off.
- If the age is negative, print an error message instead of a price.
- Print the final price with 2 decimal places.

Hint: get the base price with `if`/`elif`/`else`, then use a second `if` for the student discount. Compare the answer with `.strip().lower() == "yes"`.

## Recap

- `if condition:` runs the indented block only when the condition is `True`.
- `else:` runs when none of the conditions above it were `True`.
- `elif` adds more choices, and only the first matching branch runs.
- Indentation (4 spaces) decides which lines belong to a block.
- When ranges overlap, check the strictest condition first.

## Code for this lesson

The code for this lesson is in code/07-if-elif-else/.
