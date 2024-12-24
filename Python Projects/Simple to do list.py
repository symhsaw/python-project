import os

def load_tasks():
    """Load tasks from the in-memory list."""
    return tasks

def save_tasks(tasks):
    """Save tasks to the in-memory list."""
    return tasks

def display_tasks(tasks):
    """Display the current tasks."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    """Remove a task from the list."""
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def todo_list_app():
    """Main function for the To-Do List app."""
    print("Welcome to the Simple To-Do List App!")

    global tasks
    tasks = []

    while True:
        print("\nMenu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    todo_list_app()
