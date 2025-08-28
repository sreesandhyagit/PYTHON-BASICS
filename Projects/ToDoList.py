to_do_list= {}
key=1

def list_menu():
    print("\n==========TO-DO-LIST-MENU==========")
    print("\t1. Add Task\n\t2. Show Task\n\t3. Mark Task as done\n\t4. Delete Task\n\t5. Exit")
    
def add_task():
    global key
    global to_do_list
    try:
        task_num=int(input("How many task you want to add : "))
        if task_num==0:
            print("\nNo task added")
        else:               
            for k in range(1,task_num+1):
                # global key
                task=input(f"Enter the task {k} : ")
                to_do_list[key]={'task':task,'done':False}
                key=key+1
            print(f"\n{task_num} task added!")
        print("\nTotal tasks : ",len(to_do_list)) 
    except Exception as e:
        print("\nError : ",e)
        print("Please enter a valid  number!")        

def show_task():
    global to_do_list
    if not to_do_list:
        print("\nNo task found!")
        print("Please add task!")
    else:
        for k,v in to_do_list.items():
            status="Done" if v["done"] else "Not Done"
            print(f"{k}. {v['task']} - {status} ")

def mark_done():
    global to_do_list
    if not to_do_list:
        print("\nNo task found!")
        print("Please add task!")
    else:
        try:
            key=int(input("Enter the task number to mark as done : "))
            if key in to_do_list:
                if to_do_list[key]['done']==False:
                    to_do_list[key]['done']=True
                    print(f"\nTask {to_do_list[key]['task']} marked as Done")
                else:
                    print("\nTask already marked as done!!") 
                    yn=input("Do you want to undo mark as done : [yes/no]") 
                    if yn=="yes": 
                        to_do_list[key]['done']=False
                        print(f"\nTask {to_do_list[key]['task']} marked as Not Done")
            else:          
                print("\nInvalid Task Number!!")
        except Exception as e:
            print("\nError : ",e)
            print("Please enter a valid  number!")        
    
def delete_task():
    global to_do_list
    if not to_do_list:
        print("\nNo task found!")
        print("Please add task!")
    else:
        try:
            key=int(input("Enter the task number to delete : "))
            if key in to_do_list:
                deleted=to_do_list.pop(key) 
                print(f"Task {deleted['task']} deleted!")
            else:
                print("\nInvalid Task Number!!")
        except Exception as e:
            print("\nError : ",e)
            print("Please enter a valid  number!")
   
#main
while True:
    list_menu()
    try:
        choice=int(input("Enter your choice [1 - 5] : "))
        match choice:
            case 1:
                add_task()
            case 2:
                show_task()
            case 3:
                mark_done()
            case 4:
                delete_task()
            case 5:
                print("Exited Successfully")
                break
            case __:
                print("\nInvalid Choice!! Make sure option is in 1-5")
    except Exception as e:
        print("\nError : ",e)
        print("Please enter a valid  number!")

            