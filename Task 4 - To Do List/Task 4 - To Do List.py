class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "X" if self.completed else " "
        return f"[{status}] {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        if description.strip():
            self.tasks.append(Task(description))
            print(f"[SUCCESS] Task added successfully: '{description}'")
        else:
            print("[ERROR] Task description cannot be empty.")

    def view_tasks(self):
        if not self.tasks:
            print("\n----------------------------------------")
            print("[INFO] Your to-do list is currently empty.")
            print("----------------------------------------")
            return False
        
        print("\n========================================")
        print("              YOUR TASKS              ")
        print("========================================")
        for index, task in enumerate(self.tasks, 1):
            print(f" {index:02d}. {task}")
        print("========================================")
        return True

    def update_task_status(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"[SUCCESS] Task marked as complete: '{self.tasks[index].description}'")
            return True
        else:
            print("[ERROR] Invalid task number provided.")
            return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"[SUCCESS] Task removed successfully: '{removed.description}'")
            return True
        else:
            print("[ERROR] Invalid task number provided.")
            return False


def main():
    todo = ToDoList()
    
    while True:
        print("\n+--------------------------------------+")
        print("|           TO-DO LIST MENU            |")
        print("+--------------------------------------+")
        print("| 1. View Tasks                        |")
        print("| 2. Add Task                          |")
        print("| 3. Mark Task as Complete             |")
        print("| 4. Delete Task                       |")
        print("| 5. Exit                              |")
        print("+--------------------------------------+")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            todo.view_tasks()
            
        elif choice == "2":
            desc = input("Enter task description: ")
            todo.add_task(desc)
            
        elif choice == "3":
            if todo.view_tasks():
                try:
                    idx = int(input("Enter task number to complete: ")) - 1
                    todo.update_task_status(idx)
                except ValueError:
                    print("[ERROR] Please enter a valid numerical value.")
                    
        elif choice == "4":
            if todo.view_tasks():
                while True:
                    user_input = input("Enter task number to delete (or 'c' to cancel): ").strip()
                    
                    if user_input.lower() == 'c':
                        print("[INFO] Deletion cancelled.")
                        break
                        
                    try:
                        idx = int(user_input) - 1
                        if todo.delete_task(idx):
                            break
                    except ValueError:
                        print("[ERROR] Please enter a valid numerical value.")
                    
        elif choice == "5":
            print("\n----------------------------------------")
            print("[INFO] Application closed. Stay productive.")
            print("----------------------------------------")
            break
        else:
            print("[ERROR] Invalid choice. Select a number between 1 and 5.")


if __name__ == "__main__":
    main()
