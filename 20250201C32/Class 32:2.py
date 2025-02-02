class Treenode:
    def __init__(self,val,left,right):
        self.left= left
        self.right= right
        self.val= val
class Tree:
    def __init__(self, root):
        self.root=root

    def preorder(self,root):
        if not root:
            return
        print(root.val)
        preorder(root.left)
        preorder(root.right)
        
