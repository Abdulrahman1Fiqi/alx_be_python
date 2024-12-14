task = input("Enter your task: ")
x = input("Priority (high/medium/low): ")
y = input("Is it time-bound? (yes/no): ")
match x:
    case "high":
        if y=="yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if y=="yes":
            print("Reminder: 'Finish project report' is a medium priority task that requires immediate attention !")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case "low":
        if y=="yes":
            print("Reminder: 'Finish project report' is a low priority task that requires immediate attention !")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")

