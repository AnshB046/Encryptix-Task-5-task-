tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "status": "Pending"})
    print(f"Task '{task}' added.")

def update_task():
    if len(tasks) == 0:
        print("No tasks available to update.")
        return

    list_tasks()
    task_number = int(input("Enter the number of the task to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_number]["task"] = new_task
        print(f"Task #{task_number + 1} updated to '{new_task}'.")
    else:
        print("Task number out of range.")

def list_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['task']} - {task['status']}")

def complete_task():
    if len(tasks) == 0:
        print("No tasks available to complete.")
        return

    list_tasks()
    task_number = int(input("Enter the number of the task to mark as complete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["status"] = "Completed"
        print(f"Task #{task_number + 1} marked as completed.")
    else:
        print("Task number out of range.")

def remove_task():
    if len(tasks) == 0:
        print("No tasks available to remove.")
        return

    list_tasks()
    task_number = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Task number out of range.")

def main():
    print("Welcome to the To-Do List Manager!")
    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. Update a task")
        print("3. List tasks")
        print("4. Mark a task as completed")
        print("5. Remove a task")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            remove_task()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
