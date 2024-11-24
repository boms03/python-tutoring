class Node:
    def __init__(self,data):
        self.data=data
        self.child=[]
    def addChild(self,node):
        self.child.append(node)
      

class Tree:
    def __init__(self,root):
        self.root=root


newNode=Node(4)
newTree=Tree(newNode)

newNode2=Node(2)
newNode3=Node(5)
newNode4=Node(9)

newTree.root.addchild (newNode2)
newTree.root.addchild(newNode3)
newTree.root.addchild(newNode4)

newNode5=Node(4)
newNode6=Node(1)

newNode3.addchild(newNode5)

newNode3.addchild(newNode6)


