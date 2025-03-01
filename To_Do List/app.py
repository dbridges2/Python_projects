
tasks = []
job = ""
#add_task takes input from user and adds it to the array tasks
def add_task():
   job = input("Enter task: ")
   tasks.append(job)
   print("Task " + str(tasks) + " added")
#remove_task first lists the elements in the tasks array with numbers next to them
#then asks to user to pick a task to remove with the number associated. Then I subtract one from the number
#and use pop to remove it from the Array and then print the tasks array again
def remove_task():
    global job, tasks
    numinArray = 0
    for job in tasks:
       numinArray += 1
       print(str(numinArray) + ". " + job)
    tasktoRemove = input("Pick a task to remove " + "1-" + (str(numinArray)) + ": ")
    print(tasktoRemove)
    tasktoremove1 = int(tasktoRemove) - 1
    tasks.pop(int(tasktoremove1))
    print(tasks)
#list_task lists the tasks.
def list_task():
   global job, tasks
   for job in tasks:
      print(job)

#main function uses the while True statement to keep running
# it lists the options a user can do  and puts that choice into the choice variable
#Then uses if statement to select one of the functions and runs that function
def main():
   while True:
    print("\n Menu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. List tasks")
    print("4. Exit")
    choice = input("What would you like to do? (enter number 1-4): ")
    if(str(choice) == "1"):
      add_task()
    elif(str(choice) == "2"):
      remove_task()
    elif(str(choice) == "3"):
      list_task()
    elif(str(choice) == "4"):
      print("Exitting program")
      break
    elif(str(choice) != "1" "2", "3", "4"):
       print(str(choice) + ": Is not a valid option try again")
        
main()