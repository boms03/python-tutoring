def display_todos(todos, filter_done=None):
    todos.sort()
    for todo in todos:
        if filter_done==None:
            print(todo.priority, todo.title, todo.description, todo.isDone)
        elif filter_done==todo.isDone:
            print(todo.priority, todo.title, todo.description, todo.isDone)
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
    elif i == '2':
        ToDoList.sort()
        print("Showing all todo \n")
        display_todos(ToDoList)

    elif i == '3':
        print("Finished todo \n")
        display_todos(ToDoList,'yes')

    elif i == '4':
        print("Work on todo \n")
        display_todos(ToDoList,'no')
        
    elif i == '5':
        print("Update your todo \n")
        for index, todo in enumerate(ToDoList):
              print(index,todo.priority, todo.title, todo.description, todo.isDone)
        index =int(input("Which index will you update?"))
        p = input()
        if p == 'a':
            newTitle = input("New title:")
            todo = ToDoList[index]
            todo.title = newTitle
        elif p == 'b':
            newDescription = input("New description:")
            todo= ToDoList[index]
            todo.description = newDescription
        elif p == 'c':
            newisDone = input("New isDone:")
            todo = ToDoList[index]
            todo.isDone = newisDone
        elif p == 'd':
            newPriority = input("New Priority:")
            todo = ToDoList[index]
            todo.priority = newPriority





            
