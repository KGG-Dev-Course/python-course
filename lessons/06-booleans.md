---
title: Booleans and Comparisons
summary: Compare values and combine conditions with and, or and not to get True or False answers.
date: 2026-10-04
---

## Why this matters

Programs constantly ask yes-or-no questions. Is the password correct? Is the user old enough? Is the cart over the free-delivery limit? In Python, each of those questions produces a boolean, and booleans are what let a program make decisions, which you'll do in the next lesson.

## The concept, step by step

### True and False

You met the `bool` type in lesson 2. It has exactly two values, `True` and `False`, always with a capital first letter:

```python
is_member = True
has_paid = False
print(is_member, has_paid)
print(type(is_member))
```

Output:

```text
True False
<class 'bool'>
```

You can type booleans yourself, but most of the time they come from comparisons.

### Comparison operators

A comparison asks a question about two values and answers with `True` or `False`:

```python
print(5 == 5, 5 != 3, 3 < 2, 10 >= 10)
```

Output:

```text
True True False True
```

- `==` equal to
- `!=` not equal to
- `<` less than and `>` greater than
- `<=` less than or equal to and `>=` greater than or equal to

Remember the difference: a single `=` *stores* a value, while a double `==` *asks* whether two values are equal.

You can store the answer in a variable, just like any other value:

```python
cart_total = 54.90
free_delivery = cart_total >= 50
print(f"Free delivery: {free_delivery}")
```

Output:

```text
Free delivery: True
```

### Comparing strings

`==` works on text too, but it's exact, including capitals. `<` and `>` compare strings alphabetically:

```python
print("apple" == "Apple", "apple" < "banana", "Zebra" < "apple")
```

Output:

```text
False True True
```

That last one is surprising: every capital letter sorts before every lowercase one. When comparing what users type, clean it up first with `.lower()` from lesson 4.

### Combining with and, or, not

Three keywords combine booleans:

```python
print(True and False, True or False, not True)
```

Output:

```text
False True False
```

- `and` is `True` only if **both** sides are `True`.
- `or` is `True` if **at least one** side is `True`.
- `not` flips `True` to `False` and back.

Python also lets you chain comparisons, which reads just like maths:

```python
age = 25
print(18 <= age < 65)
```

Output:

```text
True
```

## Common mistakes

### Using = instead of ==

```python
x = 5
print(x = 5)
```

```text
TypeError: print() got an unexpected keyword argument 'x'
```

A single `=` is for storing values, not comparing them. Write `print(x == 5)`.

### Comparing a number with text

```python
print(5 == "5")
```

```text
False
```

No error, just a wrong answer. The number 5 and the string `"5"` are different values. This often happens with `input()`, so convert first with `int()` as in lesson 5.

And ordering a number against text doesn't work at all:

```python
print(1 < "2")
```

```text
TypeError: '<' not supported between instances of 'int' and 'str'
```

### Comparing floats with ==

```python
print(0.1 + 0.2 == 0.3)
```

```text
False
```

Remember the tiny float errors from lesson 3. Round before comparing: `round(0.1 + 0.2, 2) == 0.3` is `True`.

## Putting it together

A cinema checks whether a visitor can get into the late show and whether they get a discount:

```python
age = 16
has_ticket = True
with_adult = False
ticket_type = "student"

is_adult = age >= 18
can_enter = has_ticket and (is_adult or with_adult)
gets_discount = ticket_type == "student" or age < 12

print(f"Age {age}, adult: {is_adult}")
print(f"Has ticket: {has_ticket}, with adult: {with_adult}")
print(f"Can enter the late show: {can_enter}")
print(f"Gets a discount: {gets_discount}")
print(f"Needs an adult to come along: {not is_adult and not with_adult}")
```

Output:

```text
Age 16, adult: False
Has ticket: True, with adult: False
Can enter the late show: False
Gets a discount: True
Needs an adult to come along: True
```

The brackets in `can_enter` matter: the visitor needs a ticket *and* must be either an adult or with one. Try changing `with_adult` to `True` and running it again.

## Exercise

Write a script called `password_check.py` that checks a new password.

- Ask the user for a password with `input()`.
- Create these booleans and print each one: `long_enough` (at least 8 characters), `not_simple` (it isn't `"password"`, in any capitals) and `has_number_at_end` (its last character is a digit).
- Print `Strong password: True` only if all three are `True`.

Hint: `len()` and `.lower()` from lesson 4 will help. For the last character, `text[-1]` gives it, and `"0" <= text[-1] <= "9"` checks it's a digit.

## Recap

- A boolean is `True` or `False`.
- `==`, `!=`, `<`, `>`, `<=` and `>=` compare values and return a boolean.
- `=` stores a value, `==` compares two values.
- `and`, `or` and `not` combine conditions, and brackets control which goes first.
- Watch out for numbers versus strings, and for floats compared with `==`.

## Code for this lesson

The code for this lesson is in code/06-booleans/.
