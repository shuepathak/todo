import datetime

class Task:
    def __init__(self, title, description, due_date=None, priority="medium"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def mark_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.completed = True
                break

    def list_tasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"Title: {task.title}, Status: {status}, Priority: {task.priority}")
            print(f"Description: {task.description}")
            if task.due_date:
                print(f"Due Date: {task.due_date}")
            print("-" * 30)

def main():
    manager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
            due_date = None
            if due_date_str:
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
            priority = input("Enter priority (low/medium/high): ")
            task = Task(title, description, due_date, priority)
            manager.add_task(task)

        elif choice == "2":
            title = input("Enter task title to remove: ")
            manager.remove_task(title)

        elif choice == "3":
            title = input("Enter task title to mark as completed: ")
            manager.mark_completed(title)

        elif choice == "4":
            manager.list_tasks()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
