class node:
    def __init__(self,data):
        self.data = data
        self.next = None
node1=node(1)
node2=node(4)
node3=node(8)

node1.next=node2
node2.next=node3

currentNode=node1
while(currentNode is not None):
    if currentNode.data==8:
        print("We found 8")
        break
    else:
        currentNode=currentNode.next
