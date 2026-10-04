---
title: Working with Strings
summary: Join, slice, clean up and format text in Python using indexes, string methods and f-strings.
date: 2026-10-04
---

## Why this matters

Most of the data you'll handle is text: names, messages, addresses, product titles. Real text is messy, with stray spaces and random capitals. In this lesson you'll learn to pull text apart, clean it up and put it back together the way you want.

## The concept, step by step

### Joining and repeating

You met strings in lesson 2. The `+` operator joins two strings, and `*` repeats one:

```python
greeting = "Hello, " + "Maya"
print(greeting)
print("na" * 4 + " Batman")
```

Output:

```text
Hello, Maya
nananana Batman
```

### Indexing: one character at a time

Each character in a string has a position, called its **index**. Counting starts at 0, not 1. Negative numbers count from the end:

```python
word = "Python"
print(word[0], word[1], word[-1])
print(len(word))
```

Output:

```text
P y n
6
```

`len()` gives the number of characters. Because counting starts at 0, the last index is always one less than the length.

### Slicing: a piece of a string

Put a colon between two indexes to take a **slice**. The slice starts at the first index and stops *just before* the second:

```python
word = "Python"
print(word[0:3])
print(word[2:])
print(word[:2])
```

Output:

```text
Pyt
thon
Py
```

Leave out the start to begin at 0, or leave out the end to go to the last character.

### String methods

Strings come with built-in tools called **methods**. You call one by writing a dot after the string:

```python
print("pizza".upper())
print("Hello World".lower())
print("ada lovelace".title())
print("  hi  ".strip())
print("i love tea".replace("tea", "coffee"))
print("Python".find("th"))
```

Output:

```text
PIZZA
hello world
Ada Lovelace
hi
i love coffee
2
```

- `upper()`, `lower()` and `title()` change capitals.
- `strip()` removes spaces from both ends.
- `replace(old, new)` swaps one piece of text for another.
- `find(text)` returns the index where `text` starts.

Methods never change the original string. They hand you back a **new** one.

### Formatting numbers in f-strings

You've used f-strings since lesson 1. Add a colon and a format inside the braces to control how numbers look. `.2f` means "a float with 2 decimal places", which is perfect for money:

```python
price = 7.4
print(f"Each person pays: {price:.2f}")
print(f"Big number: {1234567:,}")
```

Output:

```text
Each person pays: 7.40
Big number: 1,234,567
```

That fixes the `7.4` you saw at the end of lesson 3.

## Common mistakes

### Indexing past the end

```python
print("hello"[5])
```

```text
IndexError: string index out of range
```

"hello" has 5 characters, so its indexes are 0 to 4. Use `"hello"[4]` or `"hello"[-1]` for the last letter.

### Trying to change one character

```python
message = "hi"
message[0] = "H"
```

```text
TypeError: 'str' object does not support item assignment
```

Strings can't be changed in place. Build a new string instead: `message = "H" + message[1:]`.

### Forgetting to store a method's result

```python
name = "  Ann "
name.strip()
print(f"[{name}]")
```

```text
[  Ann ]
```

`strip()` returned a clean copy, but nothing kept it. Assign it back: `name = name.strip()`.

### Joining a string and a number

```python
print("Score: " + 10)
```

```text
TypeError: can only concatenate str (not "int") to str
```

`+` only joins strings to strings. Use an f-string instead: `print(f"Score: {10}")`.

## Putting it together

Here's a conference badge made from a messy name:

```python
raw_name = "   ada LOVELACE  "
role = "guest speaker"

name = raw_name.strip().title()
initials = name[0] + name[4]
badge_line = f"{name} - {role.upper()}"

print(badge_line)
print("-" * len(badge_line))
print(f"Initials: {initials}")
print(f"Name length: {len(name)} characters")
print(f"First name: {name[:3]}")
print(f"Short role: {role.replace('guest ', '')}")
```

Output:

```text
Ada Lovelace - GUEST SPEAKER
----------------------------
Initials: AL
Name length: 12 characters
First name: Ada
Short role: speaker
```

`raw_name.strip().title()` chains two methods: `strip()` runs first, then `title()` runs on its result. The dashes line is exactly as long as the badge because it uses `len(badge_line)`.

## Exercise

Write a script called `username.py` that turns a messy full name into a username.

- Start with `full_name = "  grace HOPPER "`.
- Clean it so it reads `Grace Hopper`, and print it.
- Build a username from the first letter of the first name plus the whole last name, all in lowercase, for example `ghopper`.
- Print the username and how many characters it has.
- Print a line of `=` signs as long as the username.

Hint: after cleaning, `find(" ")` tells you where the space is. Slice after it to get the last name.

## Recap

- `+` joins strings and `*` repeats them.
- Indexes start at 0, and negative indexes count from the end.
- `text[start:end]` takes a slice that stops just before `end`.
- Methods like `strip()`, `lower()` and `replace()` return new strings, so store the result.
- `{value:.2f}` in an f-string shows a number with 2 decimal places.

## Code for this lesson

The code for this lesson is in code/04-strings/.
