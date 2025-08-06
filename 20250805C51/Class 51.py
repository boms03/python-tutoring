class Node:
    def __init__(self,value,children=[]):
        self.value=value
        self.children=children

class Tree:
    def __init__(self,root=None):
        self.root=root
        
    def preorder(self, node):
        if node==None:
            return
        print(node.value)
        for child in node.children:
            self.preorder(child)

    def inorder(self, node):
        if node==None:
            return
        for child in node.children:
            self.inorder(child)
            print(node.value)
        
    
    def postorder(self, node):
        if node==None:
            return
        for child in node.children:
            self.postorder(child)
        print(node.value)


        


    def findHeight(self, n, node):
        if node==None:
            return 0
        max_height=-1
        for child in node.children:
            child_height=self.findHeight(child)
            if max_height<child_height:
                max_height=child_height
        return max_height+1


    def findDepth(self,n,node,depth):
        if node==None:
            return 0
        if node.value==n:
            return depth
        for child in node.children:
            self.findDepth(n,child,depth+1)
            
            
            
            
        
        
        
            
        
 




            

fruitlist=['apple', 'banana', 'grape']
fruitlist[0,3]
print(fruitlist[0])
print(fruitlist[1])
print(fruitlist[2])
for i in fruitlist:
    print(i)

for i in range(0,len(fruitlist)):
    print(fruitlist[i])
    
