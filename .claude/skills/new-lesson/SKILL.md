---
name: new-lesson
description: Write the next daily lesson of the Python from Zero course (lesson markdown + runnable code) and commit it. Use when asked to create, write or add a lesson.
---

# Write the next lesson

Optional argument: a lesson number (e.g. `/new-lesson 05`). Without one, write the next lesson.

1. **Find the lesson.** List `lessons/`. The next number is one more than the highest `NN-` prefix, unless a number was given. If that lesson already exists, stop and ask before overwriting it.
2. **Read the rules.** Read `PROMPT.md`. It holds the curriculum, file layout, lesson format, writing rules and code rules. Follow it exactly. Use today's date for `date:`.
3. **Read earlier lessons.** Skim the previous 2–3 lessons so you build on them and don't re-teach.
4. **Write the files.** Create `lessons/NN-slug.md` and `code/NN-slug/*.py`.
5. **Verify the code.** If `python` (or `py`) is available, run every new `.py` file. Feed sample input through stdin when a script calls `input()`. Make the lesson's output blocks match what the code really prints. If Python isn't available, say the code is unverified.
6. **Check the format.** The frontmatter has `title`, `summary` and `date`. The body has no `#` heading and no HTML. The lesson filename and the code folder use the same `NN-slug`.
7. **Commit.** Use `git add lessons code` and commit with the message `Add lesson NN: <Title>`. Do not push. Tell the user the lesson is ready and that `git push` will publish it to the blog.
