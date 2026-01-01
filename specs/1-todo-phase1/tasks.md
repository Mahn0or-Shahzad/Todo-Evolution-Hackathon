# Tasks: Todo Phase I (In-Memory Python Console App)

**Feature**: Todo Phase I
**Plan**: [plan.md](plan.md)
**Spec**: [spec.md](spec.md)

## Implementation Strategy

We will build the application incrementally, starting with the core data structures and service logic (Foundational), followed by the specific user stories in order of priority (P1, P2), and finishing with polishing.

## Phase 1: Setup
- [x] T001 Initialize project directory structure and create empty `main.py`
- [x] T002 Setup basic Python project metadata (README.md, .gitignore)

## Phase 2: Foundational
- [x] T003 [P] Define `TodoTask` dataclass in `todo_model.py` with fields: id, title, description, is_completed, created_at
- [x] T004 Define `TodoStore` class in `todo_store.py` with in-memory storage and ID counter

## Phase 3: User Story 1 - Core Task Management (Priority: P1)
- [x] T005 [P] [US1] Implement `add_task` method in `todo_store.py` (validation, ID generation, storage)
- [x] T006 [P] [US1] Implement `get_all_tasks` method in `todo_store.py`
- [x] T007 [P] [US1] Implement `delete_task` method in `todo_store.py` with error handling for missing IDs
- [x] T008 [US1] Implement CLI menu loop in `main.py` for adding, viewing, and deleting tasks
- [x] T009 [US1] Verify independent test for US1: Start app, add "Test", list tasks, delete task

## Phase 4: User Story 2 - Task Updates and Completion (Priority: P2)
- [x] T010 [P] [US2] Implement `update_task` method in `todo_store.py` to allow editing title and description
- [x] T011 [P] [US2] Implement `toggle_completion` method in `todo_store.py` to switch `is_completed` status
- [x] T012 [US2] Update CLI menu in `main.py` to include update and toggle completion options
- [x] T013 [US2] Verify independent test for US2: Add task, update it, and mark as complete

## Phase 5: Polish & Cross-Cutting Concerns
- [x] T014 Add final input validation for numeric menu choices and handle `KeyboardInterrupt` gracefully in `main.py`
- [x] T015 Ensure consistent output formatting and success/error messaging across all commands

## Dependencies

1. Foundational (Phase 2) must be complete before User Stories (Phases 3 & 4).
2. US1 (Phase 3) is a prerequisite for US2 (Phase 4) menu integration.
3. Polish (Phase 5) is the final step.

## Parallel Execution Examples

- T003 and T005 can be developed in parallel as they cover the model and initial store logic in different files if split, or sequentially if in the same module.
- T010 and T011 can be developed in parallel within `todo_store.py`.
