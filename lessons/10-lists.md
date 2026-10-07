---
title: Lists
summary: Store many values in one list, then add, remove, sort, search and loop over them.
date: 2026-10-07
---

## Why this matters

A shopping list, the scores in a game, the songs in a playlist: real data usually comes in groups. Making a separate variable for every item would be impossible to manage. A **list** holds any number of values in one variable, in order, and lets you change them whenever you like.

## The concept, step by step

### Creating a list and reading items

Put values inside square brackets, separated by commas:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0], fruits[-1])
print(fruits[1:])
print(len(fruits))
```

Output:

```text
['apple', 'banana', 'cherry']
apple cherry
['banana', 'cherry']
3
```

Lists use the same indexes and slices you learned for strings in lesson 4. The first item is at index 0, `-1` is the last item, and `len()` counts the items.

### Changing a list

Unlike a string, a list can be changed in place. Assign to an index to replace an item:

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)
```

Output:

```text
['apple', 'blueberry', 'cherry']
```

List methods add and remove items:

```python
shopping = ["milk", "eggs"]
shopping.append("bread")
shopping.insert(0, "coffee")
shopping.remove("eggs")
last = shopping.pop()
print(shopping)
print(f"Removed: {last}")
```

Output:

```text
['coffee', 'milk']
Removed: bread
```

- `append(item)` adds to the end.
- `insert(index, item)` adds at a position and shifts the rest along.
- `remove(item)` deletes the first matching item.
- `pop()` removes the last item and gives it back. `pop(index)` removes the item at that index.

### Looping over a list

The `for` loop from lesson 9 works on lists just as it does on strings:

```python
scores = [70, 95, 82]
for score in scores:
    print(f"Score: {score}")
```

Output:

```text
Score: 70
Score: 95
Score: 82
```

If you also need the position, loop over `range(len(scores))` and use `scores[i]`. Lesson 14 shows a neater way.

### Checking with in, and adding up

The `in` keyword asks "is this item in the list?" and gives a boolean:

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits, "kiwi" not in fruits)
```

Output:

```text
True True
```

`in` works on strings as well, so `letter in "aeiou"` would replace that long vowel check from lesson 9.

For lists of numbers, `sum()`, `min()` and `max()` do the work for you:

```python
scores = [70, 95, 82]
print(sum(scores), min(scores), max(scores))
```

Output:

```text
247 70 95
```

### Sorting

`sort()` puts a list in order, changing the list itself. `sorted()` gives you a new sorted list and leaves the original alone:

```python
scores = [70, 95, 82]
print(sorted(scores))
print(scores)
scores.sort()
print(scores)
```

Output:

```text
[70, 82, 95]
[70, 95, 82]
[70, 82, 95]
```

## Common mistakes

### Indexing past the end

```python
fruits = ["apple"]
print(fruits[3])
```

```text
IndexError: list index out of range
```

A list with one item only has index 0. Check `len()` before reaching for an index you're not sure exists.

### Removing something that isn't there

```python
fruits = ["apple"]
fruits.remove("kiwi")
```

```text
ValueError: list.remove(x): x not in list
```

Check first with `in`: `if "kiwi" in fruits:` and then remove it.

### Storing the result of sort()

```python
numbers = [3, 1, 2]
result = numbers.sort()
print(result)
```

```text
None
```

`sort()` changes the list and returns nothing, which Python shows as `None`. Either call `numbers.sort()` on its own line and then use `numbers`, or write `result = sorted(numbers)`.

### Thinking = makes a copy

```python
original = ["x"]
copy = original
copy.append("y")
print(original)
```

```text
['x', 'y']
```

`copy = original` doesn't copy anything. Both names point to the same list. To get a real copy, use `copy = original.copy()`.

## Putting it together

A shopping list with a matching list of prices:

```python
shopping = ["milk", "eggs", "bread"]
prices = [1.20, 2.50, 1.80]

shopping.append("apples")
prices.append(3.10)
shopping.insert(0, "coffee")
prices.insert(0, 4.75)

shopping.remove("bread")
prices.pop(3)

print(f"You need {len(shopping)} items:")
for i in range(len(shopping)):
    print(f"{i + 1}. {shopping[i]} - {prices[i]:.2f}")

print(f"Total: {sum(prices):.2f}")
print(f"Cheapest item costs {min(prices):.2f}, dearest {max(prices):.2f}")

if "milk" in shopping:
    print("Don't forget the milk!")

shopping.sort()
print(f"Sorted for the shop: {shopping}")
```

Output:

```text
You need 4 items:
1. coffee - 4.75
2. milk - 1.20
3. eggs - 2.50
4. apples - 3.10
Total: 11.55
Cheapest item costs 1.20, dearest 4.75
Don't forget the milk!
Sorted for the shop: ['apples', 'coffee', 'eggs', 'milk']
```

After the insert, bread sits at index 3, so `prices.pop(3)` removes its price. Keeping two lists in step like this is easy to get wrong. Lesson 12 shows a better way to pair names with prices.

## Exercise

Write a script called `playlist.py`.

- Start with a list of 3 song titles.
- Use a `while` loop to keep asking the user for a song to add, until they type `done`.
- Don't add a song if it's already in the list. Print a message instead.
- At the end, print how many songs there are, then print the songs in alphabetical order, numbered from 1.

Hint: `in` checks whether a song is already there. To number the songs, loop over `range(len(...))` on a sorted copy.

## Recap

- A list holds many values in order: `items = ["a", "b"]`.
- Indexes and slices work just as they do for strings, but lists can be changed in place.
- `append`, `insert`, `remove` and `pop` add and remove items.
- `in` checks membership, and `sum`, `min` and `max` work on lists of numbers.
- `sort()` changes the list and returns `None`, while `sorted()` returns a new list.

## Code for this lesson

The code for this lesson is in code/10-lists/.
