---
title: Sets
summary: Use sets to remove duplicates, check membership fast and compare groups with union, intersection and difference.
date: 2026-11-17
---

## Why this matters

Imagine a sign-up form where people register twice, or two guest lists you need to compare. You don't care about order or position. You only care about *who is in the group*. A **set** is a collection that keeps each value only once, which makes removing duplicates and comparing groups a one-line job.

## The concept, step by step

### Creating a set

A set uses curly braces like a dictionary, but holds single values instead of key-value pairs:

```python
fruits = {"apple", "banana", "apple", "cherry"}
print(len(fruits))
print(sorted(fruits))
```

Output:

```text
3
['apple', 'banana', 'cherry']
```

The second `"apple"` was dropped, because a set never holds the same value twice. Sets also have **no order**. If you print a set of strings directly, the order can change from one run to the next. That's why the examples in this lesson use `sorted()` from lesson 10, which gives you a sorted list you can rely on.

### Removing duplicates from a list

`set()` turns a list into a set, which is the quickest way to remove duplicates:

```python
numbers = [3, 1, 3, 2, 1]
unique = set(numbers)
print(unique)
print(len(numbers), len(unique))
```

Output:

```text
{1, 2, 3}
5 3
```

If you need a list again afterwards, wrap it: `sorted(unique)` or `list(unique)`.

### Adding and removing values

Start an empty set with `set()`, then grow it with `add()`:

```python
tags = set()
tags.add("python")
tags.add("beginner")
tags.add("python")
print(sorted(tags))

tags.discard("java")
tags.remove("beginner")
print(tags)
```

Output:

```text
['beginner', 'python']
{'python'}
```

Adding a value that's already there does nothing, with no error. There are two ways to take a value out:

- `remove(value)` deletes it, and raises an error if it isn't there.
- `discard(value)` deletes it if it's there, and quietly does nothing if it isn't.

### Checking membership with in

`in` works on sets just like on lists and dictionaries:

```python
seen = {"Maya", "Leo"}
print("Leo" in seen)
print("Zoe" in seen)
```

Output:

```text
True
False
```

For a short list you won't notice a difference, but for thousands of items, `in` on a set is much faster than `in` on a list. A list checks items one by one. A set jumps straight to the answer, a lot like a dictionary key lookup.

### Comparing groups

This is where sets really shine. Say you know who came to a meetup on Monday and on Tuesday:

```python
monday = {"Maya", "Leo", "Sam"}
tuesday = {"Leo", "Ana", "Sam"}

print(sorted(monday | tuesday))
print(sorted(monday & tuesday))
print(sorted(monday - tuesday))
print(sorted(tuesday - monday))
```

Output:

```text
['Ana', 'Leo', 'Maya', 'Sam']
['Leo', 'Sam']
['Maya']
['Ana']
```

- `|` is the **union**: everyone in either set.
- `&` is the **intersection**: only people in both sets.
- `-` is the **difference**: people in the first set but not the second.

Order matters for `-`. `monday - tuesday` and `tuesday - monday` give different answers.

## Common mistakes

### Using {} for an empty set

```python
names = {}
names.add("Maya")
```

```text
AttributeError: 'dict' object has no attribute 'add'
```

Empty curly braces make an empty **dictionary**, not a set. Python decided this before sets existed, so it never changed. Write `names = set()` for an empty set. `{"Maya"}` with a value inside is a set as usual.

### Trying to index a set

```python
colors = {"red", "green", "blue"}
print(colors[0])
```

```text
TypeError: 'set' object is not subscriptable
```

A set has no positions, so there is no "first" item. If you need positions, turn it into a list first: `sorted(colors)[0]`.

### Removing a value that isn't there

```python
tags = {"python"}
tags.remove("java")
```

```text
KeyError: 'java'
```

`remove()` expects the value to exist. Check with `in` first, or use `discard()` when it's fine for the value to be missing.

## Putting it together

A small script that cleans up sign-ups for two workshops, then compares them:

```python
python_signups = ["maya", "Leo", "sam", "Maya", "ana", "leo"]
web_signups = ["Sam", "ana", "Zoe", "ana", "Kai"]

# Clean up names and remove duplicates in one go
python_group = set()
for name in python_signups:
    python_group.add(name.strip().title())

web_group = set()
for name in web_signups:
    web_group.add(name.strip().title())

print(f"Python workshop ({len(python_group)}): {sorted(python_group)}")
print(f"Web workshop ({len(web_group)}): {sorted(web_group)}")

both = python_group & web_group
everyone = python_group | web_group
python_only = python_group - web_group

print(f"Signed up for both: {sorted(both)}")
print(f"Total people: {len(everyone)}")
print(f"Python only: {sorted(python_only)}")

cancel = input("Who wants to cancel? ").strip().title()
python_group.discard(cancel)
web_group.discard(cancel)
print(f"Python workshop now: {sorted(python_group)}")
print(f"Web workshop now: {sorted(web_group)}")
```

Output (after typing leo):

```text
Python workshop (4): ['Ana', 'Leo', 'Maya', 'Sam']
Web workshop (4): ['Ana', 'Kai', 'Sam', 'Zoe']
Signed up for both: ['Ana', 'Sam']
Total people: 6
Python only: ['Leo', 'Maya']
Who wants to cancel? leo
Python workshop now: ['Ana', 'Maya', 'Sam']
Web workshop now: ['Ana', 'Kai', 'Sam', 'Zoe']
```

Notice that `"maya"` and `"Maya"` only count once, because `.title()` makes them identical before they go into the set. And `discard()` lets the cancel step work even though Leo was only in one of the workshops.

## Exercise

Write a script called `common_words.py` that compares two sentences.

- Ask the user for two sentences.
- Turn each sentence into a set of lowercase words.
- Print the words that appear in both sentences, sorted.
- Print the words that appear only in the first sentence, sorted.
- Print how many different words were used in total.

Hint: `sentence.lower().split()` gives you a list of lowercase words. `split()` is new: it breaks a string into a list wherever there are spaces. Then `set()` turns that list into a set.

## Recap

- A set holds each value only once and has no order: `{"apple", "banana"}`.
- `set(my_list)` removes duplicates, and `set()` creates an empty set. `{}` is an empty dictionary.
- `add()` adds a value, `remove()` deletes one or raises an error, `discard()` deletes one safely.
- `in` on a set is fast, even for large collections.
- `|`, `&` and `-` give the union, intersection and difference of two sets.

## Code for this lesson

The code for this lesson is in code/13-sets/.
