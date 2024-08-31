print("SHEDULE YOUR ROUTINE")
tasks=[]
total_task=int(input("ENTER THE TOTAL NUMBER OF TASKS "))
for i in range(1,total_task+1):
    name=input("enter task = ")
    tasks.append(name)
print("PRESS 1 to ADD : 2 to UPDATE : 3 to DELETE : 4 to SHOW : 5 to EXIT")
while True:
    operation=int(input("ENTER YOUR CHOICE "))
    if operation==1:
        n=input("ENTER NEW TASK ")
        tasks.append(n)
    elif operation == 2:
         a=input("ENTER TASK NAME YOU WANT TO UPDATE ")
         if a in tasks:
             b=input("ENTER THE UPDATED TASK ")
             ind=tasks.index(a)
             tasks[ind]=b
             print("TASK UPDATED SUCCESSFULLY ")
         else:
             print("INVALID CHOICE ")
    elif operation == 3:
         x=input("ENTER THE TASK YOU WANT TO DELETE ")
         if x in tasks:
             ind=tasks.index(x)
             del tasks[ind]
             print("TASK DELETED SUCCESSFULLY ")
    elif operation == 4:
         print(tasks)
    elif operation == 5:
         print ("CLOSING THE PROGRAM")
         break
    
    else:
         print("INVALID CHOICE")