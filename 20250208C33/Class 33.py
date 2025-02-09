from collections import deque
class Node:
    def __init__(self,value,right,left):
        self.val=value
        self.right=right
        self.left=left
class Tree:
    def __init__(self,root):
        self.root=root
    def preorder(self,node):
        if not node:
            return
        print(node.value)
        self.preorder(node.left)
        self.preorder(node.rigt)
    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)
    def postorder(self,node):
        if not node:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value)


    def levelorder(self,root):
        queue=deque()
        queue.push(root)
        while not queue.empty():
            node=queue.popleft()
            print(node.value)
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)


        
newNode=Node(5,None,None)
newTree=Tree(newNode)

















    
