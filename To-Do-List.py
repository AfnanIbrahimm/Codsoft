tasks = []  #Creating a List to Store Data

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' Added Successfully!")

def view_tasks():
    if not tasks:
        print("NO-Tasks Found!")
    else:
        print("\n To-Do List: ")
        for idx, task in enumerate(tasks, start = 1):
            print(f"{idx}. {task}")

def update_task(index,new_task):
    if 0 <=index< len(tasks):
        tasks[index] = new_task
        print("Task Updated Successfully!")
    else:
        print("Invalid Tasks Number")

def delete_tasks(index):
    if 0 <= index <len(tasks):
        remove_task = tasks.pop(index)
        print(f"task '{remove_task}' Removed!")
    else:
        print("Invalid Task Number.")

def main():
    while True: 
        print("\nTo-Do List Process")
        print("1. Add Task")
        print("2. View Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        CHOICE = input("Enter Your Choice: ")

        if CHOICE == "1":
            Task = input("Enter Task: ")
            add_task(Task)
        
        elif CHOICE == "2":
             view_tasks()
        
        elif CHOICE == "3":
            view_tasks()
            index = int(input("Enter a Task Number to update:")) - 1
            new_task = input("Enter a New Task: ")
            update_task(index,new_task)  # type: ignore
        
        elif CHOICE =="4":
            view_tasks()
            index = int(input("Enter a Task Number to Delete:")) - 1
            delete_tasks(index)
        
        elif CHOICE == "5":
            print("EXITINGG ...")
            break
        
        else:
            print("Invalid CHOICE! Try Again.")

if __name__ == "__main__":
    main()