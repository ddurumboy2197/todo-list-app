class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name, task_description):
        if task_name not in self.tasks:
            self.tasks[task_name] = task_description
            print(f"Task '{task_name}' added successfully.")
        else:
            print(f"Task '{task_name}' already exists.")

    def delete_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' deleted successfully.")
        else:
            print(f"Task '{task_name}' not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task_name, task_description in self.tasks.items():
                print(f"Task: {task_name}")
                print(f"Description: {task_description}")
                print("------------------------")

def main():
    todo_list = ToDoList()

    while True:
        print("1. Add task")
        print("2. Delete task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            todo_list.add_task(task_name, task_description)
        elif choice == "2":
            task_name = input("Enter task name to delete: ")
            todo_list.delete_task(task_name)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
