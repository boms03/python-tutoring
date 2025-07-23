'''Structuring: Tree Class—> Root and Node Class—> left child, right child

Find out how to make a Class Node
class Node:
    def __init__(self,value)
    self.value=value
    self.next=none

Make Tree/Node Class
Node Class --> left child, right child

Tree Class --> Root'''

class Node:
    def __init__(self,value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
        
class Tree:
    def __init__(self, root=None):
        self.root=root
    def inorder(self,node=None):
        if node==None:
            return
        print('first visit', node.value)
        self.inorder(node.left)
        print('return from left', node.value)
        print(node.value)
        self.inorder(node.right)
        print('return from right', node.value)
    def postorder(self,node=None):
        if node==None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value)
    def preorder(self,node=None):
        if node==None:
            return
        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right)




'''

Homework:
    
    inorder = LEFT, ROOT, RIGHT
class Tree:   
    def inorder(self,root=None):
        if node==None:
            return
        if node:
            inorder(node.left)
            print(node.value)
            inorder(node.right)


def --> inorder(self,root) 
terminating condition-->done with left
write recursion
    
    postorder = LEFT, RIGHT, ROOT
class postorder:
    def postorder(self,root=None):
        if node==None:
            return
        if node:
            postorder(node.left)
            postorder(node.right)
            print(node.value)

def ---> postorder(self,root) 
terminating condition
write recursion
    
    preorder = ROOT, LEFT, RIGHT
class preorder:   
    def preorder(self,root=None):
        if node==None:
            return
        if node:
            print(node.value)
            preorder(node.left)
            preorder(node.right)
        

        
def ---> preorder(self,root)        
terminating condition
write recursion'''




FirstNode=Node(50)
SecondNode=Node(20)
ThirdNode=Node(30, FirstNode,SecondNode)
'''Tree=Tree(SecondNode)'''

node_1 = Node(1)
node_4 = Node(4)
node_7 = Node(7)
node_9 = Node(9)

# Level 2 nodes
node_8 = Node(8, node_1, None)
node_2 = Node(2, node_4, node_7)
node_3 = Node(3, node_9, None)

# Level 1 nodes
node_6 = Node(6, node_8, node_2)

# Root node (Level 0)
root_node = Node(5, node_6, node_3)

Tree2=Tree(root_node)
print('inorder')
Tree2.inorder(root_node)
print('postorder')
Tree2.postorder(root_node)
print('preorder')
Tree2.preorder(root_node)




