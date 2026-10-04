---
title: Numbers and Math
summary: Do arithmetic in Python, control the order of operations, and round results so they're easy to read.
date: 2026-10-04
---

## Why this matters

Splitting a bill, working out a discount, converting a recipe for more people: a lot of useful programs are just a little bit of maths. In this lesson you'll make Python your calculator, and learn the few surprises that catch beginners out.

## The concept, step by step

### The basic operators

You already know `int` and `float` from lesson 2. Python does arithmetic on them with these operators:

```python
print(7 + 3, 7 - 3, 7 * 3, 7 / 3)
```

Output:

```text
10 4 21 2.3333333333333335
```

`+`, `-` and `*` work just like on paper. `/` is division, and it **always** gives a float, even when the answer is whole:

```python
print(8 / 2)
```

Output:

```text
4.0
```

### Floor division, remainder and powers

Three more operators are surprisingly handy:

```python
print(17 // 5, 17 % 5, 2 ** 10)
```

Output:

```text
3 2 1024
```

- `//` is **floor division**: divide and throw away the decimal part. 17 sweets shared by 5 kids gives 3 each.
- `%` is the **remainder** (often called *modulo*). After handing out 3 each, 2 sweets are left over.
- `**` raises to a power. `2 ** 10` is 2 multiplied by itself 10 times.

### Order of operations

Python follows the same rules you learned at school: powers first, then `*`, `/`, `//` and `%`, then `+` and `-`. Brackets go first of all.

```python
print(2 + 3 * 4, (2 + 3) * 4)
```

Output:

```text
14 20
```

When in doubt, add brackets. They cost nothing and make your intent obvious to whoever reads the code next.

### Rounding and absolute values

Two built-in functions help tidy up results:

```python
print(round(3.14159, 2), round(7.5), round(8.5), abs(-12))
```

Output:

```text
3.14 8 8 12
```

`round(number, digits)` rounds to that many decimal places. With no second argument it rounds to a whole number. Notice that both 7.5 and 8.5 become 8: when a number is exactly halfway, Python rounds to the nearest *even* number. `abs()` removes the minus sign, which is useful for "how far apart are these two values?"

### Updating a number

You'll often want to change a variable based on its old value. Python has a shortcut for that:

```python
points = 10
points = points + 5
points += 5
print(points)
```

Output:

```text
20
```

`points += 5` means exactly the same as `points = points + 5`. There are matching shortcuts `-=`, `*=` and `/=`.

For long numbers you can put underscores between digits to make them readable: `1_000_000` is one million.

## Common mistakes

### Expecting / to give a whole number

```python
boxes = 10 / 2
print(boxes)
```

```text
5.0
```

You wanted 5 boxes, not 5.0. If you need a whole number, use floor division: `10 // 2` gives `5`.

### Being surprised by tiny decimal errors

```python
print(0.1 + 0.2)
```

```text
0.30000000000000004
```

Computers store floats in binary, so some decimals can't be stored exactly. This isn't a bug in your code. When you show money or measurements, round them: `round(0.1 + 0.2, 2)` gives `0.3`.

### Forgetting the order of operations

```python
average = 80 + 90 / 2
print(average)
```

```text
125.0
```

Division happened first, so this is 80 + 45. Use brackets: `(80 + 90) / 2` gives `85.0`.

## Putting it together

Four friends share a pizza and drinks, add a 15% tip, and divide 14 slices between them:

```python
pizza_price = 18.50
drinks_price = 7.25
friends = 4
slices = 14

total = pizza_price + drinks_price
tip = total * 0.15
grand_total = total + tip
per_person = grand_total / friends

print(f"Food and drinks: {total}")
print(f"Tip (15%): {round(tip, 2)}")
print(f"Grand total: {round(grand_total, 2)}")
print(f"Each person pays: {round(per_person, 2)}")

# Floor division gives whole slices; % gives what's left over
print(f"Slices each: {slices // friends}")
print(f"Slices left over: {slices % friends}")
```

Output:

```text
Food and drinks: 25.75
Tip (15%): 3.86
Grand total: 29.61
Each person pays: 7.4
Slices each: 3
Slices left over: 2
```

Notice `7.4` rather than `7.40`. `round()` changes the value, not how it's displayed. You'll learn to format money with two decimal places in lesson 4.

## Exercise

Write a script called `recipe.py` that scales a pancake recipe.

- The original recipe serves 4 and uses 200 grams of flour, 2 eggs and 300 ml of milk. Store each in a variable.
- Store the number of people you're cooking for, for example 10.
- Work out the scaling factor and the new amount of each ingredient.
- Print each new amount, rounded to 1 decimal place.
- Eggs can't be split, so also print how many whole eggs you need and how much of an egg would be left over.

Hint: the scaling factor is `people / 4`. For the eggs, think about `//` and `%`.

## Recap

- `+`, `-`, `*` and `/` do arithmetic, and `/` always returns a float.
- `//` divides and drops the decimals, `%` gives the remainder and `**` raises to a power.
- Python follows the usual order of operations, so add brackets when in doubt.
- `round()` and `abs()` tidy up results, and `+=` updates a variable in place.
- Floats can carry tiny errors, so round before you show them.

## Code for this lesson

The code for this lesson is in code/03-numbers/.
