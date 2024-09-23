# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider addressing it soon."
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
        if time_bound == 'yes':
            reminder += " that requires attention today!"
        else:
            reminder += ". Plan to complete it when possible."
    case 'low':
        reminder = f"'{task}' is a low priority task"
        if time_bound == 'yes':
            reminder += " but you should consider it today!"
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered."

# Output the reminder
print(reminder)