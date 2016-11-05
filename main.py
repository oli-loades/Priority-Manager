def displayMenu(): #creates the menu of the program
    print("1 - Add a task to a list")
    print("2 - Remove a task")
    print("3 - Change priority of a task")
    print("4 - Promote a task")
    print("5 - Display tasks")
    print("6 - Load task from text files")
    print("7 - Save task to text file")
    print("0 - Exit")


def addTask(high,low): #allows user to add task
    task = input("enter the task") #stores the name of the task
    length = len(task) #stores how many characters task contains
    if task[length-1] == "H": #if the last character of task is H        
        task = task.rstrip("@H") #removes the high priority identifier from the string
        high.append(task) #add the task to the high protoity task list
        print(task, "has been added to the high priority list")
        return high  #return updated high priority list
    else: #if the last character of the string is not H
        low.append(task) #add the task to the low priority task list
        print(task, "has been added to the low priority list")
        return low #return updated low priority list      
        
def removeTask(high,low): #allows user to remove a task from the different lists
    priority = input("Enter the priority of the task?") #allows the user to enter the priority of the task
    pos = int(input("Enter the position in the list")) #used to identify the position in the list 
    if priority == "high": #if user enters high
        if pos <= len(high): #if the user input for position is in range
            print(high[pos], "has been removed") #show message of what has been removed
            high.remove(high[pos]) #remove item from the list
            return high #return updated high priority list
    elif priority == "low": #else if the user enters low
        if pos <= len(low): #if the user input for position is in range
            print(low[pos], "has been removed") #show message of what has been removed
            low.remove(low[pos]) #remove item from the list
            return low #return updated low priority list


def changePriority(high,low): #allows user to move items to the differnt lists
    priority = input("Enter the priority of the task?") #allows the user to enter the priority of the task
    pos = int(input("Enter the position in the list")) #used to identify the position in the list
    if priority == "high": #if input is high
        print(high[pos], "has been added to the low priority list") #show message of what has been changed
        low.insert(0,high[pos]) #add the element to the start of the low priority list
        high.remove(high[pos]) #remove item from the high priority list
    elif priority == "low": #if input is low
        print(low[pos], "has been added to the high priority list") #show message of what has been changed
        high.append(low[pos]) #add the element to the end of the high priority
        low.remove(low[pos]) #remove item from the low priority list
    return high #return updated high priority list
    return low #return updated low priority list


def promoteTask(high,low): #allows user to morve item up the lists
    priority = input("Enter the priority of the task?") #allows the user to enter the name of the task
    pos = int(input("Enter the position in the list")) #used to identify the position in the list
    if priority == "high": #if the user enters high
        if pos > 0: #if not dealing with the first element in the list
            promote = high.pop(pos) #removes element in positiuon pos and stores as a vriable
            high.insert(pos-1,promote) #take variable promote and moves it to position pos - 1 in the list
            print(promote, " has been moved to position" , pos - 1) #display a what task has been promoted
        else:
            print(high[pos], "cannot be promoted") #print if user is trying to promote first elemnt in the list          
    if priority == "low": #if the user enters low
        if pos > 0: #if not dealing with the first element in the list
            promote = low.pop(pos) #removes element in positiuon pos and stores as a vriable
            low.insert(pos-1,promote) #take variable promote and moves it to position pos - 1 in the list
            print(promote, " has been moved to position" , pos - 1) #display a what task has been promoted
        else: #if dealing with the first element of the low priority list
            promote = low[pos]
            high.append(low[pos]) #add the element to the end of the high priority list
            low.remove(low[pos])#remove the original element
            print(promote, " has been moved to the high priority list") #display a what task has been promoted
    return high #return updated high priority list
    return low #return updated low priority list           


def displayTasks(high,low): # prints out each item in each list
    print("High:") #header for high priority list
    for c in range(len(high)): #loop through the high priority list
        print(high[c]) #print an element of the list
    print("Low:") #header for low priority list
    for c in range(len(low)): #loop through the low priority list
        print(low[c]) #print an element of the list    


def loadTask(): #loads tasks form a text  fiel and stores them in teh appropriate lists
    highFile = open("HighPriority.txt" ,"r") #opens the high priority file in read
    lowFile = open("LowPriority.txt" ,"r") #opens the low priority file in read
    for line in highFile: #for each line in the high text file
        line = line.rstrip("\n") #remove line break
        high.append(line) #add line to the end of the high priority list  
    for line in lowFile: #for each line in the low priority text file
        line = line.rstrip("\n") #remove line break
        low.append(line) #add line to the end of the low priority list
    return high #return updated high priority list
    return low #return updated low priority list


def saveTask(high,low): #saves the items in each list to a text file 
    highFile = open("HighPriority.txt" ,"w") #opens the high priority file in write
    lowFile = open("LowPriority.txt" ,"w") #opens the low priority file in write
    for c in range(len(high)):#loops through the list
        line = high[c] + "\n" #converts each element in the list into a string
        highFile.write(line) #stores the high priority task list in the task file
    for c in range(len(low)): #loops through the list
        line = low[c] + "\n" #converts each element in the list into a string
        lowFile.write(line) #stores the low priority task list in the task file
    highFile.close() #closes the high priority file
    lowFile.close() #closes the low priority file


def quitProgram():
    print("Close") #print exit message
    exit() #terminates the program


low = [] #creates a list to store low priority tasks
high = [] #creates a list to store the high priority tasks    
displayMenu() #displays the menu of the program
valid = False #used to see if the user enter a number between 0 and 7
choice = 1
while valid == False or choice != 0: #loop until the user enters an number between 0 and 7
    choice = int(input("Select an option from the menu")) #stores the users input
    if choice >= 0 and choice <= 7:#if the user enters a number between 0 and 7
        print("Inpuit valid") # print a message informing the user they have entered a valid number
        valid = True # allows to exit the while loop
        if choice == 1: #if the user enters a 1
                addTask(high,low) #calls the function called addTask
                displayMenu() #display the menu
        elif choice == 2: #else if the user enters a 2
                removeTask(high,low) #calls the function called removeTask
                displayMenu() #display the menu
        elif choice == 3: #else if the user enters a 3
                changePriority(high,low) #calls the function called chagngePriority
                displayMenu() #display the menu
        elif choice == 4: #else if the user enters a 4
                promoteTask(high,low) #calls the function called promoteTask
                displayMenu() #display the menu
        elif choice == 5: #else if the user enters a 5
                displayTasks(high,low) #calls the function called displayTasks
                displayMenu() #display the menu
        elif choice == 6: #else if the user enters a 6
                low = []
                high = []
                loadTask() #calls the function called loadTask
                displayMenu() #display the menu
        elif choice == 7: #elseif the user enters a 7
                saveTask(high,low) #calls the function called saveTask
                displayMenu() #display the menu
        elif choice == 0: #elseif the user enters a 7
                quitProgram()
                
    else: #if the user enters anything that is not a number betwenn 0 and 7
        print("Input invalid, please enter a number from the menu") #print a message to inform them that the input was not correct
        choice = int(input("Select an option from the menu")) #allows the user to try again
