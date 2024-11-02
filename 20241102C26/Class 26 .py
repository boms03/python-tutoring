class Node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

class Tree:
    def __init__(self,root):
        self.root=root


rootNode=Node(4)
rootNode.leftchild=Node(2)
rootNode.rightchild=Node(10)
rootNode.rightchild.leftchild= Node(3)
rootnode.rightchild.rightchild= Node(5)
tree=Tree(rootNode)


