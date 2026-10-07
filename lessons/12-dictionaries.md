---
title: Dictionaries
summary: Store values by name in dictionaries, then look up, add, update, remove and loop over them.
date: 2026-10-07
---

## Why this matters

A phone book doesn't list numbers by position. You look them up by name. Lots of data works the same way: prices by product, scores by student, settings by name. A **dictionary** stores pairs of keys and values, so you can find any value instantly by its key instead of remembering where it sits in a list.

## The concept, step by step

### Creating a dictionary

A dictionary uses curly braces. Each entry is a **key**, a colon and a **value**:

```python
prices = {"apple": 0.5, "milk": 1.2}
print(prices)
print(prices["milk"])
print(len(prices))
```

Output:

```text
{'apple': 0.5, 'milk': 1.2}
1.2
2
```

You read a value by putting its key in square brackets, a lot like an index in a list. Keys are usually strings, but numbers and tuples work too. Each key appears only once.

### Adding, changing and removing

Assigning to a key adds it if it's new, or replaces its value if it already exists:

```python
prices = {"apple": 0.5, "milk": 1.2}
prices["bread"] = 1.8
prices["milk"] = 1.1
del prices["apple"]
print(prices)
```

Output:

```text
{'milk': 1.1, 'bread': 1.8}
```

`del` removes a key and its value. Dictionaries remember the order in which keys were added.

### Safe lookups with in and get()

Asking for a key that isn't there causes an error, as you'll see below. Two tools avoid that:

```python
prices = {"apple": 0.5, "milk": 1.2}
print("apple" in prices)
print(prices.get("tea"))
print(prices.get("tea", 0))
```

Output:

```text
True
None
0
```

- `in` checks whether a **key** exists, just like it checks list items in lesson 10.
- `get(key)` returns the value, or `None` if the key is missing.
- `get(key, default)` returns your default instead of `None`.

### Looping over a dictionary

A plain `for` loop gives you the keys. `items()` gives you key-value pairs as tuples, which you can unpack just like in lesson 11:

```python
prices = {"apple": 0.5, "milk": 1.2}
for item in prices:
    print(item)
for item, price in prices.items():
    print(f"{item} costs {price:.2f}")
```

Output:

```text
apple
milk
apple costs 0.50
milk costs 1.20
```

`values()` gives you just the values, so `sum(prices.values())` adds up every price.

## Common mistakes

### Looking up a missing key

```python
ages = {"Leo": 12}
print(ages["leo"])
```

```text
KeyError: 'leo'
```

Keys are exact, so `"leo"` and `"Leo"` are different keys, just like variable names in lesson 2. Clean up the key first, for example with `.title()`, or use `get()` so a missing key gives `None` instead of an error.

### Using a list as a key

```python
locations = {["Lisbon", "Portugal"]: 3}
```

```text
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
```

Keys must be values that can't change. A list can change, so Python refuses it. Use a tuple instead: `{("Lisbon", "Portugal"): 3}`.

### Expecting a list of pairs from a plain loop

```python
prices = {"apple": 0.5}
for item, price in prices:
    print(item, price)
```

```text
ValueError: too many values to unpack (expected 2)
```

A plain loop gives you only the keys. Here the key `"apple"` is a 5-letter string, and Python tries to unpack its letters into two variables. Loop over `prices.items()` to get both key and value.

## Putting it together

A grade book that stores each student's score by name:

```python
grades = {"Maya": 88, "Leo": 72, "Sam": 95}

grades["Ana"] = 64
grades["Leo"] = 78
del grades["Sam"]

print(f"Students: {len(grades)}")
for name, score in grades.items():
    if score >= 80:
        result = "great"
    elif score >= 65:
        result = "pass"
    else:
        result = "needs help"
    print(f"{name}: {score} ({result})")

average = sum(grades.values()) / len(grades)
print(f"Class average: {average:.1f}")

lookup = input("Look up a student: ").strip().title()
print(f"{lookup}: {grades.get(lookup, 'not found')}")
```

Output (after typing leo):

```text
Students: 3
Maya: 88 (great)
Leo: 78 (pass)
Ana: 64 (needs help)
Class average: 76.7
Look up a student: leo
Leo: 78
```

Type a name that isn't there, like `zoe`, and the last line becomes `Zoe: not found` instead of crashing. Compare this with the two matching lists in lesson 10: here each name and score live together, so they can't get out of step.

## Exercise

Write a script called `word_count.py` that counts letters.

- Ask the user for a sentence.
- Build a dictionary where each key is a letter and each value is how many times it appears. Skip spaces.
- Count capitals and lowercase as the same letter.
- Print each letter and its count.
- Finally, print the letter that appears most often.

Hint: start with an empty dictionary, `counts = {}`. For each letter, `counts[letter] = counts.get(letter, 0) + 1` adds one, whether or not the letter was there already.

## Recap

- A dictionary stores key-value pairs: `{"apple": 0.5}`.
- `d[key]` reads a value, and `d[key] = value` adds or updates one.
- `del d[key]` removes an entry, and `in` checks whether a key exists.
- `get(key, default)` looks up a key without risking a `KeyError`.
- Loop with `items()` to get each key and value together.

## Code for this lesson

The code for this lesson is in code/12-dictionaries/.
