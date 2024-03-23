# Create a list to store the tasks
tasks = []

# Define a function to add a task
def add_task(task):
    tasks.append(task)

# Define a function to complete a task
def complete_task(task):
    tasks.remove(task)

# Define a function to remove a task
def remove_task(task):
    tasks.remove(task)

# Get the user input
task = input("Enter a task: ")

# Add the task to the list
add_task(task)

# Print the list of tasks
print("Tasks:")
for task in tasks:
    print(task)

# Get the user input
task = input("Enter a task to complete: ")

# Complete the task
complete_task(task)

# Print the list of tasks
print("Tasks:")
for task in tasks:
    print(task)

# Get the user input
task = input("Enter a task to remove: ")

# Remove the task
remove_task(task)

# Print the list of tasks
print("Tasks:")
for task in tasks:
    print(task)