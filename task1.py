class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        del self.tasks[task_index]

    def update_task(self, task_index, new_task):
        self.tasks[task_index] = new_task

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")

def main():
    todo_list = TodoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
            if todo_list.tasks:
                task_index = int(input("Enter task number to remove: ")) - 1
                if 0 <= task_index < len(todo_list.tasks):
                    todo_list.remove_task(task_index)
                else:
                    print("Invalid task number.")
        elif choice == '3':
            todo_list.display_tasks()
            if todo_list.tasks:
                task_index = int(input("Enter task number to update: ")) - 1
                if 0 <= task_index < len(todo_list.tasks):
                    new_task = input("Enter new task: ")
                    todo_list.update_task(task_index, new_task)
                else:
                    print("Invalid task number.")
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
