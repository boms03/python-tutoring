class ToDo:
    def __init__(self, title, description, isDone, priority):
        self.title = title
        self.description = description
        self.isDone = isDone
        self.priority = priority
    def __lt__(self,other):
        return self.priority>other.priority

ToDo1=ToDo('Homework', 'python', False, 1)
ToDo2=ToDo('Memorize', 'sadlier', False, 2)
ToDo3=ToDo('Study', 'spanish', False,3)
ToDo4=ToDo('Solve', 'math', False,3)
ToDo5=ToDo('Typing', 'Writing', False, 2)

ToDoList=[ToDo1, ToDo2,ToDo3, ToDo4, ToDo5] 
ToDoList.sort()
for ToDo in ToDoList:
    print(ToDo.priority, ToDo.title)
