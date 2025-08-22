import time as t

tasks=[]
completed=[]

print("Welcome to to-do list application")

def add_task(a):
    tasks.append(a)
    t.sleep(1)
    print("\n Task added successfully")
    
def remove_task(a):
       tasks.pop(a-1)
       t.sleep(1)
       print("\n Task removed successfully")
       
def update_status(a):
    completed.append(a)
    tasks.remove(a)
    t.sleep(1)
    print(f"\n Task:{a} marked as completed")
    
def view_task():
    print("\nTasks:")
    for i,tsk in enumerate(tasks):
      print(f"{i}.{tsk}")
    t.sleep(1)  
    
def view_completed():
    print("\n Completed Tasks:")
    for i,tsk in enumerate(completed):
      print(f"{i}.{tsk}")
    t.sleep(1)
    
def clear_all_task():
    tasks.clear()
    t.sleep(1)

def clear_all_completed_task():
    completed.clear()
    t.sleep(1)
    
while True:

    t.sleep(1)
    print("1.Add task")
    print("2.Remove task")
    print("3.Update status")
    print("4.View task")
    print("5.View completed task")
    print("6.Clear all task")
    print("7.Clear all task")
    print("8.Reset application")
    print("9.Exit")
    
    try:
        x=int(input("Enter you choice:"))
    except NameError:
        print("\nNo valid input")
        continue
    except Exception:
        print("\nEnter your input as integer")
        continue
        
    if x==1:
        a=str(input("Enter your task:"))
        add_task(a)
        
    elif x==2:
        try:
          if not tasks:
             print("\nNo task is added")
          else:
             a=int(input("Enter the task index to remove:"))
             remove_task(a)
        except ValueError:
          print("\nPlease enter input as integer")
          
    elif x==3:
          if not tasks:
             print("\nNo task is added")
          else:
             a=input("Enter the task to update:")
             if a in tasks:
                update_status(a)
             else:
                print(f"{a} not in task")
              
    elif x==4:     
          if not tasks :
              print("\nNo task is added")
          else:
              view_task()
              
    elif x==5: 
          if not completed:
              print("\nNo completed task is added")
          else:
              view_completed()    
              
    elif x==6:
           clear_all_task()

    elif x==7:
           clear_all_completed_task()

    elif x==8:
           clear_all_task()
           clear_all_completed_task()
           
    elif x==9:
           break
           
    else :
           print("\nEnter the valid input")
           
    t.sleep(1) 
    print("\n")
