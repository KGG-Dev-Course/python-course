---
title: Tuples
summary: Group related values into tuples, unpack them into variables, and know when to pick a tuple over a list.
date: 2026-10-07
---

## Why this matters

Some values belong together and shouldn't change: a city's name and its coordinates, the width and height of a screen, a date. A **tuple** bundles a few related values into one, and Python protects it from being changed by accident. Tuples also give you a neat trick called unpacking, which you'll use all the time.

## The concept, step by step

### Creating a tuple

A tuple looks like a list, but uses round brackets instead of square ones:

```python
place = ("Lisbon", 38.72)
print(place)
print(place[0], len(place))
```

Output:

```text
('Lisbon', 38.72)
Lisbon 2
```

Indexing, slicing, `len()`, `in` and `for` loops all work just as they do for lists in lesson 10. The values inside can be different types: here, a string and a float.

### Tuples can't be changed

Once a tuple is created, you can't add, remove or replace its items. That's called being **immutable**, the same as strings. It sounds like a limitation, but it's useful: if a value shouldn't change, a tuple makes sure it doesn't.

A good rule of thumb:

- Use a **list** for a collection of similar things that may grow or shrink, like a shopping list.
- Use a **tuple** for a fixed group of related values that describe one thing, like a point on a map.

### Unpacking

You can pull a tuple's values out into separate variables in one line:

```python
place = ("Lisbon", 38.72)
city, latitude = place
print(city)
print(latitude)
```

Output:

```text
Lisbon
38.72
```

The first variable gets the first value, the second gets the second, and so on. This reads much better than `place[0]` and `place[1]`.

Unpacking gives you a classic trick for swapping two variables:

```python
first = "Maya"
second = "Leo"
first, second = second, first
print(first, second)
```

Output:

```text
Leo Maya
```

`second, first` on the right builds a tuple, and the left side unpacks it. You don't need the brackets when it's clear from context.

### A list of tuples

Lists and tuples work well together. A list holds many records, and each record is a tuple. You can unpack each one right in the `for` loop:

```python
scores = [("Maya", 88), ("Leo", 72)]
for name, score in scores:
    print(f"{name} scored {score}")
```

Output:

```text
Maya scored 88
Leo scored 72
```

On each pass, the next tuple is unpacked into `name` and `score`.

## Common mistakes

### Trying to change a tuple

```python
point = (1, 2)
point[0] = 5
```

```text
TypeError: 'tuple' object does not support item assignment
```

Tuples can't be changed. Make a new one instead: `point = (5, point[1])`. If you find yourself changing the values a lot, you probably want a list.

### A one-item tuple without a comma

```python
single = ("solo")
print(type(single))
```

```text
<class 'str'>
```

Round brackets alone are just grouping, like in maths. It's the **comma** that makes a tuple. Write `("solo",)` to get a one-item tuple.

### Unpacking the wrong number of values

```python
name, score = ("Maya", 88, "A")
```

```text
ValueError: too many values to unpack (expected 2, got 3)
```

You need exactly one variable per value. Use `name, score, grade = ...` instead.

## Putting it together

A trip planner that stores each city as a tuple of name, latitude and longitude, and estimates how far each one is from home:

```python
home = ("Lisbon", 38.72, -9.14)
trips = [
    ("Porto", 41.15, -8.61),
    ("Madrid", 40.42, -3.70),
    ("Faro", 37.02, -7.93),
]

home_name, home_lat, home_lon = home
print(f"Starting from {home_name} at {home_lat}, {home_lon}")

for name, lat, lon in trips:
    # A rough distance: 111 km per degree, good enough for a quick estimate
    lat_km = (lat - home_lat) * 111
    lon_km = (lon - home_lon) * 87
    distance = (lat_km ** 2 + lon_km ** 2) ** 0.5
    print(f"{name}: about {distance:.0f} km")

first_trip = trips[0]
print(f"First trip on the list: {first_trip[0]}")
print(f"Number of trips planned: {len(trips)}")
```

Output:

```text
Starting from Lisbon at 38.72, -9.14
Porto: about 274 km
Madrid: about 510 km
Faro: about 216 km
First trip on the list: Porto
Number of trips planned: 3
```

Raising to the power `0.5` (from lesson 3) takes a square root. These are straight-line estimates, not road distances. Each city's data can't be changed by accident, but the list of trips can still grow with `append()`.

## Exercise

Write a script called `rectangles.py`.

- Create a list of at least 4 rectangles, each a tuple of `(name, width, height)`, for example `("door", 0.9, 2.1)`.
- Loop over the list, unpacking each tuple, and print the name, area and perimeter of each to 2 decimal places.
- Keep track of which rectangle has the biggest area and print its name at the end.
- Add one more rectangle with `append()` before the loop, and check it appears in the output.

Hint: start with `biggest_name = ""` and `biggest_area = 0` before the loop, and update both inside an `if`.

## Recap

- A tuple is an ordered group of values in round brackets, and it can't be changed.
- Use tuples for fixed records and lists for collections that change.
- Unpacking assigns each value to its own variable: `city, lat = place`.
- `a, b = b, a` swaps two variables.
- A one-item tuple needs a trailing comma: `("solo",)`.

## Code for this lesson

The code for this lesson is in code/11-tuples/.
