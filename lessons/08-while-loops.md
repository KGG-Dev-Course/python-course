---
title: While Loops
summary: Repeat code with while loops for as long as a condition holds, and keep asking until the user gives a valid answer.
date: 2026-10-07
---

## Why this matters

Lots of tasks mean "keep doing this until something changes": keep saving until you hit your goal, keep asking until the user types a valid answer, keep a game running until the player quits. Writing the same line a hundred times isn't an option. A `while` loop lets one block of code run again and again, for as long as you need.

## The concept, step by step

### The while loop

A `while` loop looks a lot like the `if` from lesson 7. The difference is that it goes back and checks the condition again after the block runs:

```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")
```

Output:

```text
3
2
1
Go!
```

Here's what happens:

1. Python checks `count > 0`. It's `True`, so the indented block runs.
2. The block prints `count` and makes it one smaller.
3. Python jumps back up and checks the condition again.
4. When `count` reaches 0, the condition is `False`, so the loop ends and the program moves on to `print("Go!")`.

Each pass through the block is called an **iteration**.

### Something must change

For a loop to end, something inside it has to change the condition. In the countdown, `count -= 1` does that job. Every `while` loop needs an answer to the question: "What makes this condition eventually become `False`?"

### Counting and adding up

A very common pattern is to keep a running total and a counter in variables that you update on each pass:

```python
saved = 0
week = 0
while saved < 100:
    week += 1
    saved += 30
print(f"Saved {saved} after {week} weeks")
```

Output:

```text
Saved 120 after 4 weeks
```

You don't know in advance how many weeks it takes, and you don't need to. The loop simply runs until the goal is reached. That's exactly what `while` loops are best at.

### Asking until the answer is valid

You can use `input()` inside a loop to keep asking until the user types something sensible:

```python
answer = ""
while answer != "yes" and answer != "no":
    answer = input("Continue? (yes/no) ").strip().lower()
print(f"You chose {answer}.")
```

Output (after typing maybe, then YES):

```text
Continue? (yes/no) maybe
Continue? (yes/no) YES
You chose yes.
```

`answer` starts as an empty string so the condition is `True` the first time, and the loop runs at least once. The `.strip().lower()` from lesson 4 means `YES` and ` yes ` both count.

## Common mistakes

### The infinite loop

```python
count = 3
while count > 0:
    print(count)
```

This prints `3` forever, because nothing ever changes `count`. If your program seems stuck, press **Ctrl+C** in the terminal to stop it. Then add the missing update, `count -= 1`, inside the loop.

### Updating outside the loop

```python
count = 3
while count > 0:
    print(count)
count -= 1
```

This is another infinite loop. `count -= 1` isn't indented, so it isn't part of the loop and only runs after the loop ends, which never happens. Indent it to the same level as the `print()`.

### A condition that's never True

```python
answer = "yes"
while answer != "yes" and answer != "no":
    answer = input("Continue? (yes/no) ")
print("Done")
```

```text
Done
```

The question is never asked, because `answer` already holds `"yes"`, so the condition is `False` from the start. Give the variable a starting value that makes the loop run, such as an empty string.

## Putting it together

A savings planner that shows your progress week by week, then asks a yes/no question until it gets a valid answer:

```python
goal = float(input("How much do you want to save? "))
weekly = float(input("How much can you save each week? "))

saved = 0
week = 0
while saved < goal:
    week += 1
    saved += weekly
    print(f"Week {week}: saved {saved:.2f}")

print(f"You reach your goal of {goal:.2f} after {week} weeks.")

answer = ""
while answer != "yes" and answer != "no":
    answer = input("Want to save the same again? (yes/no) ").strip().lower()

if answer == "yes":
    print(f"That's {goal * 2:.2f} after {week * 2} weeks.")
else:
    print("Enjoy your purchase!")
```

Output (after typing 100, 30 and YES):

```text
How much do you want to save? 100
How much can you save each week? 30
Week 1: saved 30.00
Week 2: saved 60.00
Week 3: saved 90.00
Week 4: saved 120.00
You reach your goal of 100.00 after 4 weeks.
Want to save the same again? (yes/no) YES
That's 200.00 after 8 weeks.
```

The first loop counts and adds up. The second keeps asking until the answer is valid. Then a plain `if`/`else` from lesson 7 uses the result. Be careful if you try it yourself with 0 as the weekly amount: `saved` would never grow, and you'd have an infinite loop.

## Exercise

Write a script called `guessing_game.py`.

- Store a secret number between 1 and 20 in a variable, for example `secret = 13`.
- Keep asking the user to guess until they get it right.
- After each wrong guess, print `Too high` or `Too low`.
- When they get it, print how many guesses they took.

Hint: start with `guess = 0` so the loop runs at least once, and use a counter variable that goes up by 1 on every guess. Remember to convert each guess with `int()`.

## Recap

- A `while` loop repeats its indented block as long as its condition is `True`.
- Something inside the loop must change, or it runs forever. Press Ctrl+C to stop a stuck program.
- Counters and running totals are updated with `+=` on each pass.
- Use a `while` loop with `input()` to keep asking until the answer is valid.
- Reach for `while` when you don't know in advance how many times to repeat.

## Code for this lesson

The code for this lesson is in code/08-while-loops/.
