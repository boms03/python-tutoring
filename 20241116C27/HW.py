class Node:
    def __init__(self,data):
        self.data=data
        self.child=[]
    def addChild(self,node):
        #implement

class Tree:
    def __init__(self,root):
        self.root=root


newNode=Node(4)
newTree=Tree(newNode)

newNode2=Node(2)
newNode3=Node(5)
newNode4=Node(9)

newTree.root.child.append(newNode2)
newTree.root.child.append(newNode3)
newTree.root.child.append(newNode4)

newNode5=Node(4)
newNode6=Node(1)

newNode3.child.append(newNode5)
newNode3.child.append(newNode6)
