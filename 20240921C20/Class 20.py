fruitlist=[]
while True:
    i=input()
    if i=='1':
        fruit=input()
        fruitlist.append(fruit)
    if i=='2':
        fruitlist.pop()
    print(fruitlist)



class Stack:
    def __init__(self):
        self.l = []
    def push(self, i):
        self.l.append(i) 
        print("push :", self.l)

    def pop(self):
        self.l.pop()
        print("pop :",self.l)

    def top(self):
        if self.is_empty():
            print()
        index = len(self.l)-1
        print(self.l[index])

    def is_empty(self):
        if len(self.l)==0:
            return True
        else:
            return False
    def size(self):
        print(len(self.l))
