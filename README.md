# Python from Zero

A daily, hands-on Python course. A new lesson is added every day.

## Structure

```
course.json        Course title, description and planned lesson count
lessons/           One markdown file per lesson (01-intro.md, 02-...)
code/              Runnable code for each lesson
```

## Adding a lesson

1. Create `lessons/NN-topic.md` with frontmatter:

   ```markdown
   ---
   title: Lesson title
   summary: One-line summary
   date: YYYY-MM-DD
   ---
   ```

2. Put example code in `code/NN-topic/`.
3. Commit and push.

The number at the start of the filename sets the lesson order.
