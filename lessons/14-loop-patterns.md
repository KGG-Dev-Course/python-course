---
title: "Loop Patterns: enumerate, zip, break, continue"
summary: Number items with enumerate, walk two lists together with zip, and control loops with break and continue.
date: 2026-11-17
---

## Why this matters

You've written plenty of `for` loops by now, and some of them got a bit clumsy: `range(len(...))` just to get a position, or two lists kept in step by index. Python has a few small tools that make these everyday loops shorter and easier to read. You'll use them in almost every program you write from here on.

## The concept, step by step

### enumerate: position and value together

In lesson 10 you used `range(len(scores))` when you needed each item's position. `enumerate()` gives you the position and the value at the same time:

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```text
0 apple
1 banana
2 cherry
```

Each step of the loop gets a pair, `(index, fruit)`, which is unpacked into two variables just like the tuples in lesson 11.

People usually count from 1, not 0. Pass `start=1` to change where the numbers begin:

```python
fruits = ["apple", "banana", "cherry"]
for number, fruit in enumerate(fruits, start=1):
    print(f"{number}. {fruit}")
```

Output:

```text
1. apple
2. banana
3. cherry
```

### zip: two lists side by side

When two lists line up, such as items and their prices, `zip()` walks through both at once:

```python
items = ["milk", "bread", "eggs"]
prices = [1.2, 1.8, 2.5]
for item, price in zip(items, prices):
    print(f"{item}: {price:.2f}")
```

Output:

```text
milk: 1.20
bread: 1.80
eggs: 2.50
```

`zip()` pairs the first item with the first price, the second with the second, and so on. The name comes from a zipper, which joins two sides tooth by tooth.

### break: stop the loop early

`break` ends the loop immediately, even if there are items left. Use it when you've found what you were looking for, or when continuing makes no sense:

```python
orders = [12, 0, 7, -1, 30]
for qty in orders:
    if qty < 0:
        print("Bad order, stopping")
        break
    print(f"Order of {qty}")
print("Done")
```

Output:

```text
Order of 12
Order of 0
Order of 7
Bad order, stopping
Done
```

The `30` never gets processed. After `break`, Python jumps to the first line after the loop. `break` works in `while` loops too.

### continue: skip to the next item

`continue` skips the rest of the current step and moves on to the next item. It's handy for ignoring values you don't care about:

```python
orders = [12, 0, 7, -1, 30]
for qty in orders:
    if qty < 0:
        print("Bad order, stopping")
        break
    if qty == 0:
        continue
    print(f"Packing {qty} items")
print("Done")
```

Output:

```text
Packing 12 items
Packing 7 items
Bad order, stopping
Done
```

The empty order (`0`) is skipped without printing anything, and the loop carries on with `7`.

## Common mistakes

### Forgetting to unpack enumerate

```python
fruits = ["apple", "banana"]
for fruit in enumerate(fruits):
    print(fruit.upper())
```

```text
AttributeError: 'tuple' object has no attribute 'upper'
```

Without two variables, each `fruit` is a whole tuple like `(0, 'apple')`. Write `for index, fruit in enumerate(fruits):` to unpack it.

### Expecting zip to warn about different lengths

```python
names = ["Maya", "Leo", "Sam"]
scores = [88, 72]
for name, score in zip(names, scores):
    print(name, score)
```

Output:

```text
Maya 88
Leo 72
```

Sam silently disappears. `zip()` stops as soon as the shorter list runs out, with no error. If the lengths might differ, check first: `if len(names) != len(scores):` and print a warning.

### Putting break in the wrong place

```python
for number in range(1, 4):
    print(number)
    break
```

Output:

```text
1
```

The loop was meant to print 1, 2 and 3, but `break` runs on the very first step. `break` and `continue` almost always belong inside an `if`, so they only run when a condition is true.

## Putting it together

A race results board, plus a search that stops as soon as it finds the runner:

```python
runners = ["Maya", "Leo", "Sam", "Ana", "Kai"]
times = [41.5, 39.2, 0, 44.8, 52.3]  # minutes, 0 means did not finish
limit = 50

print("Race results")
for bib, (name, time) in enumerate(zip(runners, times), start=1):
    if time == 0:
        print(f"#{bib} {name}: did not finish")
        continue
    if time <= limit:
        status = "qualified"
    else:
        status = "over the limit"
    print(f"#{bib} {name}: {time:.1f} min ({status})")

search = input("Find a runner: ").strip().title()
found = False
for name, time in zip(runners, times):
    if name == search:
        found = True
        break
if found:
    print(f"{name} finished in {time:.1f} min")
else:
    print(f"No runner called {search}")
```

Output (after typing ana):

```text
Race results
#1 Maya: 41.5 min (qualified)
#2 Leo: 39.2 min (qualified)
#3 Sam: did not finish
#4 Ana: 44.8 min (qualified)
#5 Kai: 52.3 min (over the limit)
Find a runner: ana
Ana finished in 44.8 min
```

The first loop combines both tools: `zip()` makes `(name, time)` pairs, and `enumerate()` numbers those pairs. The brackets in `bib, (name, time)` unpack both levels at once. In the search, `break` stops the loop on a match, so `name` and `time` still hold that runner's values afterwards. The `found` flag tells you whether the loop ended because of a match or because it ran out of runners.

## Exercise

Write a script called `quiz.py` that runs a short quiz.

- Make a list of three or more questions and a matching list of answers.
- Loop over them with `zip()` and `enumerate()`, showing each question with its number, like `Question 1: ...`.
- If the user types `skip`, move on to the next question without checking it.
- If the user types `quit`, stop the quiz immediately.
- At the end, print how many answers were correct.

Hint: compare answers with `.strip().lower()` on both sides so `Paris` and ` paris` both count. Use `continue` for skip and `break` for quit.

## Recap

- `enumerate(items, start=1)` gives you a number and a value on each step.
- `zip(a, b)` walks two lists together, and stops at the end of the shorter one.
- `break` ends a loop immediately. `continue` skips to the next step.
- Put `break` and `continue` inside an `if`.
- These tools work together: `enumerate(zip(a, b))` numbers pairs.

## Code for this lesson

The code for this lesson is in code/14-loop-patterns/.
