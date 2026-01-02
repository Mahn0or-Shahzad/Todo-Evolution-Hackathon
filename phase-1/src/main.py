import sys
from todo_store import TodoStore

def main():
    store = TodoStore()

    while True:
        try:
            print("\n--- Todo App Phase I ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Toggle Completion")
            print("0. Exit")

            choice = input("\nSelect an option: ")

            if choice == "1":
                title = input("Enter task title: ")
                desc = input("Enter description (optional): ")
                try:
                    task = store.add_task(title, desc if desc else None)
                    print(f"\nTask '{task.title}' added with ID {task.id}")
                except ValueError as e:
                    print(f"\nError: {e}")

            elif choice == "2":
                tasks = store.get_all()
                if not tasks:
                    print("\nYour todo list is currently empty.")
                else:
                    print("\nID  | Title            | Status  | Description")
                    print("-" * 65)
                    for t in tasks:
                        status = "Done" if t.is_completed else "Pending"
                        desc = t.description if t.description else "-"
                        print(f"{t.id:<3} | {t.title:<16} | {status:<7} | {desc}")

            elif choice == "3":
                try:
                    task_id_input = input("Enter task ID to update: ")
                    if not task_id_input: raise ValueError("ID is required.")
                    task_id = int(task_id_input)

                    title = input("Enter new title (leave blank to keep current): ")
                    desc = input("Enter new description (leave blank to keep current): ")

                    if store.update_task(
                        task_id,
                        title if title.strip() else None,
                        desc if desc.strip() else None
                    ):
                        print(f"\nTask {task_id} updated.")
                    else:
                        print(f"\nError: Task with ID {task_id} not found.")
                except ValueError as e:
                    print(f"\nError: {e}")

            elif choice == "4":
                try:
                    task_id_input = input("Enter task ID to delete: ")
                    if not task_id_input: raise ValueError("ID is required.")
                    task_id = int(task_id_input)

                    if store.delete_task(task_id):
                        print(f"\nTask {task_id} deleted.")
                    else:
                        print(f"\nError: Task with ID {task_id} not found.")
                except ValueError as e:
                    print(f"\nError: {e}")

            elif choice == "5":
                try:
                    task_id_input = input("Enter task ID to toggle: ")
                    if not task_id_input: raise ValueError("ID is required.")
                    task_id = int(task_id_input)

                    if store.toggle_completion(task_id):
                        print(f"\nTask {task_id} status toggled.")
                    else:
                        print(f"\nError: Task with ID {task_id} not found.")
                except ValueError as e:
                    print(f"\nError: {e}")

            elif choice == "0":
                print("\nGoodbye!")
                sys.exit(0)
            else:
                print("\nInvalid choice. Please try again.")
        except KeyboardInterrupt:
            print("\n\nExiting application...")
            sys.exit(0)

if __name__ == "__main__":
    main()
