---
id: 3
title: Add Description to Task List View
stage: green
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-phase1
branch: 1-todo-phase1
user: local
command: general
labels: [ui-update, enhancements, phase1]
links:
  spec: specs/1-todo-phase1/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - src/main.py
tests:
  - null
---

## Prompt

Update the "View Tasks" feature in my Python todo app.
Currently, it only prints ID, title, and status, but each task also has a description.
Requirements: Add Description column, show description or "-" if empty, keep table aligned.

## Response snapshot

I updated the `view_tasks` logic in `src/main.py` to include a "Description" column. The table header was extended, and each row now displays the task's description, defaulting to "-" if none exists. Formatting was adjusted to maintain alignment.

## Outcome

- ✅ Impact: Users can now see task descriptions directly in the list view without updating individual tasks.
- 🧪 Tests: No automated tests; alignment verified via code logic.
- 📁 Files: Updated `src/main.py`.
- 🔁 Next prompts: null
- 🧠 Reflection: Small UI improvements like this significantly enhance the usability of the CLI interface.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
