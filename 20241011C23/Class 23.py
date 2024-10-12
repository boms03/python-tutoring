class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def find(self,index):
        currentNode=self.head
        while (index>0):
            currentNode=currentNode.next
            index=index-1
        print("You have found your node")
        return currentNode
    
    def __init__(self,data):
        self.head=None
        self.tail=None



    def insert(self,data,index):
        if self.head=None and self.tail =None:
            newNode=Node(data)
            self.head=newNode
            self.tail=newNode
        else:
            positionNode= self.find(index-1)
            newNode= Node(data)
            newNode.next=positionNode.next
            positionNode.next=newNode
            

            
    def insertHead(self, data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        
    def insertTail(self,data):
        newNode=Node(data)
        self.tail.next=newNode
        self.tail=newNode




