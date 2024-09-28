class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def printFront(self):
        if len(self.s1)==0:
            print("Queue is empty")
        else:
            print("Front is ", self.s1[0])
    def printRear(self):
        if len(self.s1)==0:
            print("Queue is empty")
        else:
            print("Rear is ", self.s1[len(self.s1)-1])
            
    
    def enQueue(self,x):
        self.s1.append(x)
        print("enqueue :", self.s1)

    def deQueue(self):
        if len(self.s1)==0:
            print("Queue is empty")
        else:
            del self.s1[0]
            print("enqueue :", self.s1)


queue=Queue()
while True:
    i=input()
    if i=="1":
        print("What would you like to input?")
        e=input()
        queue.enQueue(e)
    if i=="2":
        queue.deQueue()
    if i=="3":
        print(queue.s1)
    if i=="4":
        queue.printFront()
    if i=="5":
        queue.printRear()
    if i=='6':
        break
