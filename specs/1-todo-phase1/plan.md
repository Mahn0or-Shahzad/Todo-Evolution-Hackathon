# Implementation Plan: Todo Phase I (In-Memory Python Console App)

**Feature Branch**: `1-todo-phase1`
**Created**: 2026-01-01
**Status**: Draft
**Spec Reference**: [spec.md](spec.md)

## Technical Context

- **Language**: Python 3.10+
- **Input/Output**: Standard Streams (sys.stdin, sys.stdout)
- **State Management**: In-memory dictionary or list of objects
- **Dependencies**: Standard library only (dataclasses, datetime, typing)

## Constitution Check

- **SDD Compliance**: All code will be generated from tasks derived from this plan.
- **No Manual Logic**: Architecture defined here avoids "magic" or hidden behaviors.
- **Phase-Wise Evolution**: Design ensures easy migration to FastAPI (Phase II) and persistence.

## Architecture & Design

### 1. Data Layer (In-Memory)
- Use a `TodoTask` dataclass for type safety and clean data modeling.
- `TodoStore` class will manage the collection, providing CRUD methods.
- Auto-incrementing ID will be handled by a counter within the `TodoStore`.

### 2. Service Layer
- Logic for searching tasks, validating non-empty titles, and formatting strings for display.
- Separates CLI concerns from data manipulation.

### 3. CLI Interface
- A simple command loop:
  - Display Menu
  - Prompt for input
  - Execute corresponding service method
  - Display result/success message
- Command mapping:
  - 1: Add Task
  - 2: View All Tasks
  - 3: Update Task
  - 4: Delete Task
  - 5: Toggle Completion
  - 0: Exit

## Forward Compatibility (Strategy)

- **Priorities & Due Dates**: The `TodoTask` dataclass is designed to accept new optional fields in Phase II without breaking the dictionary-based lookup logic.
- **Persistence**: The `TodoStore` acts as a repository pattern. In Phase II, the internal list can be replaced with a database session/engine without changing the method signatures used by the CLI or API.
- **API Extension**: Service methods return objects or lists of objects, making it trivial to wrap them in FastAPI endpoints later.

## Risk Analysis

- **Risk**: Loss of data on crash (expected as per Phase I constraints).
- **Mitigation**: Clear user messaging that the session is in-memory only.
- **Risk**: ID collisions if not handled atomically.
- **Mitigation**: Store class manages the ID counter centrally.

## Evaluation & Validation

- **Definition of Done**:
  - Menu runs and accepts all 6 commands.
  - Tasks can be created and retrieved immediately.
  - No external packages in `requirements.txt`.
  - Errors handled for invalid numeric inputs or missing IDs.
