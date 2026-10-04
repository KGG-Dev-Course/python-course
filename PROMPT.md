# Lesson Rules

The curriculum and writing rules for this course. In Claude Code, run `/new-lesson` and it follows this file. With another AI, copy everything below the line and fill in **Today**.

---

You are writing one lesson of "Python from Zero", a free 30-lesson course for complete beginners. The lessons are published on a blog, one per day. Write today's lesson and its code.

## Today

- Lesson number: **NN** (for example 02)
- Date: **YYYY-MM-DD**

Write the lesson whose number matches the curriculum below. If earlier lessons are in `lessons/`, read them first. Build on what they taught and don't re-teach it.

## Curriculum

1. Getting Started with Python (already written)
2. Variables and Data Types
3. Numbers and Math
4. Working with Strings
5. Getting User Input and Type Conversion
6. Booleans and Comparisons
7. If, Elif, Else
8. While Loops
9. For Loops and range()
10. Lists
11. Tuples
12. Dictionaries
13. Sets
14. Loop Patterns: enumerate, zip, break, continue
15. Functions
16. Function Arguments: defaults, keyword args, *args, **kwargs
17. Scope and Return Values
18. List and Dictionary Comprehensions
19. Errors and Exceptions
20. Reading and Writing Files
21. Modules and Imports
22. The Standard Library Tour: datetime, random, math, pathlib
23. Virtual Environments and pip
24. Classes and Objects
25. Inheritance
26. Dunder Methods and Dataclasses
27. Working with JSON
28. Calling a Web API with requests
29. Testing with pytest
30. Final Project: A Command-Line To-Do App

## Files to create

1. `lessons/NN-short-slug.md`, for example `lessons/02-variables.md`.
   - The filename must start with the two-digit lesson number. The site uses that number to order the lessons.
   - The slug may contain only lowercase letters, digits and hyphens.
2. `code/NN-short-slug/`, holding one or more runnable `.py` files used in the lesson. The folder name must match the lesson filename.

Do not change `course.json`, `README.md` or any other lesson.

## Lesson format

The file must begin with this frontmatter, exactly:

```markdown
---
title: <Lesson title from the curriculum>
summary: <One sentence, under 120 characters, saying what the reader can do after this lesson>
date: <YYYY-MM-DD>
---
```

Then write the body in this order, using `##` headings. Never use `#`, because the site renders the title itself.

1. **Why this matters**: 2–3 sentences tying the topic to something real the reader would want to build.
2. **The concept, step by step**: 3–5 short subsections. Each one gets a small code example and a plain-English explanation of what it does.
3. **Common mistakes**: 2–4 mistakes beginners actually make. For each, show the wrong code, the error or bad output it produces, and the fix.
4. **Putting it together**: one complete, slightly larger example that uses everything from the lesson. It must be the same code as a file in `code/NN-slug/`.
5. **Exercise**: one task the reader can finish in 10–15 minutes, with clear requirements. Add a hint. Do not include the solution.
6. **Recap**: 3–5 bullet points.
7. **Code for this lesson**: one closing line, `The code for this lesson is in code/NN-slug/.`

## Writing rules

- Assume the reader knows only what earlier lessons covered. If you must use something not yet taught, say so in one line: "We'll cover X in lesson N."
- Use short paragraphs and a friendly, direct tone. Address the reader as "you".
- Aim for 800–1,500 words. A lesson should take about 10 minutes to read.
- Mark every code block with a language: `python`, `bash` or `text`. Show program output in a separate `text` block, labelled "Output:".
- Use small, concrete examples such as a shopping list, a grade calculator or a weather report. Avoid `foo`, `bar` and abstract math.
- Use plain Markdown only: headings, paragraphs, lists, code blocks, links, bold and italics. No HTML, tables, images, emojis or admonitions.

## Code rules

- Target Python 3.12+. Use only the standard library, except for the lessons that teach `requests` or `pytest`.
- Every file must run as-is with `python filename.py` and produce the output shown in the lesson.
- Follow PEP 8. Use descriptive names, and add a short comment only where the code isn't obvious.
- Lessons 1–14 use plain top-level scripts. From lesson 15 on, put the main logic in functions and use an `if __name__ == "__main__":` guard.

## Before you finish

Check each item:
- The frontmatter is valid and the date matches today's.
- The filename and code folder use the same `NN-slug`.
- Every code example is correct, and every output block matches what the code really prints.
- No concept from a later lesson is used without a note.

Then suggest a one-line commit message, in the form `Add lesson NN: <Title>`.
