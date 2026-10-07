---
title: For Loops and range()
summary: Repeat code a set number of times with for and range(), and step through every character of a string.
date: 2026-10-07
---

## Why this matters

In lesson 8 you used `while` to repeat something until a condition changed. Very often, though, you know exactly how many times to repeat: print 10 lines of a times table, count down from 5, check every letter in a word. A `for` loop does this with less code and no risk of forgetting to update a counter.

## The concept, step by step

### Looping over a string

A `for` loop takes each item from a sequence, one at a time, and runs its block once per item. A string is a sequence of characters:

```python
for letter in "cat":
    print(letter)
```

Output:

```text
c
a
t
```

On the first pass, `letter` is `"c"`. On the second it's `"a"`, then `"t"`. When there are no characters left, the loop ends. You choose the name of the loop variable, so pick one that describes each item.

### Repeating with range()

`range()` produces a sequence of numbers to loop over. With one number, it starts at 0 and stops just before that number:

```python
for i in range(3):
    print("Hip hip hooray!")
```

Output:

```text
Hip hip hooray!
Hip hip hooray!
Hip hip hooray!
```

`range(3)` gives 0, 1 and 2, so that's three passes. `i` is a common name for a loop counter when you just need to count.

### Start, stop and step

`range()` can take up to three numbers: where to start, where to stop (not included) and how big each step is:

```python
for number in range(2, 6):
    print(number)
```

Output:

```text
2
3
4
5
```

```python
for number in range(0, 10, 2):
    print(number)
```

Output:

```text
0
2
4
6
8
```

A negative step counts down: `range(5, 0, -1)` gives 5, 4, 3, 2 and 1.

The "stop is not included" rule is the same one you saw with string slices in lesson 4. So `range(1, 11)` gives 1 to 10.

### Building a result inside a loop

The running-total pattern from lesson 8 works in `for` loops too. Here we add up the numbers 1 to 100:

```python
total = 0
for number in range(1, 101):
    total += number
print(total)
```

Output:

```text
5050
```

You can also put an `if` inside the loop to count only some items, as you'll see in the full example below.

### for or while?

- Use `for` when you know how many times to repeat, or you're going through every item of something.
- Use `while` when you repeat until something happens, like a correct guess.

## Common mistakes

### Stopping one number too early

```python
for i in range(1, 5):
    print(i)
```

```text
1
2
3
4
```

If you wanted 1 to 5, this is one short, because the stop value is never included. Use `range(1, 6)`.

### Passing a string to range()

```python
count = input("How many? ")
for i in range(count):
    print("Hi")
```

After typing 3:

```text
TypeError: 'str' object cannot be interpreted as an integer
```

`input()` returns a string, as you saw in lesson 5. Convert it first: `count = int(input("How many? "))`.

### Resetting the total inside the loop

```python
for number in range(1, 4):
    total = 0
    total += number
print(total)
```

```text
3
```

You expected 6, but `total` goes back to 0 on every pass. Set it up once, *before* the loop starts.

## Putting it together

A script that prints a times table, adds it up, counts the vowels in a word and finishes with a countdown:

```python
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
```

Output (after typing 7 and Banana):

```text
Which times table? 7
The 7 times table:
1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
4 x 7 = 28
5 x 7 = 35
6 x 7 = 42
7 x 7 = 49
8 x 7 = 56
9 x 7 = 63
10 x 7 = 70
Sum of the table: 385
Type a word: Banana
'Banana' has 6 letters and 3 vowels.
Countdown:
5
4
3
2
1
Lift off!
```

The vowel check is long. In lesson 10 you'll learn the `in` keyword, which shortens it a lot.

## Exercise

Write a script called `stars.py` that draws with characters.

- Ask the user for a number of rows.
- Print a triangle with that many rows: 1 star on the first row, 2 on the second, and so on.
- Then print the same triangle upside down.
- Finally, ask for a word and print it with each letter on its own line, in capitals.

Hint: `"*" * 3` gives `***`, as you saw in lesson 4. Use `range(1, rows + 1)` to count up and a negative step to count down.

## Recap

- A `for` loop runs its block once for every item in a sequence.
- Looping over a string gives you one character at a time.
- `range(stop)`, `range(start, stop)` and `range(start, stop, step)` make sequences of numbers, and `stop` is never included.
- Set up totals and counters before the loop, and update them inside it.
- Use `for` for a known number of repeats, and `while` for "until something happens".

## Code for this lesson

The code for this lesson is in code/09-for-loops/.
