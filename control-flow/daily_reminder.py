task = input("Enter your task: ")
priority = input("priority (high/medium/low): ")
time_bound = input("Is it time-bound?(yes/no): ")
match priority:
    case "high":
        reminder = (f"'{task}' is high priority task" )
    case "medium":
        reminder = (f"'{task}' is a medium priority task")
    case "low":
        reminder = (f"'{task}' is a low priority task")
    case_:
        print("invalid priority entered.please choose from high,medium, or low")
        exit()
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += "consider completing it when you have free time."
    print("Reminder:", reminder)
