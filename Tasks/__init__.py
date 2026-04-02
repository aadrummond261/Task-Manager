# This list stores all tasks entered by the user.
tasks = []

# This function displays all tasks in the list.
# If there are no tasks, it tells the user the list is empty.
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

# This loop keeps the program running until the user chooses to exit.
while True:
    # Display the main menu.
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    # Ask the user to choose an option from the menu.
    choice = input("Choose an option: ")

    # If the user chooses 1, add a new task.
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    # If the user chooses 2, show all tasks.
    elif choice == "2":
        view_tasks()

    # If the user chooses 3, mark a task as completed.
    elif choice == "3":
        view_tasks()
        try:
            num = int(input("Enter task number: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1] += " (Completed)"
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    # If the user chooses 4, delete a task from the list.
    elif choice == "4":
        view_tasks()
        try:
            num = int(input("Enter task number: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    # If the user chooses 5, end the program.
    elif choice == "5":
        print("Goodbye!")
        break

    # If the user enters anything else, show an error message.
    else:
        print("Invalid choice. Try again.")