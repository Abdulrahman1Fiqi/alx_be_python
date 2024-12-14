task = input("Enter your task: ")
x = input("Priority (high/medium/low): ")
y = input("Is it time-bound? (yes/no): ")
match x:
    case "high":
        if y=="yes":
            print(f"Reminder: {task} is a {x} priority task that requires immediate attention today!")
        elif y=="no":
            print(f"Note: {task} is a {x} priority task. Consider completing it when you have free time.")
    case "medium":
        if y=="yes":
            print(f"Reminder: {task} is a {x} priority task that requires immediate attention today!")
        elif y=="no":
            print(f"Note: {task} is a {x} priority task. Consider completing it when you have free time.")
    case "low":
        if y=="yes":
            print(f"Reminder: {task} is a {x} priority task that requires immediate attention today!")
        elif y=="no":
            print(f"Note: {task} is a {x} priority task. Consider completing it when you have free time.")

