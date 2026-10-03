---
title: Getting Started with Python
summary: Install Python, run your first script, and learn how the course works.
date: 2026-10-03
---

## Why Python?

Python is readable, has a huge ecosystem, and is used for web backends, automation, data and AI. It's a great first language and a great second one.

## Install Python

1. Download Python 3.12+ from [python.org](https://www.python.org/downloads/).
2. On Windows, tick **"Add python.exe to PATH"** in the installer.
3. Check it works:

```bash
python --version
```

## Your first script

Create a file called `hello.py`:

```python
name = input("What's your name? ")
print(f"Hello, {name}! Welcome to the course.")
```

Run it:

```bash
python hello.py
```

## What just happened

- `input()` reads text the user types.
- `name = ...` stores it in a **variable**.
- `f"..."` is an **f-string**: anything in `{}` is replaced by its value.
- `print()` writes to the screen.

## Exercise

Change the script to also ask for the user's favourite language and print both answers in one sentence.

The code for this lesson is in `code/01-intro/`.
