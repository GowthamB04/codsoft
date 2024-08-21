def todo():
    tasks = []

    while True:
        print("\nEnter the Number in the given Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added successfully!")
        elif choice == '2':
            display(tasks)
        elif choice == '3':
            display(tasks)
            task_no = int(input("Enter the task number to delete: "))
            if 0 < task_no <= len(tasks):
                tasks.pop(task_no - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Ending")
            break
        else:
            print("invalid")
def display(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

if __name__ == "__main__":
    todo()
