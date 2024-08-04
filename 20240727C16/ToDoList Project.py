class ToDo:
    def __init__(self, title, description, isDone, priority):
        self.title = title
        self.description = description
        self.isDone = isDone
        self.priority = priority
    def __lt__(self,other):
        return self.priority>other.priority

ToDoList=[]
while True:
    print("Press 1, make your own todo.\nPress 2, show all your todo.\nPress 3, show your finsihed todo.\nPress 4, show your unfinsihed todo.")
    i = input()
    if i == '1':
        print("Make a todo:")
        title = input("title:")
        description = input("description:")
        isDone = input("Is done?:")
        priority = input("priority:")
        ToDo1=ToDo(title,description,isDone,priority)
        ToDoList.append(ToDo1)
        print("Successfully added a new todo")
        ToDoList.sort()

    elif i == '2':
        print("Showing all todo \n")
        for todo in ToDoList:
            print(todo.priority, todo.title, todo.description, todo.isDone)
        print()


    elif i == '3':
        print("Finished todo \n")
        for todo in ToDoList:
            if todo.isDone == 'yes':
                print(todo.priority, todo.title, todo.description, todo.isDone)
        print()


    elif i == '4':
        print("Work on todo \n")
        for todo in ToDoList:
            if todo.isdone == 'no':
                print(todo.priority, todo.title, todo.description, todo.isDone)
        print()

    elif i == '5':
        print("Update your todo \n")
        for index, todo in enumerate(ToDoList):
              print(index,todo.priority, todo.title, todo.description, todo.isDone)
        index = int(input("Which index will you update?"))
        p = input()
        if p == 'a':
            newTitle = input("New title:")
            todo = ToDoList[index]
            todo.title = newTitle
            

                    


              
